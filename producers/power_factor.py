import boto3
import json
from random import uniform
import time
from datetime import datetime


cliente = boto3.client('kinisis',aws_access_key_id ='ID_EXAMPLE', aws_secret_access_key='SECRET_EXAMPLE',
                       region_name='us-east-1')


id = 0
while True:
    data = uniform(0.7,1)
    id += 1;
    register = {'idtemp': str(id), 'data':str(data), 'type': 'power_factor', 'timestamp': str(datetime.now())}
    cliente.put_record(StreamName = 'windfarm', Data = json.dumps(register), Partitionkey = '02')
    time.sleep(5)
    # print(register)
