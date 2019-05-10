import sys
sys.path.append("./deps")
sys.path.append("../../")
import os
import time

os.environ["pspringaws.region"]="us-east-2"
os.environ["pspringaws.apiId"]="jc2fibip45cidbkhqcxyzvgu5i"
secretId = "XXX"

import pspringaws
from appsyncclient import AppSyncClient
import json

import logging
logging.basicConfig(level=logging.DEBUG)

# def test_realtimesecretmngr():
#     configProvider = pspringaws.RealTimeSecretsMgrConfigProvider(secretId=secretId)
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

# client = AppSyncClient(region="us-east-2",apiId="jc2fibip45cidbkhqcxyzvgu5i")
# datajson={
#     "data" : "\"",
#     "name" : "test5",
#     "scope" : "test5"
# }
# data=json.dumps(datajson)
# data = data.replace('\\"','"')
# data = data.replace("\"","\\\"")
# id="arn:aws:dynamodb:::dev-token-cache:test5:test5"
# query = json.dumps({"query": "mutation {\n  updateResource(id:\""+id+"\",data:\""+data+"\") {\n    id\n    data\n  }\n}\n"})
# print(query)
# # query = "{\"query\": \"mutation {\\n  updateResource(id:\\\"arn:aws:dynamodb:::dev-token-cache:test5:test5\\\",data:\\\"{\\\\\\\"data\\\\\\\": \\\\\\\"{\\\\\\\\\\\"firstname\\\\\\\\\\\":\\\\\\\\\\\"vasudevn\\\\\\\\\\\"}\\\\\\\", \\\\\\\"scope\\\\\\\": \\\\\\\"test5\\\\\\\", \\\\\\\"name\\\\\\\": \\\\\\\"test5\\\\\\\"}\\\") {\\n    id\\n    data\\n  }\\n}\\n\"}"
# # print(query)
# def secretcallback(client, userdata, msg):
#     logger.debug("New data received : "+str(msg))
#     callback(json.loads(msg.payload).get("data",{}).get("updatedResource",{}).get("data"))

# response = client.execute(data=query,callback=secretcallback)
# print(response)
def test_realtimedynamoconfigprovider():
    configProvider = pspringaws.RealTimeDynamodbConfigProvider(
        tableName="XXX",
        primaryKey="XXX",
        primaryKeyName="name",
        sortKeyName="scope",
        sortKey="XXX",
        configColumnName="data",
        apiId="XXXX"
    )
    time.sleep(20)
    assert configProvider.getProperty("firstname") == "vasudevan"

# def test_dynamoconfigprovider():
#     configProvider = pspringaws.DynamodbConfigProvider(
#         tableName="XXX",
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
#     configProvider = pspringaws.RealTimeS3ConfigProvider(bucketId="soo-appconfig-dev",objectKey="sooproxyapi.json")
#     time.sleep(200)
#     assert configProvider.getProperty("sooproxyapi.apiconfig")!=None

# def test_scheduleds3configprovider():
#     configProvider = pspringaws.ScheduledS3ConfigProvider(bucketId="XXX",objectKey="XXX",period="5")
#     time.sleep(50)
#     assert configProvider.getProperty("sooproxyapi.apiconfig")!=None

# def test_scheduledsecretmngrconfigprovider():
#     configProvider = pspringaws.ScheduledSecretsMngrConfigProvider(secretId="XXX",period="5")
#     time.sleep(50)
#     assert configProvider.getProperty("sooproxyapi.apiconfig")!=None