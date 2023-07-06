class config:
    _history = []

def decode(code,shift):
    ans = ""
    try:
        for v in code:
            if(v==" "):
                ans+=" ";
            else:
                ans+=chr(ord(v) - int(shift))
    except Exception as e:
        print(e)
        ans = f"""[ム] Encode Error! Use integer instead of string for shift parameter."""

    # return ans


    if(ans.startswith('[ム]')):
        config._history.append([code, ans,'error',shift])
    else:
        config._history.append([code, ans,'gud',shift])

def encode(code,shift):
    ans = ""
    try:
        for v in code:
            if(v==" "):
                ans+=" ";
            else:
                ans+=chr(ord(v) + int(shift))
    except Exception as e:
        print(e)
        ans = f"""[ム] Encode Error! Use integer instead of string for shift parameter."""

    if(ans.startswith('[ム]')):
        config._history.append([code, ans,'error',shift])
    else:
        config._history.append([code, ans,'gud',shift])


def history():
    return config._history