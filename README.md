# ths_auto_trade

股票A股同花顺trade通达信指标程序化交易自动交易量化交易 

免责声明： 程序仅供学习交流，请先用模拟账户进行测试，

如果用于实盘交易，风险自担，请知晓程序可能存在不可预知的风险。

0.学习交流讨论 加群 威信： gupiao888nb 

![Image text](https://raw.githubusercontent.com/ak4stock/ths_tdx_stock_xueqiu_guoren/main/contact.png)  


2022.11.25更新

部分控件无法操作的

可以尝试替换pywin32依赖的版本

版本如下

227,228,300,301,302,303,304,305


2022.09.09更新

增加接口文档 

增加POSTMAN接口导入文件 

需配置变量 {{BASE_URL}} 和 {{TOKEN}}再使用


更换新的验证码识别方式


已经部署测试服务器，需要测试的VX联系，一天仅限一人测试。



2022.08.05更新

注意： 无法输入验证码的问题


更新最新的easytrader

更新最新的同花顺官方客户端

找到python的.\Lib\site-packages\easytrader目录

用项目的grid_strategies.py替换目录下的即可



1.先安装依赖 
pip install -r requirements.txt

2.然后修改 run.py 里面的 client_path = 'C:/ths/xiadan.exe'

3.程序校验的token 看自己情况修改

4.需要发送通知 请配置自己的钉钉 dd_token 

*********** 请先启动同花顺软件，然后打开同花顺的委托程序

python run.py 启动程序

python test.py 测试买卖下单查询等等

如果出现验证码 还需要安装OCR 参考easytrader文档 

tesseract 安装及使用
https://blog.csdn.net/showgea/article/details/82656515

感谢easytrader

https://easytrader.readthedocs.io/zh/master/#_4

可以部署在自己的服务器上，通过HTTP协议接口发送订单数据下单。


![Image text](https://raw.githubusercontent.com/ak4stock/ths_auto_trade/main/run.png)  

![Image text](https://raw.githubusercontent.com/ak4stock/ths_auto_trade/main/test.png)  



如果对你有所帮助，赏杯咖啡

![Image text](https://raw.githubusercontent.com/ak4stock/ths_auto_trade/main/code.jpg)

万一免五开户

![Image text](https://raw.githubusercontent.com/ak4stock/ths_auto_trade/main/%E4%B8%87%E4%B8%80%E5%85%8D%E4%BA%94%E5%BC%80%E6%88%B7.PNG)

