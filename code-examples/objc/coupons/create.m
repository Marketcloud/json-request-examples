#import <Foundation/Foundation.h>

NSDictionary *headers = @{ @"authorization": @"YourPublicKey:YourToken",
                           @"accept": @"application/json",
                           @"content-type": @"application/json" };

NSData *postData = [[NSData alloc] initWithData:[@"{    "code" : "WELCOME2017",    "name" : "welcome_2017",    "type" : "total",    "target_type" : "CART_COUPON",    "discount_type" : "NET_REDUCTION",    "discount_value" : 10,    "active" : true}" dataUsingEncoding:NSUTF8StringEncoding]];

NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:@"http://api.marketcloud.it/v0/coupons"]
                                                       cachePolicy:NSURLRequestUseProtocolCachePolicy
                                                   timeoutInterval:10.0];
[request setHTTPMethod:@"POST"];
[request setAllHTTPHeaderFields:headers];
[request setHTTPBody:postData];

NSURLSession *session = [NSURLSession sharedSession];
NSURLSessionDataTask *dataTask = [session dataTaskWithRequest:request
                                            completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
                                                if (error) {
                                                    NSLog(@"%@", error);
                                                } else {
                                                    NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *) response;
                                                    NSLog(@"%@", httpResponse);
                                                }
                                            }];
[dataTask resume];