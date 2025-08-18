import pymongo

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["autonomous_trucks"]

# Collections
trucks_collection = db["trucks"]
users_collection = db["users"]
schedules_collection = db["schedules"]
service_requests_collection = db["service_requests"]

# New alerts collection
alerts_collection = db["alerts"]