from backend.extensions import redis

class Redisi(object):
    def __init__(self):
        self.r = redis
    
    def set_data(self, key, value, expired=None):
        r = self.r
        if expired:
            r.set(key,value,expired)
        else:
            r.set(key,value)
        return True
    
    def get_data(self,key):
        r = self.r
        return r.get(key)

    def del_data(key):
        r = self.r 
        r.delete(key)
        return True