

dictuser = dict()
ip = '192.168.70.237'
passw = 'Zgcs3b@9ld'
#th中间件
user = 'fb'
searchcom="ps aux|grep hsserver|grep oracle.xml|grep -v grep|awk '{print $15}'"
searchvalue ='oracle.xml'
startcom = 'cd ~;source .bash_profile;cd workspace;sh runoracle>null'
stopcom = 'cd ~;source .bash_profile;cd workspace;sh stoporacle'
description = 'th中间件'

dictuser['fb'] = [ip,user,passw,searchcom,searchvalue,startcom,stopcom,description]

#tq中间件
user = 'tq'
searchcom="ps aux|grep hsserver|grep tq.xml|grep -v grep|awk '{print $15}'"
searchvalue = 'tq.xml'
startcom = 'cd ~;source .bash_profile;cd workspace;sh runtq>null'
stopcom = 'cd ~;source .bash_profile;cd workspace;sh stoptq'
description = 'tq中间件'
dictuser['tq'] = [ip,user,passw,searchcom,searchvalue,startcom,stopcom,description]

#tq消息中心
user = 'tqmc'
searchcom="ps aux|grep hsserver|grep tqmc.xml|grep -v grep|awk '{print $15}'"
searchvalue = 'tqmc.xml'
startcom = 'cd ~;source .bash_profile;cd workspace;sh runmc'
stopcom = 'cd ~;source .bash_profile;cd workspace;sh stopmc'
description = 'tq消息中心'
dictuser['tqmc'] = [ip,user,passw,searchcom,searchvalue,startcom,stopcom,description]

# oracle数据库
user = 'oracle'
searchcom = 'ps -ef|grep ora_dbw0_orcl|grep -v grep'
searchvalue = 'oracle'
startcom = '''
	source .bash_profile;sqlplus / as sysdba <<EOF
	startup
	EOF
	'''
stopcom = '''
	source .bash_profile;sqlplus / as sysdba <<EOF
	shutdown immediate
	EOF
	'''
description = 'oracle'
dictuser['oracle'] = [ip,user,passw,searchcom,searchvalue,startcom,stopcom,description]


# oracle数据库监听
user = 'oracle'
searchcom = 'source .bash_profile;lsnrctl status|grep Instance'
searchvalue = 'orcl'
startcom = 'source .bash_profile;lsnrctl start'
stopcom = 'source .bash_profile;lsnrctl stop'
description = 'oracle数据库监听'
dictuser['oraclelisten'] = [ip,user,passw,searchcom,searchvalue,startcom,stopcom,description]

#tomcat
user = 'fb'
searchcom = 'ps -ef | grep tomcat | grep -v grep'
searchvalue = 'tomcat'
startcom = '''
source .bash_profile;
if [ -d apache-tomcat-7.0.40 ];
then
cd apache-tomcat-7.0.40/bin;
else
cd apache-tomcat-6.0.43/bin;
fi
sh startup.sh'''
stopcom = '''
source .bash_profile;
if [ -d apache-tomcat-7.0.40 ];
then
cd apache-tomcat-7.0.40/bin;
else
cd apache-tomcat-6.0.43/bin;
fi
sh shutdown.sh
sleep 1
TOM_HOME=tomcat
echo $TOM_HOME
ps -ef | grep $TOM_HOME | grep -v grep | grep -v  kill
if [ $? -eq 0 ];then
	echo 'kill - 9' `ps -ef | grep $TOM_HOME | grep -v grep | grep -v  kill | awk '{print $2}'`
	kill -9 `ps -ef | grep $TOM_HOME | grep -v grep | grep -v  kill | awk '{print $2}'`
else
	echo $TOM_HOME 'Not found Process!'
fi'''
description = 'tomcat'
dictuser['tomcat'] = [ip,user,passw,searchcom,searchvalue,startcom,stopcom,description]

