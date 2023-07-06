import base64,json

class config:
    _history = []

def decode(code):
    ans = ""
    try:
        ans = base64.b32decode(code).decode("ascii")
    except:
        ans= f"[ム] Decode Error! Code : {code} "

    # return ans

    if(ans.startswith('[ム]')):
        config._history.append([code, ans,'error'])
    else:
        config._history.append([code, ans,'gud'])

def encode(code):
    ans = ""
    try:
        ans = base64.b32encode(bytes(code, 'utf-8')).decode("ascii")
    except:
        ans = f"[ム] Encode Error! Code: {code}"

    if(ans.startswith('[ム]')):
        config._history.append([code, ans,'error'])
    else:
        config._history.append([code, ans,'gud'])

def history():
    return config._history