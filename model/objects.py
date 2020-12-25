
from pymongo import *
import hashlib

def encrypt(rp ):
    encoded_message= hashlib.sha256(str.encode(rp)) 
    converted=encoded_message.hexdigest()
    return converted


client = MongoClient('localhost',27017)

db = client.aitodo

coll  = db.comp

class customer():
    def __init__(self,fname:str,lname:str,company:str,colleagues:int,email:str,password:str,phone:str,user:str):
        self.fname = fname
        self.lname  = lname
        self.company = company
        self.colleagues = colleagues
        self.email = email
        self.password = password
        self.phone = phone
        self.user = user
        self.status = "y"

    def addusertodb(self):
        cooked  = customertodict(self)
        if companyispresent(self.company) ==True:
            return "your company is already registred"
        if companyispresent(self.company) ==False:
            
            mdata = coll.insert_one(cooked)
            return mdata.inserted_id
    
    def serchbynameandpassword(self):
        res = "user is not signed up"
        passw = encrypt(self.password)
        userdata = coll.find_one({"username":self.user,"password":passw})
        if userdata!=None:
            if userdata['status'] == 'y':
                res =  userdata
            else:
                res = "user is not verified"
        return res 
    

def companyispresent(cmp):
    ispresent = False
    arr = getallcustomer()
    if len(arr)>=1:
        for c in arr:
            if c["comapany"] == cmp:
                ispresent =True
                break
    else:
        ispresent =False
    return ispresent

def customertodict(c :customer)->dict:
    cooked = {
        "firstname":c.fname,
        "lastname":c.lname,
        "comapany" :c.company,
        "employees" :c.colleagues,
        "email" :c.email,
        "password" :encrypt(c.password),
        "phone":c.phone,
        "username":c.user,
        "status":c.status
    }
    return cooked

def getallcustomer():
    ar =[]
    for us in coll.find():
        ar.append(us)
    return(ar)


c1= customer("rishi","jha","",0,"","rishi","","rishi")
c2= customer("komal","jha","kj",0,"","rishi","","komal")
print(getallcustomer())