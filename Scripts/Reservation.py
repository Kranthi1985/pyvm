reserve_decision = raw_input("Do you want reserve the setup(yes/no): ")
print reserve_decision
if "yes" in reserve_decision:
	uName = raw_input("Please enter your username to reserve setup: ")
	fh = open("reservation/reserve.txt" , "w")
	fh.write("Setup reserved for: "+uName)
	fh.close()
else:
	print "Bye!!!"
	
