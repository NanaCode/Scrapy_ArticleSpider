# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2017/8/21 15:02'

from zheye import zheye
z = zheye()
positions = z.Recognize('captcha-cn.gif')
print(positions)