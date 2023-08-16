create an IAM role and assign lambda service two roles - AmazonEC2FullAccess and AWSLambdaBasicExecutionRole
create a lambda function with this role and use the terminate-ec2.py script to terminate the ec2 instance. 
create a EventBridge rule to trigger the above lambda on the "EC2 Instance state change event".
Verify by starting a ec2 intance and then it will be automatically terminated.
