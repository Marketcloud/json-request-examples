import Foundation

let headers = [
  "accept": "application/json",
  "content-type": "application/json",
  "authorization": "YourPublicKey:YourToken"
]

var request = NSMutableURLRequest(URL: NSURL(string: "http://api.marketcloud.it/v0/taxes/9")!,
                                        cachePolicy: .UseProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.HTTPMethod = "DELETE"
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