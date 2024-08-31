import json
from datetime import datetime

def lambda_handler(event, context):
    # Get the current UTC time
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create a response
    response = {
        'statusCode': 200,
        'body': json.dumps({
            'current_time': current_time
        })
    }
    
    return response
