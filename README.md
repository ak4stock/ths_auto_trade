# ths_auto_trade

股票A股同花顺trade通达信指标程序化交易自动交易量化交易

免责声明： 程序仅供学习交流，仅用于模拟交易测试，

如果用于实盘交易，风险自担，请知晓程序可能存在不可预知的风险。

0.学习交流讨论 加群 威信： gupiao888nb

![Image text](https://raw.githubusercontent.com/ak4stock/ths_tdx_stock_xueqiu_guoren/main/contact.png)  


1.先安装依赖 
pip install -r requirements

2.然后修改 run.py 里面的 client_path = 'C:/ths/xiadan.exe'

3.程序校验的token 看自己情况修改

4.需要发送通知 请配置自己的钉钉 dd_token 

python run.py 启动程序

python test.py 测试买卖下单查询等等

如果出现验证码 还需要安装OCR 参考easytrader文档 

感谢easytrader

https://easytrader.readthedocs.io/zh/master/#_4

可以部署在自己的服务器上，通过HTTP协议接口发送订单数据下单。


![Image text](https://raw.githubusercontent.com/ak4stock/ths_auto_trade/main/run.png)  

![Image text](https://raw.githubusercontent.com/ak4stock/ths_auto_trade/main/test.png)  


