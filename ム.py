from flask import Flask,render_template,request,session,redirect,flash
from T221 import *
from functools import wraps
import random 
import time 

ム = Flask(__name__)
ム.secret_key = 'ム'

def login_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if 'H_ID' in session:
            return route_function(*args, **kwargs)
        else:
            return redirect('/login')
    return wrapper

@ム.before_request
def check_login():
    if request.endpoint and request.endpoint != 'login' and 'H_ID' not in session:
        return redirect('/login')

@ム.route('/')
@login_required
def index():
    return render_template("index.html")

# Encode - Decode
@ム.route('/base64',methods=['GET','POST'])
@login_required
def base64():
    if request.method == "POST":
        data = (request.form).to_dict(flat=False)
        if "code" in data:
            try:
                code = data["code"][0]
                # print(code[0])
                if("decode" in data):
                    T_base64.decode(code)
                else:
                    T_base64.encode(code)

                print(T_base64.history())
            except:
                print("[ム] Base64 Error!")
        elif "clear_history" in data:
            T_base64.config._history = []
    return render_template('/en_decode/base64.html',_history=T_base64.history()[::-1])

@ム.route('/base32',methods=['GET','POST'])
@login_required
def base32():
    if request.method == "POST":
        data = (request.form).to_dict(flat=False)
        if "code" in data:
            try:
                code = data["code"][0]
                # print(code[0])
                if("decode" in data):
                    T_base32.decode(code)
                else:
                    T_base32.encode(code)

                print(T_base32.history())
            except:
                print("[ム] Base32 Error!")
        elif "clear_history" in data:
            T_base32.config._history = []
    return render_template('/en_decode/base32.html',_history=T_base32.history()[::-1])

@ム.route('/hex',methods=['GET','POST'])
@login_required
def hex():
    if request.method == "POST":
        data = (request.form).to_dict(flat=False)
        if "code" in data:
            try:
                code = data["code"][0]
                # print(code[0])
                if("decode" in data):
                    T_hex.decode(code)
                else:
                    T_hex.encode(code)

                print(T_hex.history())
            except:
                print("[ム] Hex Error!")
        elif "clear_history" in data:
            T_hex.config._history = []
    return render_template('/en_decode/hex.html',_history=T_hex.history()[::-1])

@ム.route('/caesar_cipher',methods=['GET','POST'])
@login_required
def caesar_cipher():
    if request.method == "POST":
        data = (request.form).to_dict(flat=False)
        if "code" in data and "shift" in data:
            try:
                code = data["code"][0]
                shift = (data["shift"][0])
                # print(code[0])
                if("decode" in data):
                    T_ceasar.decode(code,shift)
                else:
                    T_ceasar.encode(code,shift)

                print(T_ceasar.history())
            except:
                print("[ム] Caesar_cipher Error!")
        elif "clear_history" in data:
            T_ceasar.config._history = []
    return render_template('/en_decode/caesar_cipher.html',_history=T_ceasar.history()[::-1])


@ム.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        H_ID = request.form['H_ID']
        H_PASS = request.form['H_PASS']
        if correct(H_ID,H_PASS):
            session['H_ID'] = H_ID
            print("Logged in!",H_ID,H_PASS)
            return redirect('/')
        else:
            return render_template('login.html', error=False)
    else:
        return render_template('login.html', error=False)
@ム.route('/logout')
def logout():
    session.pop('H_ID', None)
    return redirect('/')

if __name__ =="__main__":
    from waitress import serve
    serve(ム, host="0.0.0.0", port=4444)


"""
ム Hawks : [T221] [H4wK1n6] [inv member]
* Copright Hawks Inc.
"""
