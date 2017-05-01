package main

import (
	"fmt"
	"strings"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "http://api.marketcloud.it/v0/products"

	payload := strings.NewReader("{\"name\" : \"Hefe-Weissbier\",\"sku\":\"F310R90G8BCPJ1AT\",\"category_id\":\"12\",\"brand_id\":\"19\",\"tax_id\":\"23\",\"store_id\":\"25\",\"description\" : \"The no. 1 Hefe-Weißbier in Germany and one of the world’s favourites.\",\"price\" : \"1.50\",\"stock_level\" : \"1256\",\"published\":\"true\"}")

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