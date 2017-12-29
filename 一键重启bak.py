import paramiko
# 实例化一个transport对象
ip = '192.168.70.237'
ssh = paramiko.SSHClient()

def gettransport(user):
	trans = paramiko.Transport((ip, 22))
	if user == 'fb':
		# 建立FB用户连接
		trans.connect(username='fb', password='Zgcs3b@9ld')
	elif user == 'tq':
		# 建立tq用户连接
		trans.connect(username='tq', password='Zgcs3b@9ld')
	elif user =='tqmc':
		# 建立tqmc用户连接
		trans.connect(username='tqmc', password='Zgcs3b@9ld')
	elif user =='oracle':
		# 建立oracle用户连接
		trans.connect(username='oracle', password='Zgcs3b@9ld')
	ssh._transport = trans
def session(user):
	def decorator(func):
		def wrapper(*args,**kw):
			gettransport(user)
			try:
				func()
				ssh.close()
			except Exception as e:
				ssh.close()
				print(e)
		return wrapper
	return decorator

# 执行命令，和传统方法一样
#关闭服务
@session('fb')
def closethas():
	stdin, stdout, stderr = ssh.exec_command('source .bash_profile;sh workspace/stoporacle')
	stdin, stdout, stderr = ssh.exec_command("ps aux|grep hsserver|grep oracle.xml|grep -v grep|awk '{print $15}'")
	if stdout.read() == 'oracle.xml':
		raise Exception('服务器：{0}，关闭th中间件失败'.format(ip))
	else:
		print('服务器：{0}，关闭th中间件成功'.format(ip))
@session('tq')
def closetqas():
	stdin, stdout, stderr = ssh.exec_command('source .bash_profile;sh workspace/stoptq')
	stdin, stdout, stderr = ssh.exec_command("ps aux|grep hsserver|grep tq.xml|grep -v grep|awk '{print $15}'")
	if stdout.read() == 'tq.xml':
		raise Exception('服务器：{0}，关闭tq中间件失败'.format(ip))
	else:
		print('服务器：{0}，关闭tq中间件成功'.format(ip))

@session('tqmc')
def closetqmc():
	stdin, stdout, stderr = ssh.exec_command('source .bash_profile;sh workspace/stopmc')
	stdin, stdout, stderr = ssh.exec_command("ps aux|grep hsserver|grep tqmc.xml|grep -v grep|awk '{print $15}'")
	if stdout.read() == 'tqmc.xml':
		raise Exception('服务器：{0}，关闭tqmc消息中心失败'.format(ip))
	else:
		print('服务器：{0}，关闭tqmc消息中心成功'.format(ip))
@session('fb')
def closetomcat():
	stdin, stdout, stderr = ssh.exec_command('source .bash_profile;ls -d apache-tomcat*')
	error = stderr.read()
	if stderr:
		ssh.exec_command('source .bash_profile;sh apache-tomcat-6.0.43/bin/shutdown.sh')
	else:
		ssh.exec_command('source .bash_profile;sh apache-tomcat-7.0.40/bin/shutdown.sh')
	killstr='''
	TOM_HOME=tomcat
	echo $TOM_HOME
	ps -ef | grep $TOM_HOME | grep -v grep | grep -v  kill
	if [ $? -eq 0 ];then
		echo 'kill - 9' `ps -ef | grep $TOM_HOME | grep -v grep | grep -v  kill | awk '{print $2}'`
		kill -9 `ps -ef | grep $TOM_HOME | grep -v grep | grep -v  kill | awk '{print $2}'`
	else
		echo $TOM_HOME 'Not found Process!'
	fi
	'''
	for i in range(-1,3):
		if i ==3:
			raise Exception('服务器：{0}，关闭th中间件失败'.format(ip))
		stdin, stdout, stderr=ssh.exec_command(killstr)
		out = stdout.read()
		if 'Not found Process' in out:
			break
@session('oracle')
def closeoracle():
	closecommand = '''
	source .bash_profile;sqlplus / as sysdba <<EOF
	shutdown immediate
	EOF
	'''
	stdin, stdout, stderr = ssh.exec_command(closecommand)

	stdin, stdout, stderr = ssh.exec_command('ps -ef|grep ora_dbw0_orcl|grep -v grep')
	if 'oracle' not in  stdout.read():
		print('服务器：{0}，关闭Oracle成功'.format(ip))
	else:
		raise Exception('服务器：{0}，关闭Oracle失败'.format(ip))


def _getstatus(user):
	if user == 'fb':
		gettransport('fb')
		try:
			stdin, stdout, stderr = ssh.exec_command("ps aux|grep hsserver|grep oracle.xml|grep -v grep|awk '{print $15}'")
			if stdout.read() == 'oracle.xml':
				return True
			else:
				return False
		except Exception as e:
			ssh.close()
			print(e)
	elif user == 'tq'  :
		gettransport('tq')
		try:
			stdin, stdout, stderr = ssh.exec_command("ps aux|grep hsserver|grep tq.xml|grep -v grep|awk '{print $15}'")
			if stdout.read() == 'tq.xml':
				return True
			else:
				return False
		except Exception as e:
			ssh.close()
			print(e)
	elif user == 'tqmc':
		gettransport('tqmc')
		try:
			stdin, stdout, stderr = ssh.exec_command("ps aux|grep hsserver|grep tqmc.xml|grep -v grep|awk '{print $15}'")
			a = stdout.read()
			print(a)
			print(123)
			if 'tqmc.xml' in a:
				return True
			else:
				return False
		except Exception as e:
			ssh.close()
			print(e)
	elif user == 'oracle':
		# 建立oracle用户连接
		gettransport('oracle')
		try:
			stdin, stdout, stderr = ssh.exec_command('ps -ef|grep ora_dbw0_orcl|grep -v grep')
			if 'oracle' in stdout.read():
				return True
			else:
				return False
		except Exception as e:
			ssh.close()
			print(e)
	elif user == 'oraclelisten':
		gettransport('oracle')
		try:
			stdin, stdout, stderr = ssh.exec_command('source .bash_profile;lsnrctl start')
			if 'orcl' in stdout.read():
				return True
			else:
				return False
		except Exception as e:
			ssh.close()
			print(e)
	elif user == 'tomcat':
		gettransport('fb')
		try:
			stdin, stdout, stderr = ssh.exec_command('ps -ef | grep tomcat | grep -v grep')
			if 'tomcat'  in stdout.read():
				return True
			else:
				return False
		except Exception as e:
			ssh.close()
			print(e)
@session('oracle')
def openoracle():
	opencommand = '''
	source .bash_profile;sqlplus / as sysdba <<EOF
	startup
	EOF
	'''
	stdin, stdout, stderr = ssh.exec_command(opencommand)
	stdout.read()
	# print('stdout:',stdout.read())
	# print('stdout:',stderr.read())
	stdin, stdout, stderr = ssh.exec_command('ps -ef|grep ora_dbw0_orcl|grep -v grep')
	if 'oracle' in  stdout.read():
		print('服务器：{0}，开启Oracle成功'.format(ip))
	else:
		raise Exception('服务器：{0}，开启Oracle失败'.format(ip))
@session('oracle')
def openoraclelisten():
	stdin, stdout, stderr = ssh.exec_command('source .bash_profile;lsnrctl status|grep Instance')
	if 'orcl' in stdout.read():
		print('服务器：{0}，Oracle监听已启动'.format(ip))
	else:
		stdin, stdout, stderr = ssh.exec_command('source .bash_profile;lsnrctl start')
		if 'orcl' in stdout.read():
			print('服务器：{0}，开启oracle监听成功'.format(ip))
		else:
			raise Exception('服务器：{0}，开启Oracle监听失败'.format(ip))

@session('fb')
def openthas():
	stdin, stdout, stderr = ssh.exec_command('cd ~;source .bash_profile;cd workspace;sh runoracle')
	stdin, stdout, stderr = ssh.exec_command("ps aux|grep hsserver|grep oracle.xml|grep -v grep|awk '{print $15}'")
	print(stdout.read())
	if stdout.read() != 'oracle.xml':
		raise Exception('服务器：{0}，启动th中间件失败'.format({'ip':ip}))

@session('tq')
def opentqas():
	stdin, stdout, stderr = ssh.exec_command('source .bash_profile;sh workspace/runtq')
	stdin, stdout, stderr = ssh.exec_command("ps aux|grep hsserver|grep tq.xml|grep -v grep|awk '{print $15}'")
	if stdout.read() != 'tq.xml':
		raise Exception('服务器：{0}，启动tq中间件失败'.format({'ip':ip}))

@session('tqmc')
def opentqmc():
	stdin, stdout, stderr = ssh.exec_command('source .bash_profile;sh workspace/runmc')
	stdin, stdout, stderr = ssh.exec_command("ps aux|grep hsserver|grep tqmc.xml|grep -v grep|awk '{print $15}'")
	if stdout.read() == 'tqmc.xml':
		raise Exception('服务器：{0}，启动tqmc消息中心失败'.format(ip))
@session('fb')
def opentomcat():
	stdin, stdout, stderr = ssh.exec_command('source .bash_profile;ls -d apache-tomcat*')
	error = stderr.read()
	if stderr:
		ssh.exec_command('source .bash_profile;sh apache-tomcat-6.0.43/bin/startup.sh')
	else:
		ssh.exec_command('source .bash_profile;sh apache-tomcat-7.0.40/bin/startup.sh')
	stdin, stdout, stderr = ssh.exec_command('ps -ef | grep tomcat | grep -v grep')
	if 'tomcat' not in stdout.read():
		raise Exception('服务器：{0}，启动tomcat失败'.format(ip))

def printstatus(type):
	'''

	:param type: 1 tq，2th， 3 集成
	:return:
	'''
	if type not in (1,2,3):
		raise Exception('打印所有服务状态函数，输入参数不正确，type: 1 tq，2th， 3 集成')
	list = [('oracle','oraclelisten','tq','tomcat','tqmc'),('oracle','oraclelisten','fb','tomcat'),('oracle','oraclelisten','fb','tq','tomcat','tqmc')]
	listresult=dict()
	for i in list[type-1]:
		if _getstatus(i):
			listresult[i] = '1'
		else:
			listresult[i] = '0'
	print('已启动服务：')
	for key,value in listresult.items():

		if value=='1':
			print('-->服务器：{0}，{1}已启动'.format(ip,key))
	print('未启动服务：')
	for key,value in listresult.items():

		if value=='0':
			print('-->服务器：{0}，{1}未启动'.format(ip,key))

# closethas()
# closetqas()
# closetqmc()
# closetqas()
closeoracle()

openoracle()
# openoraclelisten()
openthas()
# opentqas()
# opentqmc()
# opentomcat()
# printstatus(3)

# 关闭连接
