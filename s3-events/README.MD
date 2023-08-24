Steps:

1. Create an IAM role by using cloud shell. Execute the "lambda-role.sh" script in cloudshell and it will create a role with this name - "LambdaS3AndCloudWatchRole"
wget https://github.com/gaurav157243/aws-projects/raw/main/s3-events/lambda-role.sh

If you want to wget the script file then Right Click on the RAW button and get the url and use the same with the wget command

2. Create a lambda function with the above role and use the python script present in the folder. Deploy the lambda.

3. Create a S3 bucket, then Properties tab -> Event notifications -> Create Event Notificaiton and configure the lambda with this event. 


