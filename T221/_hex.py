import binascii
import codecs


class config:
    _history = []

def decode(code):
    ans = ""
    try:
        ans = binascii.unhexlify(code).decode()
    except Exception as e:
        print(e)
        ans= f"[ム] Decode Error! Code : {code} "

    # return ans

    if(ans.startswith('[ム]')):
        config._history.append([code, ans,'error'])
    else:
        config._history.append([code, ans,'gud'])

def encode(code):
    ans = ""
    try:
        hexlify = codecs.getencoder('hex')
        ans = hexlify(bytes(code, 'utf-8'))[0].decode("ascii")
    except Exception as e:
        print(e)
        ans = f"[ム] Encode Error! Code: {code}"

    if(ans.startswith('[ム]')):
        config._history.append([code, ans,'error'])
    else:
        config._history.append([code, ans,'gud'])


def history():
    return config._history