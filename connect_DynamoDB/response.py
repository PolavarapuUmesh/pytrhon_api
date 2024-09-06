
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('MusicCollection')
try:
    response = table.get_item(
        Key={
            'Artist': 'jesus_barber',  
            'SongTitle': 'boo..boo'  
        }
    )
    item = response.get('Item')
    if item:
        print(f"Item retrieved: {item}")
    else:
        print("Item not found.")
except Exception as e:
    print(f"Error: {e}")