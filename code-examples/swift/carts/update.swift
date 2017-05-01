import Foundation

let headers = [
  "authorization": "YourPublicKey:YourToken",
  "accept": "application/json",
  "content-type": "application/json"
]

let postData = NSData(data: "{"user_id" : 1,"items" : [{"product_id":13,"quantity":2},{"product_id":15,"quantity":8}]}".dataUsingEncoding(NSUTF8StringEncoding)!)

var request = NSMutableURLRequest(URL: NSURL(string: "http://api.marketcloud.it/v0/carts/9")!,
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