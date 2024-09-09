import boto3

def create_dynamodb_table():
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')

    table_name = 'MusicCollection'
    key_schema = [
        {
            'AttributeName': 'Artist',
            'KeyType': 'HASH'               #Hasn is for partition key 
        },
        {
            'AttributeName': 'SongTitle',
            'KeyType': 'RANGE'              #Range is for sort key
        }
    ]

    attribute_definitions = [
        {
            'AttributeName': 'Artist',
            'AttributeType': 'S'  
        },
        {
            'AttributeName': 'SongTitle',
            'AttributeType': 'S' 
        }
    ]

    provisioned_throughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput=provisioned_throughput
        )

        print(f"Table creation initiated: {response['TableDescription']['TableName']}")
        
        table = boto3.resource('dynamodb', region_name='us-east-1').Table(table_name)
        table.wait_until_exists()
        print(f"Table {table_name} created successfully.")

    except Exception as e:
        print(f"Error creating table: {e}")

create_dynamodb_table()
