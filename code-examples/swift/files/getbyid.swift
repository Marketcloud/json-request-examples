import Foundation

let headers = [
  "authorization": "YourPublicKey:YourToken",
  "accept": "application/json",
  "content-type": "application/json"
]

var request = NSMutableURLRequest(URL: NSURL(string: "http://api.marketcloud.it/v0/files/9")!,
                                        cachePolicy: .UseProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.HTTPMethod = "GET"
request.allHTTPHeaderFields = headers

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