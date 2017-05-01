package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "http://api.marketcloud.it/v0/orders"

	payload := strings.NewReader("{\"state\" : \"Processing\",\"total\" : 99.99, \"display_total\" : \"$ 99.99\", \"items_total\" : 89.99, \"dispaly_item_total\" : \"$ 89.99\", \"shipping_address_id\" : 124, \"billing_address_id\" : 123}")

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