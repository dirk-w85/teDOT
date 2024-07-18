import requests
import json
import sys

API_URL = 'https://api.thousandeyes.com/v6/groups.json'
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

def generate_mermaid_diagram(label):
    # Mermait Frontmatter Code https://mermaid.js.org/config/configuration.html?#frontmatter-config
    mermaid_lines = ["---"]
    mermaid_lines.append("title: "+label["name"])
    mermaid_lines.append("config:")
    mermaid_lines.append("  theme: base")
    mermaid_lines.append("---")

    # Start of the Diagram Definition
    mermaid_lines.append("flowchart LR")

    # Getting Label Details (includes Tests and Agents)
    labelDetails = get_thousandeyes("https://api.thousandeyes.com/v6/groups/"+str(label["groupId"]))

    if "tests" in labelDetails["groups"][0]:
        for test in labelDetails["groups"][0]["tests"]:
            # Checking if Test-Type is supported in teDOT
            if supported_tests(test):
                test_id = test['testId']
                test_name = test['testName']
                mermaid_lines.append(f'{test_id}("{test_name}"<br>Type: {test["type"]}, Interval: {test["interval"]}s):::teTest')

                # Getting the Agent Details
                test_agents = get_thousandeyes(test['apiLinks'][0]['href'])

                # Looping over the list of Agents in the Test
                for agent in test_agents["test"][0]["agents"]:
                    agent_id = agent['agentId']
                    agent_name = agent['agentName']
                    agent_type = agent['agentType']
                    if agent_type == "Enterprise":
                        agent_ip = "<br>IP: "+agent["ipAddresses"][0]
                    else:
                        agent_ip = ""
                    mermaid_lines.append(f'{agent_id}(["{agent_name}{agent_ip}<br>({agent_type} Agent)"]):::teAgent --- {test_id}')

                # Creating Test Target per Type
                mermaid_lines = test_target(test,mermaid_lines)

        # Just some Formating
        mermaid_lines.append("classDef teAgent fill:#FA6800")
        mermaid_lines.append("classDef teTest fill:#DAE8FC")
        mermaid_lines.append("classDef teTarget fill:#FFF2CC")

        return "\n".join(mermaid_lines)

# Step 0: Welcome Message
print("\nWelcome! Please wait while we create your Mermaid Code...")

# Getting all Labels 
labels = get_thousandeyes(API_URL)
if labels:
    for label in labels["groups"]:
        # Checking for Test-Labels which are not Built-In
        if label["type"] == "tests" and label["builtin"] == 0:
            print(f'\n\n##### START - Label: {label["name"]} - START #####')
            mermaid_diagram = generate_mermaid_diagram(label)

            print(mermaid_diagram) 
            with open('mermaid_diagram.md', 'a') as f:
                f.write(f'\n##### START - Label: {label["name"]} - START #####\n')
                f.write(mermaid_diagram+"\n\n")
                f.write(f'##### END - Label: {label["name"]} - END #####\n')                

            print(f'##### END - Label: {label["name"]} - END #####\n')
else:
    print("Failed to retrieve test configuration")
