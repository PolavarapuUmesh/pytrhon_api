import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('MusicCollection')

try:
    table.delete_item(
        Key={
            'Artist': 'ani_popudi',  
            'SongTitle': 'blue_ocean'  
        }
    )
    print("Item deleted successfully.")
except Exception as e:
    print(f"Error: {e}")
