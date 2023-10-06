import boto3

def lambda_handler(event, context):
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Get all running instances
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            
            # Check if the 'shutdown' tag exists and is set to 'false'
            shutdown_tag = False
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'shutdown' and tag['Value'].lower() == 'false':
                    shutdown_tag = True
                    break
            
            # If the 'shutdown' tag is 'false', skip this instance
            if shutdown_tag:
                print(f"Instance {instance_id} is tagged to not shutdown.")
            else:
                # Stop the instance
                ec2.stop_instances(InstanceIds=[instance_id])
                print(f"Stopping instance {instance_id}")
    
    return {
        'statusCode': 200,
        'body': 'EC2 instances stopped based on the "shutdown" tag.'
    }
