from pspring import ConfigurationProvider, Configuration
from .realtimes3 import RealTimeS3
import logging
import json
from .dynamodb import DynamoDBTable
from appsyncclient import AppSyncClient

logger = logging.getLogger(__name__)
config = Configuration.getConfig(__name__)

class RealTimeDynamodbConfigProvider(ConfigurationProvider):
    def __init__(self,**kargs):
        self.subscriptions = []
        self.tableName = kargs.get("tableName") or config.getProperty("tableName")
        self.primaryKey = kargs.get("primaryKey") or config.getProperty("primaryKey")
        self.primaryKeyName = kargs.get("primaryKeyName") or config.getProperty("primaryKeyName")
        self.sortKey = kargs.get("sortKey") or config.getProperty("sortKey")
        self.sortKeyName = kargs.get("sortKeyName") or config.getProperty("sortKeyName")
        self.region = kargs.get("region") or config.getProperty("region")
        self.configColumnName = kargs.get("configColumnName") or config.getProperty("configColumnName")
        self.apiId = kargs.get("apiId") or config.getProperty("apiId")

        @DynamoDBTable(
            tableName=self.tableName,
            primaryKey=self.primaryKeyName,
            sortKey=self.sortKeyName,
            region=self.region
        )
        class DynamoTable():
            pass
        self.table = DynamoTable()
        self.response = {}
        dynamoContent = self.table.get(self.primaryKey,scope=self.sortKey,column=self.configColumnName)
        try:
            self.response = json.loads(str(dynamoContent))
        except Exception as er:
            logger.warn(f"Received content from dynamodb was not json {er}")
        
        self.subscribeAppSync()

    def eventCallBack(self,response):
        logger.info("Received updated data "+str(response))
        self.response = json.loads(response).get(self.configColumnName)
        self.publish()

    def refresh(self):
        pass

    def subscribeAppSync(self):
        self.appsyncclient = AppSyncClient(region=self.region,apiId=self.apiId)
        
        id = "arn:aws:dynamodb:::"+self.tableName+":"+self.primaryKey
        if self.sortKey != None:
            id = id + ":"+self.sortKey

        query = json.dumps({"query": "subscription {\n  updatedResource(id:\""+id+"\") {\n    id\n    data\n  }\n}\n"})

        def secretcallback(client, userdata, msg):
            logger.debug("New data received : "+str(msg))
            self.eventCallBack(json.loads(msg.payload).get("data",{}).get("updatedResource",{}).get("data"))

        response = self.appsyncclient.execute(data=query,callback=secretcallback)


    def publish(self):
        for subscription in self.subscriptions:
            subscription()

    def getProperty(self,propertyName):
        return self.response.get(propertyName)

    def subscribe(self,callback):
        self.subscriptions.append(callback)
