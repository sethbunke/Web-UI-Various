import pymongo
from pymongo import MongoClient
url = 'mongodb://test1:test1@ds021694.mlab.com:21694/pymongo1'

client = MongoClient(url)
#client = MongoClient(host='ls021694.mlab.com', port=21694)
db = client.pymongo1
cursor = db.col1.find()

print(cursor)

for document in cursor:
    print(document)


# import pymongo
# from pymongo import MongoClient
# url = 'mongodb://test1:test1@ds021694.mlab.com:21694/pymongo1'




# client = MongoClient(url)
# #client = MongoClient(host='ls021694.mlab.com', port=21694)
# db = client.T5_DataViews
# #cursor = db.9412.find()
# #cursor = db.get_collection("9412").find()

# print(cursor)

# for document in cursor:
#     print(document)