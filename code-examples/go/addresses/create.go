package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "http://api.marketcloud.it/v0/addresses"

	payload := strings.NewReader("{\"email\": \"john@thewall.io\",\"full_name\": \"Jon Snow\",\"country\" : \"Westeros\", \"state\": \"The North\", \"city\": \"Winterfell\", \"address1\": \"Winterfell Castle, 1\", \"postal_code\": \"12345\"}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("authorization", "YourPublicKey:YourToken")
	req.Header.Add("accept", "application/json")
	req.Header.Add("content-type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}