from pymongo import MongoClient
from os import environ
from ..constants import mongo_uri

class Connector:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Connector.__instance == None:
            Connector()
        return Connector.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Connector.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.__client = MongoClient(environ.get(mongo_uri)[1:-1])
            self.__db = self.__client.ShifterMongoDB
            self.__status = True
            Connector.__instance = self

    def close_connection(self):
        if self.__status:
            self.__status = False
            self.__client.close()
            Connector.__instance = None
        else:
            print("You cannot close a closed or not open client")

    def does_collection_exist(self, name):
        col_list = self.__db.list_collection_names()
        return name in col_list

    def get__collection(self, name):
        if self.does_collection_exist(name):
            return self.__db[name]
        else:
            return None