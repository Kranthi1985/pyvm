import logging
class logger(object):
	def __init__(self):
		logging.basicConfig(level=logging.INFO)
		self.logObj = logging.getLogger(__name__)
	
	def logInfo(self,info):
		self.logObj.info(info)
	
	def logError(self,info):
		self.logObj.error(info)
		
	def logWarn(self,info):
		self.logObj.warn(info)
		
	def logDebug(self,info):
		self.logObj.debug(info)
