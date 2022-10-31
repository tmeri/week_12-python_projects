#Purpose of the project: To list some of the AWS services, print length and delete from the list.
#1, The list should be empty initially.

AWS_Services_List = []

#2, Populate the list using append or insert.

AWS_Services_List.append('EC2')
AWS_Services_List.append('VPC')
AWS_Services_List.append('Lambda')
AWS_Services_List.append('S3')
AWS_Services_List.append('EFS')
AWS_Services_List.append('Storage Gateway')
AWS_Services_List.append('DynamoDB')
AWS_Services_List.append('RDS')
AWS_Services_List.append('ElasticCache')
AWS_Services_List.append('Elastic Kubernetes Service')


#3, Print the list and the length of the list.

print(AWS_Services_List)

print(len(AWS_Services_List))

#4, Remove two specific services from the list by name or by index.

del AWS_Services_List  [2]
del AWS_Services_List  [7]

#5, Print the new list and the new length of the list.

print(AWS_Services_List)

print(len(AWS_Services_List))








