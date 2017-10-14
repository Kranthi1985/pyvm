import os,sys,re
import getopt
import sys,os
###Declare global variables
hName = ""
uName = ""
passwd = ""
tName = ""
sName = ""
opts = []
args = ""


def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "h:u:p:t:s:he", ["hostIp=", 
																  "userName=", 
																  "passWord=", 
																  "tcName=",
																  "suiteName",
																  "help"])
	except getopt.GetoptError as err:
		print str(err)  # will print something like "option -a not recognized"
		sys.exit()
	for option in opts:
		try:
			if "hostIp" in option[0]:
				hName = option[1]
			elif "userName" in option[0]:
				uName = option[1]
			elif "passWord" in option[0]:
				passwd = option[1]
			elif "tcName" in option[0]:
				tName = option[1]
			elif "suiteName" in option[0]:
				uName = option[1]
			elif "help" in option[0]:
				usage()
		except:
			print "Something missed"
			
def usage():
	print "################################################################"
	print "#      --hostIp = hostname/ip [str]                            #"
	print "#      --username = username [str]                             #"     
	print "#      --passWord = password [str]                             #"
	print "#      --tcName   = testcasename                               #"
	print "#      --suiteName   = testsuitname                            #"
	print "#      --help                                                  #"
	print "################################################################" 

if __name__ == "__main__":
	main()