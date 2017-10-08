from pyVim.connect import SmartConnect
import ssl
import os,sys

class vcenter(object):
	def __init__(self,ip,uName,passwd):
		self.ip = ip
		self.uName = uName
		self.passWord = passwd
	
	def connect(self,ip = self.ip, userName = self.uName, passwd = self.passWord)
		sslObj = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
		sslObj.verify_mode = ssl.CERT_NONE
		vcenterObj = SmartConnect(host=ip, user=userName, pwd=passwd, sslContext=sslObj)
		return vcenterObj
		
		