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

def test_target(test, graphviz_lines):
    if test["type"] == "agent-to-server":
        graphviz_lines.append(f"  target_{test['testId']} --Trace: {test['pathTraceMode']}<br>Protocol: {test['protocol']}<br>DSCP: {test['dscpId']} --> {test['testId']}_server([{test['server']}]):::teTarget")

    if test["type"] == "agent-to-agent":
        resp = get_thousandeyes("https://api.thousandeyes.com/v7/agents/"+str(test['targetAgentId']))
        targetAgent = resp["agentName"]
        agent_type = resp["agentType"]
        graphviz_lines.append(f'  target_{test["testId"]} --Trace: {test["pathTraceMode"]}<br>Protocol: {test["protocol"]}/{test["port"]}<br>DSCP: {test["dscpId"]} --> {test["testId"]}_agent(["{targetAgent}<br>({agent_type} Agent)"]):::teTarget')

    if test["type"] == "dns-server":
        test_dnsServers = get_thousandeyes(test['apiLinks'][0]['href'])
        for dnsServer in test_dnsServers["test"][0]["dnsServers"]:
            dnsServer_id = dnsServer['serverId']
            dnsServer_name = dnsServer['serverName']

            # for next version            
            #graphviz_lines.append(f"{test['testId']} --Trace: {test['pathTraceMode']}, Protocol: {test['dnsTransportProtocol']} --> {dnsServer_id}([{dnsServer_name}])")
            graphviz_lines.append(f'  target_{test['testId']}_{dnsServer_id} [label="{dnsServer_name}"]')

    if test["type"] == "dns-trace":
        graphviz_lines.append(f"  target_{test['testId']} --DNS Query-Class: {test['dnsQueryClass']}<br>DNS Protocol: {test['dnsTransportProtocol']} --> {test['testId']}_domain({test['domain']}):::teTarget")


    if test["type"] == "http-server" or test["type"] == "page-load" :
        graphviz_lines.append(f'  target_{test['testId']} [label="{test['url'].rstrip('/')}"]')
        
    return graphviz_lines

def test_target_details(test, graphviz_lines):
    if test["type"] == "agent-to-server":
        graphviz_lines.append(f"  target_{test['testId']} --Trace: {test['pathTraceMode']}<br>Protocol: {test['protocol']}<br>DSCP: {test['dscpId']} --> {test['testId']}_server([{test['server']}]):::teTarget")

    if test["type"] == "agent-to-agent":
        resp = get_thousandeyes("https://api.thousandeyes.com/v7/agents/"+str(test['targetAgentId']))
        targetAgent = resp["agentName"]
        agent_type = resp["agentType"]
        graphviz_lines.append(f'  target_{test["testId"]} --Trace: {test["pathTraceMode"]}<br>Protocol: {test["protocol"]}/{test["port"]}<br>DSCP: {test["dscpId"]} --> {test["testId"]}_agent(["{targetAgent}<br>({agent_type} Agent)"]):::teTarget')

    if test["type"] == "dns-server":
        test_dnsServers = get_thousandeyes(test['apiLinks'][0]['href'])
        for dnsServer in test_dnsServers["test"][0]["dnsServers"]:
            dnsServer_id = dnsServer['serverId']
            dnsServer_name = dnsServer['serverName']

            # for next version            
            #graphviz_lines.append(f"{test['testId']} --Trace: {test['pathTraceMode']}, Protocol: {test['dnsTransportProtocol']} --> {dnsServer_id}([{dnsServer_name}])")
            graphviz_lines.append(f"  target_{test['testId']} --Trace: {test['pathTraceMode']} --> {dnsServer_id}([{dnsServer_name}]):::teTarget")

    if test["type"] == "dns-trace":
        graphviz_lines.append(f"  target_{test['testId']} --DNS Query-Class: {test['dnsQueryClass']}<br>DNS Protocol: {test['dnsTransportProtocol']} --> {test['testId']}_domain({test['domain']}):::teTarget")


    if test["type"] == "http-server" or test["type"] == "page-load" :
        graphviz_lines.append(f'  target_{test['testId']} [label="{test['url'].rstrip('/')}"]')
        
    return graphviz_lines

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

def generate_graphviz_diagram(label):


    node_agent_attributes = 'shape=rectangle,color="#f15d22", style=filled'
    node_test_attributes = 'color="#00bceb", style=filled , shape=rectangle'
    node_target_attributes = 'color="#74bf4b", style=filled , shape=folder'

    # Mermait Frontmatter Code https://graphviz.js.org/config/configuration.html?#frontmatter-config
    graphviz_lines = ['digraph G {']
    graphviz_lines.append('  fontname="Arial"')
    graphviz_lines.append('  beautify=true')
    graphviz_lines.append('  center=true')
    graphviz_lines.append('  rankdir = LR')    

    # Getting Label Details (includes Tests and Agents)
    labelDetails = get_thousandeyes("https://api.thousandeyes.com/v6/groups/"+str(label["groupId"]))

    testRank = "  {rank = same;"
    if "tests" in labelDetails["groups"][0]:
        graphviz_lines.append('\n  // Tests') 
        for test in labelDetails["groups"][0]["tests"]:
            # Checking if Test-Type is supported in teDOT
            if supported_tests(test):
                test_id = test['testId']
                test_name = test['testName']                
                graphviz_lines.append(f'  test_{test_id}[label="{test_name} Type: {test["type"]}, Interval: {test["interval"]}s", {node_test_attributes}]')
                testRank = testRank+" test_"+str(test['testId'])+";"
            testRank = testRank+" }"
            graphviz_lines.append(testRank)
            testRank = "  {rank = same;"

    agentRank = "  {rank = same;"
    agentIdList = []
    if "tests" in labelDetails["groups"][0]:
        graphviz_lines.append('\n  // Agents') 
        for test in labelDetails["groups"][0]["tests"]:
            # Checking if Test-Type is supported in teDOT
            if supported_tests(test):
                test_id = test['testId']
                test_name = test['testName']

                # Getting the Agent Details
                test_agents = get_thousandeyes(test['apiLinks'][0]['href'])

                # Looping over the list of Agents in the Test
                for agent in test_agents["test"][0]["agents"]:
                    if agent['agentId'] not in agentIdList:
                        agentIdList.append(agent['agentId'])

                # Looping over the list of Agents in the Test
                for agent in test_agents["test"][0]["agents"]:
                    agent_id = agent['agentId']
                    agent_name = agent['agentName']
                    agent_type = agent['agentType']   
  
                    if agent_type == "Enterprise" and "ipAddresses" in agent:
                        #print(agent["ipAddresses"])
                        agent_ip = " IP: "+agent["ipAddresses"][0]
                    else:
                        agent_ip = ""
                    agentRank = agentRank+" agent_"+str(agent['agentId'])+";"
                    #graphviz_lines.append(f'  agent_{agent_id} [label="{agent_name}{agent_ip} ({agent_type} Agent)", {node_agent_attributes}]')
                agentRank = agentRank+" }"
                graphviz_lines.append(agentRank)
                agentRank = "  {rank = same;"
    print(agentIdList)
    agentRank = agentRank+" }"
    for agent in agentIdList:
        graphviz_lines.append(f'  agent_{agent} [label="{agent}{agent} ({agent} Agent)", {node_agent_attributes}]')
        agentRank = agentRank+" agent_"+str(agent)+";"
    graphviz_lines.append(agentRank)
    agentRank = "  {rank = same;"

    targetRank = "  {rank = same;"
    if "tests" in labelDetails["groups"][0]:
        graphviz_lines.append('\n  // Targets') 
        for test in labelDetails["groups"][0]["tests"]:
            # Checking if Test-Type is supported in teDOT
            if supported_tests(test):
                test_id = test['testId']
                test_name = test['testName']

                graphviz_lines = test_target(test,graphviz_lines)
                
                targetRank = targetRank+" }"
                graphviz_lines.append(targetRank)
                targetRank = "  {rank = same;"

    if "tests" in labelDetails["groups"][0]:
        graphviz_lines.append('\n  // Links') 
        for test in labelDetails["groups"][0]["tests"]:
            # Checking if Test-Type is supported in teDOT
            if supported_tests(test):
                test_id = test['testId']
                test_name = test['testName']
                #graphviz_lines.append(f'  test_{test_id}[label="{test_name} Type: {test["type"]}, Interval: {test["interval"]}s"]')

                # Getting the Agent Details
                test_agents = get_thousandeyes(test['apiLinks'][0]['href'])

                # Looping over the list of Agents in the Test
                AgentToTest = "  {"
                for agent in test_agents["test"][0]["agents"]:
                    agent_id = agent['agentId']
                    agent_name = agent['agentName']
                    agent_type = agent['agentType']        
                    if agent_type == "Enterprise" and "ipAddresses" in agent:
                        #print(agent["ipAddresses"])
                        agent_ip = " IP: "+agent["ipAddresses"][0]
                    else:
                        agent_ip = ""
                    AgentToTest = AgentToTest + " agent_"+str(agent['agentId'])    
                    #graphviz_lines.append(f'  agent_{agent_id} [label="{agent_name}{agent_ip} ({agent_type} Agent)", {node_agent_attributes}]')

                AgentToTest = AgentToTest + " } -> test_"+str(test['testId'])
                #AgentToTest = AgentToTest + " } -> test_"+str(test['testId'])+'[label="TCP/443 Path: Classic", style=dashed]'
                graphviz_lines.append(AgentToTest)
                # Creating Test Target per Type
                #graphviz_lines = test_target(test,graphviz_lines)

        graphviz_lines.append('}')

        return "\n".join(graphviz_lines)

# Step 0: Welcome Message
print("\nWelcome! Please wait while we create your Graphviz DOT Code...")

# Getting all Labels 
labels = get_thousandeyes(API_URL)
if labels:
    for label in labels["groups"]:
        # Checking for Test-Labels which are not Built-In
        if label["type"] == "tests" and label["builtin"] == 0:
            print(f'\n\n##### START - Label: {label["name"]} - START #####')
            graphviz_diagram = generate_graphviz_diagram(label)

            print(graphviz_diagram) 
            #with open('graphviz_diagram.md', 'a') as f:
            #    f.write(f'\n##### START - Label: {label["name"]} - START #####\n')
            #    f.write(graphviz_diagram+"\n\n")
            #    f.write(f'##### END - Label: {label["name"]} - END #####\n')                

            print(f'##### END - Label: {label["name"]} - END #####\n')
else:
    print("Failed to retrieve test configuration")
