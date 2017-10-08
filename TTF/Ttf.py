import os,sys,re
import getopt

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "h:u:p:he", ["hostName=", "userName=", "passWord=", "help"])
	except getopt.GetoptError as err:
		print str(err)  # will print something like "option -a not recognized"
	print opts
	for option in opts:
		print option
		# if "hostName" in option:
			
		# print option,value
		
def usage():
	print "################################################################"
	print "#      --hostName = hostname/ip [str]                          #"
	print "#      --username = username [str]                             #"     
	print "#      --passWord = password [str]                             #"
	print "#      --help                                              #"
	print "################################################################" 

if __name__ == "__main__":
	main()