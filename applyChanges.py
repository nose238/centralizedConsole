import commands

txt_ip_change = open("/home/software/scriptsSoporte/centosFiles/CAMILO.txt", "r")


for ip in txt_ip_change:
	txt_ip_no_SSH = open("/home/software/scriptsSoporte/centosFiles/ipListNoSSH.txt", "r")
	print("Trying to apply changes to " + ip)

	temp = open("/home/software/scriptsSoporte/centosFiles/ipListNoSSH.txt", "r") # use to count lines
	lines = len(list(temp)) # use to count lines



	counter = 1 # use to know how many IP's are in TXT
	for noSSH in txt_ip_no_SSH:
		if ip == noSSH:
			print("This ip has no ssh connection. Changes has not been applied")
			break
		elif counter == lines:
			txt = open("/home/software/scriptsSoporte/centosFiles/userClient.txt", "r")
			userClient = txt.read()
			userClient = userClient[:len(userClient)-1]
			ipClient = ip[:len(ip)-1]
			txt.close()
			txt = open("/home/software/scriptsSoporte/centosFiles/portClient.txt", "r")
			portClient = txt.read()
			portClient = portClient[:len(portClient)-1]
			f = commands.getoutput("scp /home/software/scriptsSoporte/centosFiles/pf.xml "+userClient+"@"+ipClient+":")
			print(f + "Changes has been applied\n\n\n")
		counter += 1 # use to know how many IP's are in TXT
	txt_ip_no_SSH.close()		
txt_ip_change.close()