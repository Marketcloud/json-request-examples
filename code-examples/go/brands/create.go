package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "http://api.marketcloud.it/v0/brands"

	payload := strings.NewReader("{\"name\" : \"Paulaner\",\"description\" : \"Paulaner is a German brewery established in 1634 in Munich.\",\"image_url\" : \"http://media.marketcloud.it/v0/\",\"url\" : \"Paulaner-Beer\"}")

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