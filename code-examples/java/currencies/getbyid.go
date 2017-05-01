package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "http://api.marketcloud.it/v0/currencies/9"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("authorization", "YourPublicKey:YourToken")
	req.Header.Add("accept", "application/json")
	req.Header.Add("content-type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}