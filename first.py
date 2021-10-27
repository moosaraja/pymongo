import pymongo
client = pymongo.MongoClient('mongodb://localhost')

db = client['cooker']
cars = db['training']
"""cars.insert_one({
    'make' : 'Ford',
    'Model' : 'Edge'
})
"""
results = cars.find({"Year":{"$gte":"2014"}},{"Year":1,"_id":0}).count()
print(results)
"""for result in results:
    print(result)"""
