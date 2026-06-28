 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
     
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    # Create Method
    def create(self, data):
        if data is not None: 
            try:
                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            
            except Exception as e:
                print("Insert failed:", e)
                return False
        
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    
    # Read Method 
    
    def read(self, query):
        try:
            data = self.database.animals.find(query)
            return list(data)
        except Exception as e: 
            print("Read failed:", e)
            return []
    
    #Create method to implement the U in CRUD. 
    
    # Update Method 
    
    def update(self, query, new_values):
        try:
            result = self.database.animals.update_many(query, new_values)
            return result.modified_count
        except Exception as e:
            print("Update failed:", e)
            return 0
        
    # Create method to implement D in CRUD.
  
    # Delete Method
  
    def delete(self, query):
        try:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Delete failed:", e)
            return 0

 

  
    