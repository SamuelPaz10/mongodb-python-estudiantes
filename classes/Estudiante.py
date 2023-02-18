from classes.DbMongo import DbMongo

class Estudiante:

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__collection = "Estudiante"

    def save(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        client.close()

    def update_student(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]


        collection.find_one_and_update({'nombre:': self.nombre}, {'apellido': self.apellido})

        #collection.update_one({'nombre': self.nombre}, { "$set": {'apellido': self.apellido}})
        #collection.update_one({'apellido':"Pérez"}, { "$set": {'nombre': "Juan"}})

        client.close()