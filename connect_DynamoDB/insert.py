import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('MusicCollection')
try:
    table.put_item(
        Item={
            'Artist': 'ani_popudi', 
            'SongTitle': 'blue_ocean',  
            'Album': 'belive',  
            'ReleaseYear': 2024  
        }
    )
    print("Item inserted successfully.")
except Exception as e:
    print(f"Error: {e}")
