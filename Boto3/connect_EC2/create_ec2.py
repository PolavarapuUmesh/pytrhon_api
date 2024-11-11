import boto3
ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId='ami-0c94855ba95c71c99',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='account.pem',
    SecurityGroups=['sg-07aa7ce82e0798c59']
    )
print("successfully created",response)

