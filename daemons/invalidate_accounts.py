from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import int
from future import standard_library
standard_library.install_aliases()
from builtins import input
from builtins import str
#!/usr/bin/env python
import time
import pymongo
import pymongo.objectid
if "Darwin" in os.popen("uname").read():
	MONGOSERVER = 'localhost'
else:
	MONGOSERVER = '192.168.167.192'
	
MONGOPORT = 27017

def getDB():
    conn = None
    while not conn:
        try:
            conn = pymongo.Connection(MONGOSERVER, MONGOPORT)
        except Exception as e:
            time.sleep(1)
            print("no conn", e)
    db = conn.newsrivr
    return db

def getCollUsers():
    db = getDB()
    coll = db.users
    return coll

def getCollDrops():
    db = getDB()
    coll = db.drops
    return coll

def clog(s):
    print(str(s))
    
def main():
    print("PAS OP: INVALIDATE USERS !!!")
    import random
    ri = random.randint(100,1000)
    print(ri)
    keepdropuser = []
    deletedropuser = []
    richeck = input("Check: wat is het nummer: ")    
    if ri==int(richeck):
        print("ok, invalidating")
        for u in getCollUsers().find():
            if "screen_name" in u:
                if "rabshakeh" == u["screen_name"]:
                    print(u["screen_name"])
                    del u["access_token"]
                    getCollUsers().save(u, safe=True)
        print("done")
        return
    else:
        print("bye")

            
if __name__ == '__main__':
    main()