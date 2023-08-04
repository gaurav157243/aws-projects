import boto3
import os
import json

def lambda_handler(event, context):
        
    dynamodb = boto3.resource('dynamodb')
    #table_name = os.environ.get('TABLE')
    table = dynamodb.Table('user-table')
    

    # Parse the data sent in the request payload
    try:
        request_data = json.loads(event['body'])
        print(request_data)
        user_id = request_data['UserId']
        user_name = request_data['UserName']
        email = request_data['Email']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input data')
        }

    # Insert data into DynamoDB
    data_to_insert = {
        'UserId': user_id,
        'UserName': user_name,
        'Email': email
    }
    
    table.put_item(Item=data_to_insert)

    return {
        'statusCode': 200,
        "headers": {
                "Access-Control-Allow-Origin": "*",  # Change this to the allowed origin(s) or '*' for any origin
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",  # Add other allowed methods as needed
                "Access-Control-Allow-Headers": "Content-Type, Authorization"  # Add other allowed headers as needed
        },
        'body': json.dumps('DynamoDB operations executed successfully!')
    }
