import os
from azure.cosmos import CosmosClient, exceptions

# 從環境變數中獲取 Cosmos DB 的信息
uri = os.environ['COSMOS_DB_URI']
key = os.environ['COSMOS_DB_KEY']
database_name = os.environ['COSMOS_DB_DATABASE_NAME']
container_name = os.environ['COSMOS_DB_CONTAINER_NAME']

# 創建 Cosmos DB 客戶端
client = CosmosClient(uri, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# 插入數據
data = {
    'id': 'item1',
    'name': 'GitHub Action Item',
    'description': 'This item was added by a GitHub Action'
}

try:
    container.create_item(body=data)
    print("Item successfully added!")
except exceptions.CosmosResourceExistsError:
    print("Item already exists!")
