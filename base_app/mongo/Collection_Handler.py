from base_app.mongo.Connector import Connector

class CollectionHandler:
    def __init__(self, collection_name):
        self.connector = Connector.getInstance()
        self.collection = self.connector.get__collection(name=collection_name)
        if self.collection is None:
            raise ValueError(f'{collection_name} collection does not found!')
