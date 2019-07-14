from aip import AipOcr
"""百度文字识别接口
    APPID  AK  SK
"""
APP_ID = '16241205'
API_KEY = 'GNuO8wX03YEwa3E9s45FXFpW'
SECRET_KEY = 'DaO0yj17LWW4RS2iufDPUVW5OjFjCTf6'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_content():
    image = get_file_content('./screen.png')

    """ 调用通用文字识别, 图片参数为本地图片 """
    data = client.basicGeneral(image)
    # 打印识别出来的结果字典
    # print(data)
    # 从字典中取出结果
    image_content = ""
    for words in data['words_result']:
        print(words["words"])
        image_content += words['words']
    with open("./mytext", "w") as f:
        f.write(image_content)
    print(image_content)

if __name__ == "__main__":
    get_content()