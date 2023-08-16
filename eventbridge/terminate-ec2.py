import boto3
import json

def lambda_handler(event, context):
    
    print("event: " + json.dumps(event))
    # Extract instance details from the EventBridge event
    instance_id = event['detail']['instance-id']
    print("instance id: " + instance_id)

    ec2_client = boto3.client('ec2')
    print(f"Terminating instance with id: {instance_id}")
    ec2_client.terminate_instances(InstanceIds=[instance_id])
