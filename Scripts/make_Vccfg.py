#!/usr/bin/python
print "###############################################"
d={}
def main():
	flag =0
	datacenter_count = int(raw_input("How many datacenters you want[1-3]:"))
	if datacenter_count >=1 and  datacenter_count <= 3:
		datacenter(datacenter_count)
	else :
		print "Please select datacenters upto 3"
		exit()
		
	print d
def datacenter(datacenter_count):
	for i in range(1,datacenter_count+1):
		print i
		datacenter_name = raw_input("Please enter the datacenter name for datacenter "+str(i)+":") or "ds"+str(i)
		print datacenter_name
		if datacenter_name:
			d[datacenter_name]={}
	for dcName in sorted(d.keys()):
		cluster_check = raw_input("Do you want clusters in Dtacenter "+dcName+":")
		if (cluster_check == "yes" or "y" or "Yes" or "YES" or "Y"):
			Cluster(dcName)
		else:
			pass
	#print d

def Cluster(dcName):
    #clustername=raw_input("please enter cluster name:")	or 	"Cluster"
	#d[dcName][clustername]={}
	pass
if __name__ == "__main__":
	main()