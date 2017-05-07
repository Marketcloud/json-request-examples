import Foundation

let headers = [
  "authorization": "YourPublicKey:YourToken",
  "accept": "application/json",
  "content-type": "application/json"
]

let postData = NSData(data: "{"cost_type" : "fixed_fee", "fixed_fee" : 5}".dataUsingEncoding(NSUTF8StringEncoding)!)

var request = NSMutableURLRequest(URL: NSURL(string: "http://api.marketcloud.it/v0/brands/3")!,
                                        cachePolicy: .UseProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.HTTPMethod = "PUT"
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