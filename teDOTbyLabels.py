import requests
import json
import sys

# Replace these with your actual ThousandEyes API credentials and API endpoint
API_URL = 'https://api.thousandeyes.com/v6/groups.json'
API_TOKEN = sys.argv[1]

def get_thousandeyes_labels():
    headers = {
        'Authorization': "Bearer "+API_TOKEN
    }
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None    

def get_thousandeyes_label_details(labelId):
    url = "https://api.thousandeyes.com/v6/groups/"+str(labelId)
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


def get_thousandeyes_test_configuration():
    headers = {
        'Authorization': "Bearer "+API_TOKEN,
        'Accept': 'application/json'
    }
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def get_thousandeyes_test_agents(url):
    #print(url)
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

def get_thousandeyes_accountgroup():
    headers = {
        'Authorization': "Bearer "+API_TOKEN,
        'Accept': 'application/json'
    }
    response = requests.get("https://api.thousandeyes.com/v7/account-groups", headers=headers)
    if response.status_code == 200:
        resp = response.json()
        return resp["accountGroups"][0]["organizationName"]
    else:
        print(f"Error: {response.status_code}")
        return None

def get_thousandeyes_usage():
    headers = {
        'Authorization': "Bearer "+API_TOKEN,
        'Accept': 'application/json'
    }
    response = requests.get("https://api.thousandeyes.com/v7/usage", headers=headers)
    if response.status_code == 200:
        resp = response.json()
        teUnitsIncluded = str(resp["usage"]["quota"]["cloudUnitsIncluded"])
        teCloudUnitsProjected = str(resp["usage"]["cloudUnitsProjected"])
        teEntUnitsProjected = str(resp["usage"]["enterpriseUnitsProjected"])


        return f"cloud([Cloud Units<br>{teCloudUnitsProjected}]) -..- total((Total Units<br>{teUnitsIncluded})) -..- ent([Enterprise Units<br>{teEntUnitsProjected}])"
    else:
        print(f"Error: {response.status_code}")
        return None

def test_destination(test):
    if test["type"] == "agent-to-server":
        return test["server"]

    if test["type"] == "agent-to-agent":
        return "Agent-to-Agent"

    
    if test["type"] == "dns-server":
        test["domain"] = test["domain"].split(" ")
        return test["domain"][0]

    if test["type"] == "http-server" or test["type"] == "page-load" :
        return test["url"]

    return "server"

def generate_mermaid_diagram(test_config, label):
    mermaid_lines = ["---", "title: "+label["name"],"config:","  theme: base","  themeVariables:","    primaryColor: '#00ff00'", "---"]
    mermaid_lines.append("flowchart LR")

    labelDetails = get_thousandeyes_label_details(label["groupId"])
    #print(labelDetails["groups"]["tests"])

    for test in labelDetails["groups"][0]["tests"]:
#        if test["type"] == "dns-server":
            test_id = test['testId']
            test_name = test['testName']
#            mermaid_lines.append(f"{test_id}({test_name}\nType: {test['type']}) --> {test_destination(test)}")
#            mermaid_lines.append(f"{test_id}({test_name}) -..-> {test_destination(test)}")
            mermaid_lines.append(f"{test_id}({test_name}<br>Target: {test_destination(test)})")

            test_agents = get_thousandeyes_test_agents(test['apiLinks'][0]['href'])


            for agent in test_agents["test"][0]["agents"]:
                #print("Agents")
                #for agent in test['agents']:
                agent_id = agent['agentId']
                agent_name = agent['agentName']
                mermaid_lines.append(f'{agent_id}(["{agent_name}"]):::teAgent --> {test_id}')
        
            if test["type"] == "dns-server":
                test_dnsServers = get_thousandeyes_test_agents(test['apiLinks'][0]['href'])
                for dnsServer in test_dnsServers["test"][0]["dnsServers"]:
                    dnsServer_id = dnsServer['serverId']
                    dnsServer_name = dnsServer['serverName']
                    mermaid_lines.append(f"{test_id} --> {dnsServer_id}([{dnsServer_name}])")

#    mermaid_lines.append(get_thousandeyes_usage())
    mermaid_lines.append("classDef teAgent fill:#f96")

            
    
    return "\n".join(mermaid_lines)

# Step 1: Retrieve the ThousandEyes Test Configuration
test_config = get_thousandeyes_test_configuration()
labels = get_thousandeyes_labels()
if labels:
    for label in labels["groups"]:
        if label["type"] == "tests" and label["builtin"] == 0:
#            print(label["groupId"]) 
#            print(label["name"])
            print(f'\n##### Label: {label["name"]} - START #####')
            mermaid_diagram = generate_mermaid_diagram(test_config, label)

            print(mermaid_diagram)

            print(f'##### Label: {label["name"]} - END #####')



    with open('labels.json', 'w') as f:
        json.dump(labels, f, indent=4)
#    print("Test configuration saved to test_config.json")

    # Step 2: Generate the Mermaid Diagram
#    mermaid_diagram = generate_mermaid_diagram(test_config)
    
    # Step 3: Output the Diagram
#    print(mermaid_diagram)
#    with open('mermaid_diagram.md', 'w') as f:
#        f.write(mermaid_diagram)

#    print("Mermaid diagram saved to mermaid_diagram.md")
else:
    print("Failed to retrieve test configuration")
