{
    "method": "POST",
    "url": "http://api.marketcloud.it/v0/products/:id/variants",
    "httpVersion": "HTTP/1.1",
    "headers": [
        { "name": "Authorization", "value": "YourPublicKey:YourToken" },
        { "name": "Accept", "value": "application/json" },
        { "name": "Content-Type", "value": "application/json" }
    ],
    "postData" : {
        "text" : "[{ \"price\":13.5, \"name\":\"Scala tshirt\", \"description\":\"Tshirt\", \"stock_type\":\"infinite\", \"color\":\"black\", \"size\":\"xl\", \"id\":1}]"
    },
    "headersSize" : 150,
    "bodySize" : 150
}

