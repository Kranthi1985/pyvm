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
		opts, args = getopt.getopt(sys.argv[1:], "h:u:p:t:s:he", ["hostName=", 
																  "userName=", 
																  "passWord=", 
																  "tcName=",
																  "suiteName",
																  "help"])
	except getopt.GetoptError as err:
		print str(err)  # will print something like "option -a not recognized"
		sys.exit()
	for option in opts:
		print type(list(option))
		try:
			if "hostName" in option[0]:
				

def usage():
	print "################################################################"
	print "#      --hostName = hostname/ip [str]                          #"
	print "#      --username = username [str]                             #"     
	print "#      --passWord = password [str]                             #"
	print "#      --tcName   = testcasename                               #"
	print "#      --suiteName   = testsuitname                            #"
	print "#      --help                                                  #"
	print "################################################################" 

if __name__ == "__main__":
	main()