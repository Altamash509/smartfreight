import boto3

# This uses the same credentials stored from `aws configure`
s3 = boto3.resource('s3')

print("Listing buckets...")
for bucket in s3.buckets.all():
    print(bucket.name)
