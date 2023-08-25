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
            "Resource": "arn:aws:sns:us-east-1:665178635794:s3eventtopic",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:::test12345677dfsfd"
                },
                "StringEquals": {
                    "aws:SourceAccount": "665178635794"
                }
            }
        }
    ]
}                  

3. Create a SQS queue and edit the access policy and modfiy the topic arn and the queue arn

{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:us-east-1:665178635794:s3testqueue",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:sns:us-east-1:665178635794:s3eventtopic"
        }
      }
    }
  ]
}

4. Add a subcription between the topic and the sqs queue.


5. Upload a new file in a s3 bucket and check that there is a new message in the sqs queue


