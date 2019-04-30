import sys
sys.path.append("./deps")
sys.path.append("../../")
import os
import time

os.environ["pspringaws.region"]="us-east-2"
os.environ["pspringaws.apiId"]="XXX"
secretId = "XXX"

import pspringaws

import logging
logging.basicConfig(level=logging.DEBUG)

def test_realtimesecretmngr():
    configProvider = pspringaws.RealTimeSecretsMgrConfigProvider(secretId=secretId)
    assert configProvider.getProperty("XX")==str(3600)

def test_secretmngr():
    configProvider = pspringaws.SecretsMgrConfigProvider(secretId=secretId)
    assert configProvider.getProperty("XX")==str(3600)

def test_dynamodb():

    @pspringaws.DynamoDBTable(tableName="XXX",primaryKey="name",sortKey="scope")
    class TestDynamo():
        pass
    table = TestDynamo()
    response = table.get("test",column="firstname",scope="test")
    assert response=="vas"

def test_s3configprovider():
    configProvider = pspringaws.S3ConfigProvider(bucketId="XXX",objectKey="XXX")
    assert configProvider.getProperty("XXX")!=None

def test_realtimes3configprovider():
    configProvider = pspringaws.RealTimeS3ConfigProvider(bucketId="XXX",objectKey="XXX")
    assert configProvider.getProperty("XXX")!=None

def test_scheduleds3configprovider():
    configProvider = pspringaws.ScheduledS3ConfigProvider(bucketId="XXX",objectKey="XXX",period="5")
    time.sleep(50)
    assert configProvider.getProperty("sooproxyapi.apiconfig")!=None

def test_scheduledsecretmngrconfigprovider():
    configProvider = pspringaws.ScheduledSecretsMngrConfigProvider(secretId="XXX",period="5")
    time.sleep(50)
    assert configProvider.getProperty("sooproxyapi.apiconfig")!=None