import Foundation

let headers = [
  "authorization": "YourPublicKey:YourToken",
  "accept": "application/json",
  "content-type": "application/json"
]

let postData = NSData(data: "{"name" : "ExpressCouriers Inc","price" : "€ 5.00","min_price" : 10.00, "max_weight" : 30.00 }".dataUsingEncoding(NSUTF8StringEncoding)!)

var request = NSMutableURLRequest(URL: NSURL(string: "http://api.marketcloud.it/v0/shippings")!,
                                        cachePolicy: .UseProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.HTTPMethod = "POST"
request.allHTTPHeaderFields = headers
request.HTTPBody = postData

let session = NSURLSession.sharedSession()
let dataTask = session.dataTaskWithRequest(request, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    println(error)
  } else {
    let httpResponse = response as? NSHTTPURLResponse
    println(httpResponse)
  }
})

dataTask.resume()