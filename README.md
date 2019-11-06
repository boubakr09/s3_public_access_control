## Control s3 public access

Amazon s3 ACL enable you to define which AWS account or group can access buckets and objects, also define the type (Read or Write) of access. Imagine you are working on a project where public access on s3 bucket are not allowed. So you put in place a control mechanism which can varify the permissions on your buckets and send you an email (using Amazon SNS) if there any public access on a bucket. 

You can control these ACL using python

## Test
Run the python script bellow
