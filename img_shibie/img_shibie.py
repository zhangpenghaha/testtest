import keyboard
import time
from PIL import ImageGrab

from mytest.img_shibie.baidu_img import get_content

"""
1. 保存截图到本地
2. 识别本地图片
"""

def screen():
    # 截图F1 监控
    print("开始截图")
    # 阻塞程序运行
    keyboard.wait(hotkey="ctrl+alt+a")
    # 保存截图
    keyboard.wait(hotkey="ctrl+c")
    print("结束截图")
    time.sleep(0.5)
    image = ImageGrab.grabclipboard()
    image.save("screen.png")
    # print(image)
    get_content()


if __name__ == "__main__":
    while True:
        screen()