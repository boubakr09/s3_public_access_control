## Control s3 public access

Amazon s3 ACL enable you to define which AWS account or group can access buckets and objects, also define the type (Read or Write) of access. Imagine you are working on a project where public access on s3 bucket are not allowed. So you put in place a control mechanism which can varify the permissions on your buckets, if there any, delete the public access block and send you an email using Amazon SNS. 

You can control these ACL using python (see : [script](https://github.com/boubakr09/s3_public_access_control/blob/master/s3_public_access_control.py))

## Test
Run the command bellow:
```
python3 s3_public_access_control.py
```
