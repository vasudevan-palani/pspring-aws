import sys
sys.path.append("./deps")
sys.path.append("../../")
import os

os.environ["pspringaws.region"]="us-east-2"
os.environ["pspringaws.realtimesecretsmngrconfigprovider.apiId"]="3h5qsweuu5ebvny3q5ibu77dyi"

import pspringaws

def test_realtimesecretmngr():
    configProvider = pspringaws.RealTimeSecretsMgrConfigProvider(secretId="sales-ctp-dev")
    assert configProvider.getProperty("websec_TTL")==3600

def test_secretmngr():
    configProvider = pspringaws.SecretsMgrConfigProvider(secretId="sales-ctp-dev")
    assert configProvider.getProperty("websec_TTL")==3600

def test_dynamodb():

    @pspringaws.DynamoDBTable(tableName="dev-token-cache",primaryKey="name",sortKey="scope")
    class TestDynamo():
        pass
    table = TestDynamo()
    response = table.get("test",column="firstname",scope="test")
    assert response=="vas"
