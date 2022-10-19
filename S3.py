import boto3
import csv
from statistics import mean
import pandas as pd
from botocore.exceptions import ClientError
import numpy as np


s3 = boto3.client('s3')
response = s3.list_buckets()['Buckets']
for bucket in response:
   # print('Bucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))
    #name = bucket['Name'].split(',')
    name = bucket['Name'].split(', ')
    date = bucket['CreationDate']

    with open("output.txt", "a") as f:
     print(name, file=f)
     print(date, file=f)
   # np.savetxt("s5.csv", 
    #       name,
    #       delimiter =", ", 
    #      fmt ='% s')

    #print(name)

   # dict = ({'Bucket name': [name], 'Created on': [date]})
   # df = pd.DataFrame(data=dict)
   # print(df.to_csv(sep='\t',index=False, header=False))

   # df.to_csv('/Users/sahayagodson/Documents/AWS-Python/S3/s3.csv',sep='\t',index=False, header=True)
