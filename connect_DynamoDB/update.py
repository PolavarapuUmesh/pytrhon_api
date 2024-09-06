import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('MusicCollection')

try:
    table.update_item(
        Key={
            'Artist': 'balu_babi', 
            'SongTitle': 'nee_preshnallu'  
        },
        UpdateExpression='SET Album = :album, ReleaseYear = :year',
        ExpressionAttributeValues={
            ':album': 'kbl', 
            ':year': 2025 
        }
    )
    print("Item updated successfully.")
except Exception as e:
    print(f"Error: {e}")
