Steps:

1. Create a S3 bucket

2. Create a SNS topic
2a. Edit the topic and modify the access policy, make the appropriate changes and save it with the topic.
2b. Modify the SNS-topic-ARAN, bucketname and the source account it

{
    "Version": "2012-10-17",
    "Id": "example-ID",
    "Statement": [
        {
            "Sid": "Example SNS topic policy",
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": [
                "SNS:Publish"
            ],
            "Resource": "SNS-topic-ARN",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:*:*:bucket-name"
                },
                "StringEquals": {
                    "aws:SourceAccount": "bucket-owner-account-id"
                }
            }
        }
    ]
}                  

3. Create a SQS queue

4. Upload a new file in a s3 bucket and check that there is a new message in the sqs queue


