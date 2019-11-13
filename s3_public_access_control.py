import boto3

#Create an s3 client
s3 = boto3.client('s3')
#Create an sns client
sns = boto3.client('sns')

#email address of the subscriber
endpoint = 'email_address_of_subscriber'

#Create an sns topic
response = sns.create_topic(Name='s3_public_access_control')
#save the topic arn in the variable 'topicarn'
topicarn = (response['TopicArn'])

#get the subscribers of the topic
response6 = sns.list_subscriptions_by_topic(
    TopicArn=topicarn
    )

#verify if the given endpoint already subscribe to the topic
if (response6['Subscriptions']) == '[]' or (response6['Subscriptions'][0]['Endpoint']) == endpoint::
    #if so, do nothing
    pass
#if not proceed to subscription
else:
    response2 = sns.subscribe(TopicArn=topicarn, Protocol='email', Endpoint=endpoint)


#get list of existing buckets
response3 = s3.list_buckets()

#a loop to browse the list of buckets
for bucket in response3['Buckets']:
    #save the bucket name in variable 'bucket_name'
    bucket_name = (bucket['Name'])
    #get the bucket permission
    response4 = s3.get_bucket_acl(Bucket=bucket_name)
    #a loop to browse those permission
    for permission in response4['Grants']:
        #verify if the permission is public (READ or WRITE)
        if (permission['Grantee']['Type']) == 'Group':
            if (permission['Permission']) == 'READ' or (permission['Permission']) == 'WRITE':
                #save the buckets names which has public access
                bucket_with_public_access = (bucket['Name'])
                #remove the public access permission on the given bucket
                s3.put_public_access_block(
                    Bucket=bucket_with_public_access,
                    PublicAccessBlockConfiguration={
                        'BlockPublicAcls': True,
                        'IgnorePublicAcls': True,
                        'BlockPublicPolicy': True,
                        'RestrictPublicBuckets': True
                    }
                )
                #save the bucket name that has public access in variable 'message'
                message = ('Public access on '+bucket_with_public_access+' bucket')
                #publish a message send via email to subscribers
                response5 = sns.publish(
                    TopicArn = topicarn,
                    Message = message,
                    Subject = 's3 Public Access Control',
                    )
