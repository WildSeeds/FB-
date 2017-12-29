from 一键重启.一键重启2 import baseconnect
from 一键重启.userinfo import dictuser

# fbinfo = dictuser['fb']
#fbinfo = dictuser['tq']
#fbinfo = dictuser['tqmc']
#fbinfo = dictuser['oracle']
fbinfo = dictuser['oraclelisten']
# print(fbinfo)
fbobj = baseconnect(fbinfo[0],fbinfo[1],fbinfo[2],fbinfo[3],fbinfo[4],fbinfo[5],fbinfo[6],fbinfo[7])
if fbobj.connect():
	fbobj.stop()
	fbobj.startup()

else:
	print('连接失败')