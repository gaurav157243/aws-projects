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
    
    # # Check if the instance type is part of the free tier
    # is_free_tier = is_instance_type_free_tier(instance_type)
    
    # if not is_free_tier:
    #     # Terminate the instance
    #     print(f"Terminated instance {instance_id} due to non-free tier instance type: {instance_type}")
        
    #     ec2_client.terminate_instances(InstanceIds=[instance_id])
    #     print(f"Terminated instance {instance_id} due to non-free tier instance type: {instance_type}")
    # else:
    #     print(f"Instance {instance_id} has a free tier instance type: {instance_type}")

def is_instance_type_free_tier(instance_type):
    # List of instance types that are part of the AWS Free Tier
    free_tier_instance_types = [
        't2.micro', 't2.small', 't2.medium',
        't3.micro', 't3.small', 't3.medium',
        't3a.micro', 't3a.small', 't3a.medium'
        # Add more instance types as needed
    ]
    
    return instance_type in free_tier_instance_types
