package helper

import (
	"fmt"
	"net/http"
	"io/ioutil"
	"bytes"
	"encoding/json"
)

func Test(){
	fmt.Println("Helper - Test")
}

func POSTrequest (url string, headers string,payload map[string]string) string {
	PostPayload, _ := json.Marshal(payload)

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(PostPayload))
    if err != nil {
        fmt.Println("Error creating request:", err)        
    }

    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error making request:", err)        
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)        
    }

	return string(body)
}

func GETrequest (url string, payload map[string]string) string{
	//fmt.Println(payload)

	client := &http.Client{}
	req, err := http.NewRequest("GET", url, nil)

	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("Authorization", "Bearer "+payload["Token"])

	resp, err := client.Do(req)

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)        
    }
	
	return string(body)
}