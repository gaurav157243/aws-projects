# Create an IAM role for Lambda with S3 and CloudWatch Logs permissions
aws iam create-role \
  --role-name LambdaS3AndCloudWatchRole \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  }'

# Attach the policy for S3 full access to the role
aws iam attach-role-policy \
  --role-name LambdaS3AndCloudWatchRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

# Attach the policy for CloudWatch Logs permissions to the role
aws iam attach-role-policy \
  --role-name LambdaS3AndCloudWatchRole \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
