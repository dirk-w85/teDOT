package main

import (
    "fmt"
    "html/template"    
	"log/slog"
    "net/http"
	"teDOTweb/helper"
	"encoding/json"
	"strings"
	"os"
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


type ALLDiagrams struct {
    Tags []struct {
        LabelID     string
        Diagram     string
    }
}

type TEAllAccountGroups struct {
	AccountGroups []struct {
		AccountGroupName      string `json:"accountGroupName"`
		Aid                   string `json:"aid"`
	} `json:"accountGroups"`
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
		URL                  string    `json:"url"`
		DNSServers		[]struct {
			ServerID		  string 	`json:"serverid"`
			ServerName		  string 	`json:"serverName"`
		} `json:"dnsServers"`
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

func getLabels (teAGT string, teAID string) TELabels {
    slog.Debug("Getting ALL Tags/Labels...")
	slog.Debug("Selected AID: "+teAID)
	//teAGT = "01ab-cf1d5e79-16d3-4293-8235-5e196aeac6c1"
	getData := map[string]string{
		"Token": teAGT,
	}
	// Getting TE Labels 
	url := fmt.Sprintf("https://api.thousandeyes.com/v7/tags?expand=assignments&aid="+teAID)
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

func getAccountGroups (token string) string {
    slog.Debug("Getting ALL Account-Groups...")
	getData := map[string]string{
		"Token": token,
	}
	// Getting TE Labels 
	url := fmt.Sprintf("https://api.thousandeyes.com/v7/account-groups")
	response := helper.GETrequest(url,getData)
	//fmt.Println(response)
	var teAGs TEAllAccountGroups
	json.Unmarshal([]byte(response), &teAGs)
	return response
}

func getAllTests(teAGT string, teAID string) TEAllTests{
    slog.Debug("Getting ALL Tests...")

    getData := map[string]string{
		"Token": teAGT,
	}

	// Getting all TE Tests 
	url := fmt.Sprintf("https://api.thousandeyes.com/v7/tests?aid="+teAID)
	response := helper.GETrequest(url,getData)
    //fmt.Println(response)
    var teAllTests TEAllTests
    json.Unmarshal([]byte(response), &teAllTests)

	slog.Debug("Received ALL Tests...")
    return teAllTests
}

func getTestDetails(testURL string, teAGT string) TETestDetail {
   //fmt.Println("Getting Test Details...")
   //slog.Debug(teAID)

    getData := map[string]string{
		"Token": teAGT,
	}

	// Getting TE Tests Details 
	url := fmt.Sprintf(testURL+"?expand=agent")
	response := helper.GETrequest(url,getData)
    //fmt.Println(response)
    var teTestDetail TETestDetail
    json.Unmarshal([]byte(response), &teTestDetail)

    return teTestDetail
}

func createDiagrams(teLabels TELabels, teAGT string, mermaidLook string, meramidDirection string, graphBrandColors string, teAID string) ALLDiagrams {
    slog.Debug("Creating Diagrams...")
    var allDiagrams ALLDiagrams

    teAllTests := getAllTests(teAGT, teAID)

	for _, label := range teLabels.Tags {
        //fmt.Println("Label: "+label.Value)

        lines := []string{}
	    lines = append(lines, "---")
//	    lines = append(lines, "title: "+label.Value)
	    lines = append(lines, "config:")
	    lines = append(lines, "  look: "+mermaidLook)		
//	    lines = append(lines, "  htmlLabels: false")
	    lines = append(lines, "---")
	    lines = append(lines, "graph "+meramidDirection)
		if(graphBrandColors == "thousandeyes"){
			lines = append(lines, "classDef teAgent fill:#FB7C32,color:#fff,stroke:#FB7C32")
        	lines = append(lines, "classDef teTest fill:#0d274d,color:#fff,stroke:#0d274d")
        	lines = append(lines, "classDef teTarget fill:#dddddd,color:#0d274d,stroke:#0d274d")
		}
		if(graphBrandColors == "cisco2025"){
			lines = append(lines, "classDef teAgent fill:#FF9000,color:#fff,stroke:#FF9000")
        	lines = append(lines, "classDef teTest fill:#02C8FF,color:#07182D,stroke:#02C8FF")
        	lines = append(lines, "classDef teTarget fill:#0A60FF,color:#fff,stroke:#0A60FF")
		}

        
		for _, assignedTest := range label.Assignments {
			//fmt.Printf("Tests ID: %s\n", test.ID)

            for _, test := range teAllTests.Tests{
                if(test.TestID == assignedTest.ID){
                    //fmt.Printf("  Tests Self: %s\n", test.Links.Self.Href)

                    // Define the Tests
					mermaidTest := ""
					mermaidTest = fmt.Sprintf("test_%s[\"**%s**<br>*Type: %s<br>Interval: %ds*\"]:::teTest", test.TestID, test.TestName, test.Type, test.Interval )
					lines = append(lines, mermaidTest)

                    teTestDetail := getTestDetails(test.Links.Self.Href, teAGT)

                    // Define the Agents
                    mermaidAgent := ""

                    for _, agent := range teTestDetail.Agents {
                        if(agent.AgentType == "cloud"){
                            mermaidAgent = fmt.Sprintf("agent_%s([\"%s<br>*%s*\"]):::teAgent",agent.AgentID, agent.AgentName, agent.AgentType )
                        }

                        if(agent.AgentType == "enterprise"){
                            mermaidAgent = fmt.Sprintf("agent_%s([\"%s<br>*%s<br>%s*\"]):::teAgent",agent.AgentID, agent.AgentName, agent.IPAddresses[0], agent.AgentType )
                        }
                        lines = append(lines, mermaidAgent)
                    }

                    // Connecting Agents to Tests
                    for _, agent := range teTestDetail.Agents {
                        lines = append(lines, "agent_"+agent.AgentID+" --> test_"+test.TestID)
                    }


					// Connecting Tests to Test-Targets

					mermaidTestTarget := "test_"+test.TestID+" -- tcp/1234 --> target_dummy>Test-Type not yet supported]:::teTarget"

					if(test.Type == "agent-to-server"){
						mermaidTestTarget = fmt.Sprintf("test_%s -- %s --> srv_%s[\"%s\"]:::teTarget", test.TestID, test.Protocol, test.TestID, test.Server)
					}

					if(test.Type == "http-server"){
						mermaidTestTarget = fmt.Sprintf("test_%s -- %s<br>Trace: %s --> srv_%s[\"<p>%s</p>\"]:::teTarget", test.TestID, test.Protocol, test.PathTraceMode, test.TestID, test.URL)
					}

					if(test.Type == "dns-server"){
						for _, dnsServer := range test.DNSServers {
							mermaidTestTarget = fmt.Sprintf("test_%s -- Trace: %s --> srv_%s_%s[\"<p>%s</p>\"]:::teTarget", test.TestID, test.PathTraceMode, test.TestID, dnsServer.ServerID, dnsServer.ServerName)
							lines = append(lines, mermaidTestTarget)
						}
						mermaidTestTarget = ""
					}

					lines = append(lines, mermaidTestTarget)

					

                }
            }	        
		}

        diagram := strings.Join(lines, "\n")

        allDiagrams.Tags = append(allDiagrams.Tags, struct {
            LabelID string
            Diagram string
        }{
            LabelID: label.ID,
            Diagram: diagram,
        })
	}
	slog.Debug("Diagrams created.")
	return allDiagrams
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
    //tmpl, err := template.New("form").ParseFiles("formTemplate.html")
	tmpl, err := template.ParseFiles("formTemplate.html")
    if err != nil {
        http.Error(w, "Error parsing template", http.StatusInternalServerError)
        return
    }
    
    err = tmpl.Execute(w, nil)
    if err != nil {
        http.Error(w, "Error executing template", http.StatusInternalServerError)
        return
    }
	slog.Debug("Form Page Template executed.")
}

func submitHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method != "POST" {
        http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        return
    }
    
    // Parse form data
    err := r.ParseForm()
    if err != nil {
        http.Error(w, "Error parsing form", http.StatusBadRequest)
        return
    }
    
    // Get the input value
    userInput := r.FormValue("userInput")
	graphlook := r.FormValue("radioDefault")
	graphDirection := r.FormValue("radioDirection")
	graphBrandColors := r.FormValue("radioBrandColors")
	userAID := r.FormValue("ag")
    
    // Log the input on server side
    slog.Debug("User submitted: %s\n", userInput)
    slog.Debug("Graph Look: %s\n", graphlook)
    slog.Debug("Graph Direction: %s\n", graphDirection)
    slog.Debug("Graph Brand: %s\n", graphBrandColors)
    
    // Display result page
    //tmpl, err := template.New("result").ParseFiles("resultTemplate.html")


	teLabels := getLabels(userInput, userAID)
	allDiagrams := createDiagrams(teLabels, userInput, graphlook, graphDirection, graphBrandColors, userAID)

	tmpl, err := template.ParseFiles("resultTemplate.html")
    if err != nil {
        http.Error(w, "Error parsing template", http.StatusInternalServerError)
        return
    }
	//fmt.Println(allDiagrams)

	data := struct {
		UserInput string
		UserAID string
		Diagrams ALLDiagrams
		Labels TELabels
	}{
		UserInput: userInput,
		UserAID: userAID,
		Diagrams: allDiagrams,
		Labels: teLabels,
	}
    err = tmpl.Execute(w, data)
    if err != nil {
        http.Error(w, "Error executing result template", http.StatusInternalServerError)
        return
    }

	slog.Debug("Result Page Template executed.")
}

func apiAccountGroupHandler(w http.ResponseWriter, r *http.Request) {
    //tmpl, err := template.New("form").ParseFiles("formTemplate.html")

	if r.Method != "GET" {
        http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        return
    }
    
    // Parse form data
    err := r.ParseForm()
    if err != nil {
        http.Error(w, "Error parsing form", http.StatusBadRequest)
        return
    }
    
    // Get the input value
    //userInput := r.FormValue("userInput")
	userInput := r.FormValue("token")

	//userInput := "91bbe972-f931-446a-97e4-016797e5293a"
    slog.Debug("API // AccountGroup Handler")
	slog.Debug("Using Bearer", userInput)

	response := getAccountGroups(userInput)

	fmt.Fprintf(w, response)
}

func testHandler(w http.ResponseWriter, r *http.Request) {
    //tmpl, err := template.New("form").ParseFiles("formTemplate.html")
	userInput := "01ab-cf1d5e79-16d3-4293-8235-5e196aeac6c1"
	teAID := "0"
    slog.Debug("Test Handler")
	slog.Debug("Using Bearer", userInput)

	teLabels := getLabels(userInput, teAID)
	allDiagrams := createDiagrams(teLabels, userInput, "classic", "LR", "thousandeyes", teAID)

	tmpl, err := template.ParseFiles("testTemplate.html")
    if err != nil {
        http.Error(w, "Error parsing template", http.StatusInternalServerError)
        return
    }
	//fmt.Println(allDiagrams)

	data := struct {
		UserInput string
		Diagrams ALLDiagrams
		Labels TELabels
	}{
		UserInput: userInput,
		Diagrams: allDiagrams,
		Labels: teLabels,
	}
    err = tmpl.Execute(w, data)
    if err != nil {
        http.Error(w, "Error executing result template", http.StatusInternalServerError)
        return
    }
}

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stderr,nil))
	logger = slog.New(slog.NewJSONHandler(os.Stderr,&slog.HandlerOptions{Level: slog.LevelDebug}))
	slog.SetDefault(logger)
	slog.Debug("Application started - Verion: 0.2025.06.23.00")
    // Register handlers
    http.HandleFunc("/", homeHandler)
    http.HandleFunc("/submit", submitHandler)
    http.HandleFunc("/test", testHandler)
    http.HandleFunc("/api/accountgroups", apiAccountGroupHandler)
    
    slog.Debug("Server starting on :8090")
    slog.Debug("Press Ctrl+C to stop the server")
    
    // Start server
    http.ListenAndServe(":8090", nil)
}
