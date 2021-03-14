class Repository:
    """
    Repository for storing domain objects
    """
    def __init__(self):
        self._objects = []

    def store(self, obj):
        pass

    def update(self, object):
        pass

    def find(self, objectId):
        pass

    def delete(self, objectId):
        pass
    
    def getAll(self):
        return self._objects

    def __len__(self):
        return len(self._objects)

    def __str__(self):
        r = ""
        for e in self._objects:
            r += str(e)
            r += "\n"
        return r
