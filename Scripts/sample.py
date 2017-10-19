#!/usr/bin/python
import sys
d={}
def main():
	try:
		datacenter_count = int(raw_input("How many datacenters you want[1-3]:"))
	except ValueError,UnboundLocalError:
		print "Please enter the valid input"
		sys.exit()
	if datacenter_count >=1 and  datacenter_count <= 3:
		datacenter(datacenter_count)
	else :
		print "Please select datacenters upto 3"
		sys.exit()
def datacenter(datacenter_count):
	for i in range(1,datacenter_count+1):
		datacenter_name = raw_input("Please enter the datacenter name for datacenter "+str(i)+":") or "dc"+str(i)
		d[datacenter_name]={}
	cluster_check = raw_input("Do you want clusters in  [yes/no]")
	if "yes" in cluster_check: 
		if (datacenter_count==3):
			default_cluster_count = 0
			for dcName in d.keys():
				clustername = raw_input("enter cluster name for "+dcName+":" ) or "cluster"+str(default_cluster_count)
				d[dcName][clustername]={}
				default_cluster_count+=1
		elif(datacenter_count==2):
			#cluster_number = int(raw_input("How many clusters you want : "))
			if (cluster_number >=1 and  cluster_number <= 3):
				for dcName in d.keys():
					print "hi"
					cluster_number = int(raw_input("How many clusters you want in : "+dcName+":"))
					for j in range(cluster_number):
						clustername = raw_input("enter cluster name for "+dcName+":" ) or "cluster"+j
					
		elif(datacenter_count==1):
			for dcName in d.keys():
				cluster_number = int(raw_input("How many clusters you want in : "+dcName+":'))
				if (cluster_number >=1 and  cluster_number <= 3):
					for j in range(cluster_number):
						clustername = raw_input("enter cluster name for "+dcName+":" ) or "cluster"+j
						d[dcName][clustername]={}
				else :
					pass
	elif  ( "no" in cluster_check ):
		host()
	else:
		print "you have selected wrong option please try again later"

def Cluster(dcName,cluster_number):
	for j in range(cluster_number):
		clustername=raw_input("please enter cluster name:"+dcName+":")	or "Cluster"+str(j)
		d[dcName][clustername]={}

def host():
	print "calling host method"
if __name__ == "__main__":
	main()
