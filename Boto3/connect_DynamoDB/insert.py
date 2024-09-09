import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('MusicCollection')
try:
    table.put_item(
        Item={
            'Artist': 'jonus_blue', 
            'SongTitle': 'blue_ocean',  
            'Album': 'on_the_way',  
            'ReleaseYear': 2024  
        }
    )
    print("Item inserted successfully.")
except Exception as e:
    print(f"Error: {e}")
