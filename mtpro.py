# 导入需要的库
import requests
import json

# 获取数据
response = requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/mtproto.json')

# 将获取的数据转换为Python列表
data = json.loads(response.text)

# 遍历列表
for item in data:
    # 取出每一项的host，port和secret
    host = item['host']
    port = item['port']
    secret = item['secret']
    
    # 生成对应的Telegram代理链接
    link = 'https://t.me/proxy?server={}&port={}&secret={}'.format(host, port, secret)
    
    # 打印生成的链接
    print(link)
    ```
    
    生成的tg代理，直接在tg点击就行，不过我也不知道如何测tg代理的速度
