from classes.DbMongo import DbMongo

class Student:

    def __init__(self, name, last_name, cellphone):
        self.name = name
        self.last_name = last_name
        self.cellphone = cellphone
        self.__collection = "estudiante"

    def save(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        client.close()

    def update_student(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]

        #collection.update_one({'nombre':self.name}, { "$set": {'apellido':self.last_name}})
        collection.update_one({'_id': self.id}, { "$set": {self.__dict__}})

        client.close()
        
    def delete_student(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        client.close()