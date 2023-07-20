import json
import boto3
import os
from botocore.exceptions import ClientError

# Initialize AWS clients
sqs = boto3.client('sqs')
ses = boto3.client('ses')

def send_email(sender_email, recipient_email, subject, body):
    try:
        response = ses.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [recipient_email]
            },
            Message={
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': body
                    }
                }
            }
        )
        print(f"Email sent! Message ID: {response['MessageId']}")
    except ClientError as e:
        print(f"Error sending email: {e.response['Error']['Message']}")
        

def lambda_handler(event, context):
    sender_email = "gaurav157243@gmail.com"
    recipient_email = "shruti.srs@gmail.com"
    subject = "lambda sqs testing email"
    
    for record in event['Records']:
        print("test")
        email_body = record["body"]
        print(str(email_body))
        send_email(sender_email, recipient_email, subject, email_body)
