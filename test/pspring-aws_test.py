import sys
sys.path.append("./deps")
sys.path.append("../../")
import os
import time

os.environ["pspringaws.region"]="us-east-2"
os.environ["pspringaws.apiId"]="XX"
secretId = "XXX"

import pspringaws
from appsyncclient import AppSyncClient
import json

import logging
logging.basicConfig(level=logging.DEBUG)

# def test_realtimesecretmngr():
#     configProvider = pspringaws.RealTimeSecretsMgrConfigProvider(secretId=secretId)
#     time.sleep(200)
#     assert configProvider.getProperty("XX")==str(3600)

# def test_secretmngr():
#     configProvider = pspringaws.SecretsMgrConfigProvider(secretId=secretId)
#     assert configProvider.getProperty("XX")==str(3600)

# def test_dynamodb():

#     @pspringaws.DynamoDBTable(tableName="XXX",primaryKey="name",sortKey="scope")
#     class TestDynamo():
#         pass
#     table = TestDynamo()
#     response = table.get("test",column="firstname",scope="test")
#     assert response=="vas"

def test_realtimedynamoconfigprovider():
    configProvider = pspringaws.RealTimeDynamodbConfigProvider(
        tableName="XXX",
        primaryKey="test5",
        primaryKeyName="name",
        sortKeyName="scope",
        sortKey="test5",
        configColumnName="data",
        tableAsConfig="True",
        apiId="XXX"
    )
    time.sleep(200)
    assert configProvider.getProperty("firstname") == "vasudevan"

# def test_dynamoconfigprovider():
#     configProvider = pspringaws.DynamodbConfigProvider(
        # tableName="XXX",
#         primaryKey="XXX",
#         primaryKeyName="XX",
#         sortKeyName="XXX",
#         sortKey="XXX",
#         configColumnName="data"
#     )
#     assert configProvider.getProperty("visitorId")!=None

# def test_s3configprovider():
#     configProvider = pspringaws.S3ConfigProvider(bucketId="XXX",objectKey="XXX")
#     assert configProvider.getProperty("XXX")!=None

# def test_realtimes3configprovider():
#     configProvider = pspringaws.RealTimeS3ConfigProvider(bucketId="XXX",objectKey="XXX.json")
#     time.sleep(200)
#     assert configProvider.getProperty("XXX")!=None

# def test_scheduleds3configprovider():
#     configProvider = pspringaws.ScheduledS3ConfigProvider(bucketId="XXX",objectKey="XXX",period="5")
#     time.sleep(50)
#     assert configProvider.getProperty("XXX")!=None

# def test_scheduledsecretmngrconfigprovider():
#     configProvider = pspringaws.ScheduledSecretsMngrConfigProvider(secretId="XXX",period="5")
#     time.sleep(50)
#     assert configProvider.getProperty("XXXX")!=None