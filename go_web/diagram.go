package main

import (
    "fmt"
 //   "net/http"
	"teDOTweb/helper"
	"encoding/json"
	"strings"
)

type TETestDetail struct {
	Interval        int       `json:"interval"`
	TestID          string    `json:"testId"`
	BgpMeasurements bool      `json:"bgpMeasurements"`
	UsePublicBgp    bool      `json:"usePublicBgp"`
	Description     string    `json:"description"`
	LiveShare       bool      `json:"liveShare"`
	TestName        string    `json:"testName"`
	CreatedBy       string    `json:"createdBy"`
//	CreatedDate     time.Time `json:"createdDate"`
	ModifiedBy      string    `json:"modifiedBy"`
//	ModifiedDate    time.Time `json:"modifiedDate"`
	SavedEvent      bool      `json:"savedEvent"`
	Type            string    `json:"type"`
	AlertsEnabled   bool      `json:"alertsEnabled"`
	Enabled         bool      `json:"enabled"`
	Agents          []struct {
		Prefix            string   `json:"prefix"`
		IPAddresses       []string `json:"ipAddresses"`
		PublicIPAddresses []string `json:"publicIpAddresses"`
		Network           string   `json:"network"`
		AgentID           string   `json:"agentId"`
		AgentName         string   `json:"agentName"`
		AgentType         string   `json:"agentType"`
		CountryID         string   `json:"countryId"`
		Location          string   `json:"location"`
	} `json:"agents"`
	BandwidthMeasurements bool   `json:"bandwidthMeasurements"`
	ContinuousMode        bool   `json:"continuousMode"`
	DscpID                string `json:"dscpId"`
	Ipv6Policy            string `json:"ipv6Policy"`
	MtuMeasurements       bool   `json:"mtuMeasurements"`
	NumPathTraces         int    `json:"numPathTraces"`
	PathTraceMode         string `json:"pathTraceMode"`
	ProbeMode             string `json:"probeMode"`
	NetworkMeasurements   bool   `json:"networkMeasurements"`
	Protocol              string `json:"protocol"`
	RandomizedStartTime   bool   `json:"randomizedStartTime"`
	Server                string `json:"server"`
	Dscp                  string `json:"dscp"`
	Links                 struct {
		Self struct {
			Href string `json:"href"`
		} `json:"self"`
		TestResults []struct {
			Href string `json:"href"`
		} `json:"testResults"`
	} `json:"_links"`
}

type TELabels struct {
	Tags []struct {
		ID          string    `json:"id"`
		Aid         int64     `json:"aid"`
		ObjectType  string    `json:"objectType"`
		Key         string    `json:"key"`
		Value       string    `json:"value"`
		Color       string    `json:"color"`
		Icon        string    `json:"icon"`
		Description any       `json:"description"`
		AccessType  string    `json:"accessType"`
		LegacyID    int64     `json:"legacyId"`
		Assignments []struct {
			ID   string `json:"id"`
			Type string `json:"type"`
		} `json:"assignments"`
	} `json:"tags"`
}

type ALLDiagrams struct {
    Label []struct {
        LabelID     string
        Diagram     string
    }
}

type TEAllTests struct {
	Tests []struct {
		Interval              int       `json:"interval"`
		TestID                string    `json:"testId"`
		BgpMeasurements       bool      `json:"bgpMeasurements"`
		UsePublicBgp          bool      `json:"usePublicBgp"`
		Description           string    `json:"description"`
		LiveShare             bool      `json:"liveShare"`
		TestName              string    `json:"testName"`
		CreatedBy             string    `json:"createdBy"`
//		CreatedDate           time.Time `json:"createdDate"`
		ModifiedBy            string    `json:"modifiedBy"`
//		ModifiedDate          time.Time `json:"modifiedDate"`
		SavedEvent            bool      `json:"savedEvent"`
		Type                  string    `json:"type"`
		AlertsEnabled         bool      `json:"alertsEnabled"`
		Enabled               bool      `json:"enabled"`
		BandwidthMeasurements bool      `json:"bandwidthMeasurements"`
		ContinuousMode        bool      `json:"continuousMode"`
		DscpID                string    `json:"dscpId"`
		Ipv6Policy            string    `json:"ipv6Policy"`
		MtuMeasurements       bool      `json:"mtuMeasurements"`
		NumPathTraces         int       `json:"numPathTraces"`
		PathTraceMode         string    `json:"pathTraceMode"`
		ProbeMode             string    `json:"probeMode"`
		NetworkMeasurements   bool      `json:"networkMeasurements"`
		Protocol              string    `json:"protocol"`
		RandomizedStartTime   bool      `json:"randomizedStartTime"`
		Server                string    `json:"server"`
		Dscp                  string    `json:"dscp"`
		Links                 struct {
			Self struct {
				Href string `json:"href"`
			} `json:"self"`
			TestResults []struct {
				Href string `json:"href"`
			} `json:"testResults"`
		} `json:"_links"`
	} `json:"tests"`
}

func getLabels (teAGT string) TELabels {
    fmt.Println("Getting ALL Tags/Labels...")
	//teAGT = "01ab-cf1d5e79-16d3-4293-8235-5e196aeac6c1"
	getData := map[string]string{
		"Token": teAGT,
	}

	// Getting TE Labels 
	url := fmt.Sprintf("https://api.thousandeyes.com/v7/tags?expand=assignments")
	response := helper.GETrequest(url,getData)
	//fmt.Println(response)
	var teLabels TELabels
	lines := []string{}
	
	json.Unmarshal([]byte(response), &teLabels)
	for _, label := range teLabels.Tags {
		lines = append(lines, label.Value)
	}
	//return lines
	return teLabels
}

func getAllTests(teAGT string) TEAllTests{
    fmt.Println("Getting ALL Tests...")

    getData := map[string]string{
		"Token": teAGT,
	}

	// Getting TE Tests 
	url := fmt.Sprintf("https://api.thousandeyes.com/v7/tests")
	response := helper.GETrequest(url,getData)
    //fmt.Println(response)
    var teAllTests TEAllTests
    json.Unmarshal([]byte(response), &teAllTests)
//    for _, test := range teAllTests.Tests {
//		fmt.Println("  Test Name: "+test.TestName)
//		fmt.Println("  Test ID: "+test.TestID)
//	}
    return teAllTests
}

func getTestDetails(testURL string, teAGT string) TETestDetail {
    fmt.Println("Getting Test Details...")

    getData := map[string]string{
		"Token": teAGT,
	}

	// Getting TE Tests 
	url := fmt.Sprintf(testURL+"?expand=agent")
	response := helper.GETrequest(url,getData)
    //fmt.Println(response)
    var teTestDetail TETestDetail
    json.Unmarshal([]byte(response), &teTestDetail)

//    for _, agent := range teTestDetail.Agents {
//		fmt.Println("  Agent Name: "+agent.AgentName)
//		fmt.Println("  Agent ID: "+agent.AgentID)
//	}

    return teTestDetail
}

func createDiagrams(teLabels TELabels, teAGT string) {
    fmt.Println("Creating Diagrams...")
    var allDiagrams ALLDiagrams

	//fmt.Println(teLabels)
    teAllTests := getAllTests(teAGT)

	for _, label := range teLabels.Tags {
        //fmt.Println("Label: "+label.Value)

        lines := []string{}
	    lines = append(lines, "---")
	    lines = append(lines, "title: "+label.Value)
	    lines = append(lines, "config:")
	    lines = append(lines, "  look: handDrawn")
	    lines = append(lines, "---")
	    lines = append(lines, "graph LR")
        
		for _, assignedTest := range label.Assignments {
			//fmt.Printf("Tests ID: %s\n", test.ID)

            for _, test := range teAllTests.Tests{
                if(test.TestID == assignedTest.ID){
                    //fmt.Printf("  Tests Self: %s\n", test.Links.Self.Href)

                    // Define the Tests
                    lines = append(lines, "test_"+test.TestID+"("+test.TestName+")")

                    teTestDetail := getTestDetails(test.Links.Self.Href, teAGT)

                    // Define the Agents
                    mermaidAgent := ""

                    for _, agent := range teTestDetail.Agents {
                        if(agent.AgentType == "cloud"){
                            mermaidAgent = fmt.Sprintf("agent_%s([\"%s<br>%s\"])",agent.AgentID, agent.AgentName, agent.AgentType )
                        }

                        if(agent.AgentType == "enterprise"){
                            mermaidAgent = fmt.Sprintf("agent_%s([\"%s<br>%s<br>%s\"])",agent.AgentID, agent.AgentName, agent.IPAddresses[0], agent.AgentType )
                        }
                        lines = append(lines, mermaidAgent)
                    }

                    // Connecting Agents to Tests
                    for _, agent := range teTestDetail.Agents {
                        lines = append(lines, "agent_"+agent.AgentID+" --> test_"+test.TestID)
                    }
                }
            }	        
		}

        diagram := strings.Join(lines, "\n")
        fmt.Println("#-----------#")
        //fmt.Println(diagram)

        allDiagrams.Label = append(allDiagrams.Label, struct {
            LabelID string
            Diagram string
        }{
            LabelID: label.ID,
            Diagram: diagram,
        })


	}
    fmt.Println(allDiagrams.Label[0].Diagram)
}

func main() {
    // Start server
    fmt.Println("Diagram Test")

    userInput := "01ab-cf1d5e79-16d3-4293-8235-5e196aeac6c1"
    teLabels := getLabels(userInput)
    createDiagrams(teLabels, userInput)
}