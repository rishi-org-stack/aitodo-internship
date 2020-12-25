from pymongo import *

import hashlib

client = MongoClient('localhost',27017)

dbb = client.aitodo


def encrypt(rp ):
    encoded_message= hashlib.sha256(str.encode(rp)) 
    converted=encoded_message.hexdigest()
    return converted


def coll(collection):
    return db[collection]


def serchbynameandpassword(name,password,db):
    collt = coll(db)
    res = "user is not signed up"
    passw = encrypt(password)
    userdata = collt.find_one({"name":name,"password":passw})
    if userdata!=None:
        if userdata['status'] == 'y':
            res =  userdata
        else:
            res = "user is not verified"
    return res

