import requests
import json
import sys

API_URL = 'https://api.thousandeyes.com/v7/alerts/rules'
API_TOKEN = sys.argv[1]

def get_thousandeyes(url):
    headers = {
        'Authorization': "Bearer "+API_TOKEN,
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None    

def test_target(test, mermaid_lines):
    if test["type"] == "agent-to-server":
        mermaid_lines.append(f"{test['testId']} --Trace: {test['pathTraceMode']}<br>Protocol: {test['protocol']}<br>DSCP: {test['dscpId']} --> {test['testId']}_server([{test['server']}]):::teTarget")

    if test["type"] == "agent-to-agent":
        resp = get_thousandeyes("https://api.thousandeyes.com/v7/agents/"+str(test['targetAgentId']))
        targetAgent = resp["agentName"]
        agent_type = resp["agentType"]
        mermaid_lines.append(f'{test["testId"]} --Trace: {test["pathTraceMode"]}<br>Protocol: {test["protocol"]}/{test["port"]}<br>DSCP: {test["dscpId"]} --> {test["testId"]}_agent(["{targetAgent}<br>({agent_type} Agent)"]):::teTarget')

    if test["type"] == "dns-server":
        test_dnsServers = get_thousandeyes(test['apiLinks'][0]['href'])
        for dnsServer in test_dnsServers["test"][0]["dnsServers"]:
            dnsServer_id = dnsServer['serverId']
            dnsServer_name = dnsServer['serverName']

            # for next version            
            #mermaid_lines.append(f"{test['testId']} --Trace: {test['pathTraceMode']}, Protocol: {test['dnsTransportProtocol']} --> {dnsServer_id}([{dnsServer_name}])")
            mermaid_lines.append(f"{test['testId']} --Trace: {test['pathTraceMode']} --> {dnsServer_id}([{dnsServer_name}]):::teTarget")

    if test["type"] == "dns-trace":
        mermaid_lines.append(f"{test['testId']} --DNS Query-Class: {test['dnsQueryClass']}<br>DNS Protocol: {test['dnsTransportProtocol']} --> {test['testId']}_domain({test['domain']}):::teTarget")


    if test["type"] == "http-server" or test["type"] == "page-load" :
        mermaid_lines.append(f"{test['testId']} --Trace: {test['pathTraceMode']}<br>Protocol: {test['protocol']} --> {test['testId']}_url([{test['url'].rstrip('/')}]):::teTarget")
        
    return mermaid_lines

def supported_tests(test):
    supportedTests = ["agent-to-server","agent-to-agent","dns-server","dns-trace","http-server","page-load"]

    if test["enabled"] == 0:
        return False
    else:
        if test["type"] in supportedTests:
            return True
        else:
            print(f'Test Type {test["type"]} not yet suppored')
            return False

def generate_mermaid_diagram(alertId):
    # Getting Label Details (includes Tests and Agents)
    alertDetails = get_thousandeyes("https://api.thousandeyes.com/v7/alerts/rules/"+str(alertId))

    # Mermait Frontmatter Code https://mermaid.js.org/config/configuration.html?#frontmatter-config
    mermaid_lines = ["---"]
    mermaid_lines.append("title: Alert Rule - "+alertDetails["ruleName"])
    mermaid_lines.append("config:")
    mermaid_lines.append("  theme: base")
    mermaid_lines.append("---")

    # Start of the Diagram Definition
    mermaid_lines.append("flowchart LR")

    # Replace characters in alert expression to work with mermaid
    alertDetails["expression"] = alertDetails["expression"].replace('"', "'")

    mermaid_lines.append(f'{alertDetails["ruleId"]}("{alertDetails["ruleName"]}<br>Sev: {alertDetails["severity"].upper()}"):::teRule --- {alertDetails["ruleId"]}_exp(["{alertDetails["expression"]}"])')
    #print("\n".join(mermaid_lines))

    if "tests" in alertDetails:
        #print(alertDetails)
        for test in alertDetails["tests"]:
            #mermaid_lines.append(f'{test['testId']}("{test['testName']}"):::teTest')
            #mermaid_lines.append(f'{alertDetails["ruleId"]} --> {test['testId']}')
            mermaid_lines.append(f'{test["testId"]}("Test: {test["testName"]}"):::teTest --> {alertDetails["ruleId"]}')

    
    if "email" in alertDetails["notifications"]:
        recepientCount = 0
        if "recipients" in alertDetails["notifications"]["email"]:
            mermaid_lines.append(f'{alertDetails["ruleId"]}_exp --> {alertDetails["ruleId"]}_email("Email"):::teNoti')
        #if len(alertDetails["notifications"]["email"]["recipients"]) >= 1:
            for recepient in alertDetails["notifications"]["email"]["recipients"]:


                recipientObj = recepient.replace(".","_")
                recipientObj = recipientObj.replace("@","_")
                #mermaid_lines.append(f'{alertDetails["ruleId"]}_email --> {alertDetails["ruleId"]}_rec{str(recepientCount)}(["{recepient}"])')
                mermaid_lines.append(f'{alertDetails["ruleId"]}_email --> {recipientObj}(["<p>{recepient}</p>"])')
                recepientCount=recepientCount+1

    if "thirdParty" in alertDetails["notifications"]:
        mermaid_lines.append(f'{alertDetails["ruleId"]}_exp --> {alertDetails["ruleId"]}_3rd("3rd Party"):::teNoti')
    if "webhook" in alertDetails["notifications"]:
        mermaid_lines.append(f'{alertDetails["ruleId"]}_exp --> {alertDetails["ruleId"]}_webhook("Webhook"):::teNoti')
    if "customWebhook" in alertDetails["notifications"]:
        mermaid_lines.append(f'{alertDetails["ruleId"]}_exp --> {alertDetails["ruleId"]}_webhook("Webhook"):::teNoti')
        for webhook in alertDetails["notifications"]["customWebhook"]:
            mermaid_lines.append(f'{alertDetails["ruleId"]}_webhook --> {webhook["integrationId"]}("{webhook["integrationName"]}")')

            mermaid_lines.append(f'{webhook["integrationId"]} --> {webhook["integrationId"]}_target("<p>{webhook["target"]}</p>")')


    # Just some Formating
    mermaid_lines.append("classDef teTest fill:#FA6800")
    mermaid_lines.append("classDef teRule fill:#DAE8FC")
    mermaid_lines.append("classDef teNoti fill:#FFF2CC")

    return "\n".join(mermaid_lines)

# Step 0: Welcome Message
print("\nWelcome! Please wait while we create your Mermaid Code...")

# Getting all Labels 
alertRules = get_thousandeyes(API_URL)
if alertRules:
    for alertRule in alertRules["alertRules"]:
        print(f'\n\n##### START - Alert Rule: {alertRule["ruleName"]} - START #####')
        mermaid_diagram = generate_mermaid_diagram(alertRule["ruleId"])

        print(mermaid_diagram)           

        print(f'##### END - Alert Rule: {alertRule["ruleName"]} - END #####\n')
else:
    print("Failed to retrieve test configuration")
