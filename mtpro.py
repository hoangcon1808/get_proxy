# 导入需要的库
import requests
import json

# 获取数据 (请在下面的引号中填写有效的URL)
response = requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/mtproto.json')

# 检查请求是否成功
if response.status_code == 200:
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
else:
    print("Failed to retrieve data. Status code:", response.status_code)
