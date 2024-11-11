import boto3

ec2 = boto3.client('ec2')

def describe_instances():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"Instance Type: {instance['InstanceType']}")
            print(f"State: {instance['State']['Name']}")
            print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")
            print('---')

def start_instance(instance_id):
    response = ec2.start_instances(InstanceIds=[instance_id])
    print(f"Starting instance: {instance_id}")
    print(response)

def stop_instance(instance_id):
    response = ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Stopping instance: {instance_id}")
    print(response)

if __name__ == "__main__":
    describe_instances()
    start_instance('i-0abcdef1234567890')
    stop_instance('i-0abcdef1234567890')
