import datetime
from time import timezone
import pymongo

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000")
    print("Your db is now connected.")
except:
    print("Database connection error!!!***")

mydb = myclient["project"]
mycol = mydb["sales"]

agg=[
    {
        '$match': {
            'saleDate': {
                '$gte': datetime(2015, 8, 25, 10, 1, 2, tzinfo=timezone.utc), 
                '$lt': datetime(2015, 8, 27, 0, 0, 0, tzinfo=timezone.utc)
            }
        }
    }
]

TestOutput = mycol.aggregate(agg)
print(list(TestOutput))


myclient.close()