import hashlib

def encrypt(rp ):
    encoded_message= hashlib.sha256(str.encode(rp)) 
    converted=encoded_message.hexdigest()
    return converted
