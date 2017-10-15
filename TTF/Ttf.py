#Import Module
import os,sys,re
currentPath = os.path.dirname(os.path.abspath(__file__))
addPath = os.path.split(currentPath)[0]
print addPath
sys.path.append(addPath)
import getopt
import sys,os
import subprocess
from Tests.Lib.log import logger

#creating objects 
log = logger()


def main():
	subprocess.call("clear")
	###Declare global variables
	vcenterIp = ""
	tName = ""
	sName = ""
	rUser = ""
	opts = []
	args = ""
	flag = 0
	try:
		opts,args = getopt.getopt(sys.argv[1:], "v:t:s:r:v:h", ["vcenterIp=", 
																  "tcName=",
																  "suiteName=",
																  "reservationUser=",
																  "vcCfgFile=",
																  "help"])
	except getopt.GetoptError as err:
		log.logError(str(err)) # will print something like "option -a not recognized"
		sys.exit()
	if len(opts) == 0:
		usage()
	for option in opts:
		try:
			if "vcenterIp" in option[0] :
				vcenterIp = option[1]
			elif "tcName" in option[0]:
				tName = option[1]
			elif "suiteName" in option[0]:
				sName = option[1]
			elif "reservationUser" in option[0]:
				rUser = option[1]
			elif "vcCfgFile" in option[0]:
				vcFile = option[1]
			elif "help" in option[0]:
				flag = 1
				

		except:
			print "Something went wrong"
			
	#Validating the ip
	if flag == 1:
		usage()
		sys.exit()
		
	if not vcenterIp or not tName or not rUser:
		log.logError("Please Enter valid command line parameters")
		usage()		
		sys.exit()
	validationIp(vcenterIp)
	reservationValidation(rUser)
			
def usage():
	print "\n"
	print "################################################################"
	print "#      --vcenterIp*       = vcenterIp                          #"
	print "#      --tcName*          = testcasename                       #"
	print "#      --suiteName        = testsuitname                       #"
	print "#      --vcCfgFile        = Vcenter configuration file         #"
	print "#      --reservationUser* = username                           #"
	print "#      --help                                                  #"
	print "################################################################" 
	
	
	print "python Ttf.py --vcenterIp <ip> --tcName <testcase name> --suiteName <suitename> --vcCfgFile <Vccfgfile> --reservationUser <Username>"
	print "\n"
def validationIp(ip):
	log.logInfo("Performing health check for ip: " + ip)
	ping = subprocess.Popen(['ping', '-c 2', ip], stdout=subprocess.PIPE)
	pingResult = ping.communicate()[0]
	if "64 bytes from " in pingResult:
		log.logInfo("Health check done for ip: " + ip)
	else:
		log.logError("health check failed for ip: " + ip)
		sys.exit()

def reservationValidation(user):
	log.logInfo("Validating reservation user")
	try:
		fh = open (addPath+"Scripts/reservation/reserve.txt","rw")
		line = fh.readline()
		if user not in line or not line:
			log.logError("Setup is reserved for " + reservationUser + 
					"rerve with your name by using Reseravation.py utility ")
		fh.close()
	except (OSError, IOError) as e:
		log.logError(e)
		log.logError("Setup reserve with your name")
	
	
if __name__ == "__main__":
	main()