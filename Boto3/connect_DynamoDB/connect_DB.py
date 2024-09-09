import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('MusicCollection')
try:
    response = table.meta.client.describe_table(TableName='MusicCollection')
    print(response['Table'])
except Exception as e:
    print(f"Error: {e}")

