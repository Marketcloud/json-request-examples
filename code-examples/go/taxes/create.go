package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "http://api.marketcloud.it/v0/taxes"

	payload := strings.NewReader("{ \"rates\" : [  { \"state\" : \"*\", \"postcode\" : \"*\", \"city\" : \"*\", \"priority\" : 0, \"country\" : \"Italy\", \"rate\" : 22, \"name\" : \"IVA\", \"shipping\" : true, \"country_code\" : \"IT\" } ], \"name\" : \"Standard VAT\", \"application_id\" : 4323, \"id\" : 169405 }")

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