import requests
import json

# A股打板level2接口lev2数据股票量化交易程序化交易通达信指标交易同花顺自动交易

'''
lev2数据
lev2接口
LEV2数据
LEV2接口
level2数据
level2接口
LEVEL2数据
LEVEL2接口

涨停龙头战法
打板

'''

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
        "token":"token", # 校验token
        "code":"000000", # 自己修改股票代码
        "amount":"100",  # 数量
        "price":"11.11", # 价格
        "is_market":0    # 市价单 还是 限价单
    } 
    '''
    test5(d)
    test6(d)
    test1()
    test2()
    test3()
    test4()
    '''
    test1()
