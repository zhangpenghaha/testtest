import time

from aip import AipSpeech


"""APPID  AK  SK
tex 	String 	合成的文本，使用UTF-8编码，
请注意文本长度必须小于1024字节 	是
cuid 	String 	用户唯一标识，用来区分用户，
填写机器 MAC 地址或 IMEI 码，长度为60以内 	否
spd 	String 	语速，取值0-15，默认为5中语速 	否
pit 	String 	音调，取值0-15，默认为5中语调 	否
vol 	String 	音量，取值0-15，默认为5中音量 	否
per 	String 	发音人选择, 0为女声，1为男声，
3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女 	否
"""
APP_ID = '16196385'
API_KEY = 'WxGRlVF08c8xe0ZhqqOkiiIx'
SECRET_KEY = 'iXuAerVj1XQG7opFDb1nfOOlUYrxF7bf'

def video():

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    # 文本地址
    with open("C:/Users/Administrator/Desktop/测试语音/购物车.txt", 'r',encoding='gbk') as f:
        list1 = f.read()
    result = client.synthesis(list1,'zh', 12, {'vol':5, "per":0})
    # 语音保存地址
    with open("C:/Users/Administrator/Desktop/测试语音/{}.mp3".format(time.strftime("%Y%m%d%H%M%S")), 'wb') as f:
        f.write(result)

if __name__ == "__main__":
    video()
