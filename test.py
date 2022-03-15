import requests
import json

BASE_URL = "http://127.0.0.1:801/"

se = requests.session()
def test1():
    print("开始发送:")
    try:
        resp = se.get(BASE_URL + "api/balance?token=token")
    except Exception as Ex:
        raise Ex
    res = json.loads(resp.text)
    print(res)

def test2():
    print("开始发送:")
    try:
        resp = se.get(BASE_URL + "api/position?token=token")
    except Exception as Ex:
        raise Ex
    res = json.loads(resp.text)
    print(res)

def test3():
    print("开始发送:")
    try:
        resp = se.get(BASE_URL + "api/orders/today?token=token")
    except Exception as Ex:
        raise Ex
    res = json.loads(resp.text)
    print(res)

def test4():
    print("开始发送:")
    try:
        resp = se.get(BASE_URL + "api/orders/filled?token=token")
    except Exception as Ex:
        raise Ex
    res = json.loads(resp.text)
    print(res)

def test5(d):
    print("开始发送:")
    print(d)
    try:
        resp = se.post(BASE_URL + "api/sell",data=json.dumps(d))
    except Exception as Ex:
        print(Ex)
    res = json.loads(resp.text)
    print(res)

def test6(d):
    print("开始发送:")
    print(d)
    try:
        resp = se.post(BASE_URL + "api/buy",data=json.dumps(d))
    except Exception as Ex:
        print(Ex)
    res = json.loads(resp.text)
    print(res)



#交流讨论+威信: gupiao888nb
if __name__ == "__main__":
    
    d = {
        "token":"token",
        "code":"603969",
        "amount":"100",
        "price":"5.10",
        "is_market":0
    }
    '''
    test5(d)
    test6(d)
    test1()
    test2()
    test3()
    test4()
    '''
    test5(d)
