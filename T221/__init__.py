import T221._base64 as T_base64
import T221._base32 as T_base32
import T221._hex as T_hex
import T221._caesar_cipher as T_ceasar
import base64
import binascii
import codecs

class config:
    _hdb_path = "./static/HDB.HS"

def HDB():
    _hdb = []

    with open(config._hdb_path,'r') as f:
        for line in f:
            text = line.strip().split('-------')
            try:
                _hdb.append(
                    [
                        base64.b64decode((binascii.unhexlify(text[0]).decode())).decode("ascii"),
                        base64.b64decode((binascii.unhexlify(text[1]).decode())).decode("ascii")
                    ]
                )
            except:
                pass
    return _hdb

def correct(H_ID,H_PASS):
    _hdb = HDB()
    for up in _hdb:
        if(up[0]==H_ID and up[1]==H_PASS):
            return True
    return False