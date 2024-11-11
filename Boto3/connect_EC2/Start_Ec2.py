import boto3
def start_instance(instance_id):
# def stop_instance(instance_id):
    ec2 =  boto3.client('ec2')
    response = ec2.start_instances(InstanceIds=[instance_id])
    # response = ec2.stop_instances(InstanceIds=[instance_id])

    print(f"Starting instance: {instance_id}")
    # print(f"Stopping instance: {instance_id}")

    print(response)

start_instance('107.23.223.14')   
# stop_instance('i-0a3c970bd1af8fb87')  
