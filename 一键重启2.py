import paramiko,time

class baseconnect(object):
	def __init__(self,ip,user,passw,searchcom,searchvalue,startcom,stopcom,description):
		self.ip= ip
		self.user = user
		self.passw = passw
		self.searchcom =searchcom
		self.searchvalue = searchvalue
		self.startcom = startcom
		self.stopcom =stopcom
		self.description = description
		self.ssh = paramiko.SSHClient()
	def connect(self):
		trans = paramiko.Transport((self.ip, 22))
		try:
			trans.connect(username=self.user, password=self.passw)
		except:
			return False
		self.ssh._transport = trans
		return True
	def close(self):
		self.ssh.close()
	def _getstatus(self):
		stdin, stdout, stderr = self.ssh.exec_command(self.searchcom,timeout=5)
		stoutstr = str(stdout.read())
		# print('获取状态，stdout：',stoutstr)
		# print('获取状态，stderro：',stderr.read())
		if self.searchvalue in stoutstr:
			return True
		else:
			return  False
	def startup(self,timeout = 5):
		if self._getstatus():
			return '服务器{0}:服务{1}已经启动'.format(self.ip,self.description)
		else:
			try:
				stdin, stdout, stderr = self.ssh.exec_command(self.startcom,timeout)
				#outstr = str(stdout.read())

			except Exception :
				pass
		count = 0
		while True:
			a = self._getstatus()
			if count < 15 and not a :
				count +=1
				time.sleep(1)
			else:
				if a:
					return '服务器{0}:服务{1}启动成功'.format(self.ip, self.description)
					#print('服务器{0}:服务{1}启动成功'.format(self.ip, self.description))
				else:
					return '服务器{0}:服务{1}启动失败'.format(self.ip, self.description)
					#print('服务器{0}:服务{1}启动失败'.format(self.ip, self.description))
	def stop(self):

		stdin, stdout, stderr = self.ssh.exec_command(self.stopcom)
		outstr = str(stdout.read())
		# print('关闭服务stdout',outstr)
		# print('关闭服务stderror',stderr.read())
		if not self._getstatus():
			return '服务器{0}:服务{1}关闭成功'.format(self.ip, self.description)
		else:
			return '服务器{0}:服务{1}关闭失败'.format(self.ip, self.description)
	def getstatus(self):
		if self._getstatus():
			return '服务器{0}:服务{1}已启动'.format(self.ip, self.description)
		else:
			return '服务器{0}:服务{1}已停止'.format(self.ip, self.description)


