#from data_handlers import MongoDBDataHandler, FileDataHandler, SimpleDirectoryReaderHandler

class DataHandlerFactory:
    def __init__(self):
        self._handlers = {}
        
    def register_handler(self, name, handler):
        self._handlers[name] = handler
        
    def get_handler(self, name):
        if name not in self._handlers:
            raise ValueError(f"Handler not found: {name}")
        return self._handlers[name]()

# Create an instance of DataHandlerFactory
data_handler_factory = DataHandlerFactory()

# Register our previously defined data handlers
from data_handlers import SimpleDirectoryReaderHandler, MongoDBDataHandler
data_handler_factory.register_handler("MongoDB", MongoDBDataHandler)

data_handler_factory.register_handler("SimpleDirectoryReader", SimpleDirectoryReaderHandler)


# Fixme: Wire up the SimpleDirectoryReaderHandler

# Usage example
# handler = data_handler_factory.get_handler("MongoDB")
