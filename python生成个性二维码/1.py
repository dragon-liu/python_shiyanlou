#-*- coding:utf-8 -*-

#本课程通过调用MyQR接口来实现生成个人所需二维码，并可以设置二维码的大小、是否在现有图片的基础上生成、是否生成动态二维码
#有关QR码详见https://blog.csdn.net/u012611878/article/details/53167009
from MyQR import myqr

#生成普通2维码
myqr.run('https://www.shiyanlou.com')

#生成图片2维码
myqr.run( words='https://www.shiyanlou.com',
picture='Sources/shiyanlouLogo.png',
save_name='artistic.png'
)

#生成彩色图片2维码
myqr.run( words='https://www.shiyanlou.com',
picture='Sources/shiyanlouLogo.png',
colorized=True,
save_name='artistic_Color.png'
)

#生成gakki的动态gif二维码
myqr.run(words = 'http://www.shiyanlou.com',
picture = 'H:/实验楼python练手项目/python生成个性二维码/Sources/gakki.gif',
colorized = True,
save_name = 'Animated.gif')