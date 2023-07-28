#!/bin/bash

## This script will be executed from the AWS CloudShell Terminal
## When using cloudshell, you dont need to configure the AWS account credentials
## and you can easily perform CLI operation in your account

## usage: create-x-servers.sh <numberOfServersToCreate>
## eg. create-x-servers.sh 2 

## the above command will create 2 servers; wait for them to come in running state and
## then automatically terminate the same.

# Prompt for the number of instances to create
read -p "Enter the number of EC2 instances to create (max 100): " NUM_INSTANCES

# Display a warning message about potential costs
echo "WARNING: This script will create $NUM_INSTANCES EC2 instances in your AWS account, which can incur costs."
echo "FREE TIER LIMIT is 750 EC2 hours per month"

read -p "Do you want to continue? (Y/N): " CONTINUE

# Convert the user's input to uppercase for case-insensitive comparison
CONTINUE=$(echo "$CONTINUE" | tr '[:lower:]' '[:upper:]')

# Check if the user wants to continue
if [[ "$CONTINUE" != "Y" ]]; then
  echo "Exiting the script. No instances will be created."
  exit 0
fi

# Validate the input for presence
if [[ -z "$NUM_INSTANCES" ]]; then
  echo "Error: Input for number of instances is required."
  exit 1
fi

# Check if NUM_INSTANCES exceeds 100
if [[ "$NUM_INSTANCES" -gt 100 ]]; then
  echo "Error: Number of instances should not exceed 100."
  exit 1
fi

# Set the region where you want to create instances
AWS_REGION="us-east-1"

# AMI ID of the Free Tier eligible instance in your region (Amazon Linux 2, t2.micro)
AMI_ID="ami-05548f9cecf47b442"

# Instance Type eligible for Free Tier (t2.micro)
INSTANCE_TYPE="t2.micro"

# Create EC2 instances
echo "Creating $NUM_INSTANCES EC2 instances..."
for i in `seq 1 $NUM_INSTANCES`
do
  echo "creating instance# $i"
  aws ec2 run-instances \
    --image-id "$AMI_ID" \
    --instance-type "$INSTANCE_TYPE" \
    --count 1 \
    --region "$AWS_REGION" >/dev/null 2>/dev/null
done


# Wait for instances to be in 'running' state
echo "Waiting for instances to be in 'running' state..."
aws ec2 wait instance-running --region "$AWS_REGION" --instance-ids $(aws ec2 describe-instances --filters "Name=instance-state-name,Values=pending" --query "Reservations[].Instances[].InstanceId" --output text --region "$AWS_REGION")

# Get the public IP addresses of the instances
echo "Getting public IP addresses..."
PUBLIC_IPS=$(aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].PublicIpAddress" --output text --region "$AWS_REGION")

echo "Public IP addresses of instances:"
echo "$PUBLIC_IPS"

# Terminate EC2 instances
echo "Terminating EC2 instances..."
for ip in $PUBLIC_IPS; do
  instance_id=$(aws ec2 describe-instances --filters "Name=ip-address,Values=$ip" --query "Reservations[].Instances[].InstanceId" --output text --region "$AWS_REGION")
  echo "Terminating instance with ip: $ip"
  aws ec2 terminate-instances --instance-ids "$instance_id" --region "$AWS_REGION" >/dev/null 2> /dev/null
done

echo "EC2 instances terminated successfully."
