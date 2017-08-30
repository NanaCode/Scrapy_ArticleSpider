# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2017/8/21 8:44'

import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

# from PIL import Image

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
header = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhihu.com",
    "User-Agent": agent
}


def get_xsrf():
    # 获取xsrf code
    response = session.get("https://www.zhihu.com", headers=header)
    match_obj = re.match('.*name="_xsrf" value="(.*)"', response.text)
    if match_obj:
        print(match_obj.group(1))
    else:
        return ""

#     # 获取验证码
#     def get_captcha():
#
#     # t = str(int(time.time() * 1000))
#     # captcha_url = "https://www.zhihu.com/captcha.gif?r=%s&type=login
#
#     "%t
#     captcha_url = "https://www.zhihu.com/captcha.gif?&type=login
#
#
# "
#     captcha_image = session.get(captcha_url, headers=headers)
#     with open('captcha.gif', 'wb') as f:
#         f.write(captcha_image.content)
#         f.close()
#     try:
#         im = Image.open("captcha.gif")
#         im.show()
#         captcha = input("please input the captcha:")
#         im.close()
#     except:
#         print("未打开验证码文件")


def get_captcha():
    # import time
    # t = str(int(time.time()*1000))
    # captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
    captcha_url = "https://www.zhihu.com/captcha.gif?&type=login"
    t = session.get(captcha_url, headers=header)
    with open("captcha.jpg", "wb") as f:
        f.write(t.content)
        f.close()

    from PIL import Image
    try:
        im = Image.open('captcha.jpg')
        # im.save()
        im.show() #图片展示出来
        im.close()
    except:
        print("未打开验证码文件")



def zhihu_login(account, password):
    # 知乎登录
    if re.match("^1\d{10}", account):
        print("手机号码登陆")
        post_url = "https://www.zhihu.com/login/phone_num"
        # post_url = "https://www.zhihu.com / captcha.gif?&type=login"
        post_data = {
            "-xsrf": get_xsrf(),
            "password": password,
            # "captcha_type": "cn",
            "phone_num": account,
            "captcha": ""
        }

        response_text = session.post(post_url, data=post_data, headers=header)

        session.cookies.save()

# # get_xsrf()
# zhihu_login("13729496321", "xienanadada")

get_captcha()