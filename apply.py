import commands

txt_changes = open("/home/software/scriptsSoporte/centosFiles/CAMILO.txt", "r")


print("IP addresses will be modified: \
 " + str(len( open("/home/software/scriptsSoporte/centosFiles/CAMILO.txt").readlines())))
ip_with_ssh_connection = len(open("/home/software/scriptsSoporte/centosFiles/ipListSSH.txt").readlines() ) # ip addresses which have ssh connection


for ip_change in txt_changes:
	txt_connection_ssh = open("/home/software/scriptsSoporte/centosFiles/ipListSSH.txt", "r")
	print("************************************")
	print("Changes in : " + ip_change[:-1])
	counter = 1
	
	for line in txt_connection_ssh:
		ipAdClient = line.partition("|")[0]
		if str(ip_change[:-1]) == str(ipAdClient):
			#################   APPLY CHANGES   ##################
			# Read client data
			ipAdClient = line.partition("|")[0]
			temp       = line.partition("|")[2]
			userClient = temp.partition("|")[0]
			temp       = temp.partition("|")[2]
			portClient = temp.partition("|")[0][:len(temp.partition("|")[0])-1]
			print("IP: " + ipAdClient + "	USER: " +  userClient + "	PORT: " + portClient)
			print(str(ip_change[:-1]) + " have SSH connection. DO ALL STUFF")
			# Applying changes in each warrior
			f = commands.getoutput("ssh "+userClient+"@"+ipAdClient+ " -p " + portClient + " ' if [ -d /backupCentralizedConsole ]; \
				then echo \"Enter to backup directory\"; \
				else mkdir /backupCentralizedConsole; echo \"backup directory generated\"; \
				fi; \
				cp /cf/conf/config.xml /backupCentralizedConsole/cfconf.xml ; \
				cp /conf/config.xml /backupCentralizedConsole/conf.xml ; ' ")
			print("Generate backup ...... DONE")
			f = commands.getoutput("ssh "+userClient+"@"+ipAdClient + " -p " +portClient +" 'rm -f /cf/conf/config.xml ;  rm -f /conf/config.xml ;'  " )
			print("Delete file in /cf/conf/config.xml & /conf/config.xml...... DONE")
			f = commands.getoutput("scp -P "+portClient+" /home/software/scriptsSoporte/centosFiles/pf.xml "+userClient+"@"+ipAdClient+":/cf/conf/config.xml")
			print("Copy in /cf/conf/config.xml & /conf/config.xml...... DONE")
			f = commands.getoutput("ssh "+userClient+"@"+ipAdClient+ " -p " + portClient + "  ' rm -f /tmp/config.cache'  " )
			print("Delete cache ...... DONE")
			print("Changes has successfully been applied in: " + ipAdClient + "\n\n\n")
			txt_connection_ssh.close()
			break
		elif counter == int(ip_with_ssh_connection):
			print(str(ip_change[:-1]) + " Has no ssh connection. It isn't possible to apply Changes")
			txt_connection_ssh.close()
			break
		counter += 1






				







	
	

	# for ip_with_ssh in txt_connection_ssh:
	# 	if str(ip_change) == str(ip_with_ssh):
	# 		print(str(ip_change[:-1]) + "have connection. DO ALL STUFF")
	# 		#################APPLY CHANGES##################
	# 			##read client data
	# 		txt = open("/home/software/scriptsSoporte/centosFiles/userClient.txt", "r")
	# 		userClient = txt.read()
	# 		userClient = userClient[:len(userClient)-1]
	# 		txt.close()
	# 		ipClient = ip_change [:len(ip_change)-1]
	# 		txt = open("/home/software/scriptsSoporte/centosFiles/portClient.txt", "r")
	# 		portClient = txt.read()
	# 		portClient = portClient[:len(portClient)-1]
	# 			#applying changes in each warrior
	# 		f = commands.getoutput("ssh "+userClient+"@"+ipClient+ " ' if [ -d /backupCentralizedConsole ]; \
	# 				then echo \"Enter to backup directory\"; \
	# 				else mkdir /backupCentralizedConsole; echo \"backup directory generated\"; \
	# 				fi; \
	# 				cp /cf/conf/config.xml /backupCentralizedConsole/cfconf.xml ; \
	# 				cp /conf/config.xml /backupCentralizedConsole/conf.xml ;' ")
	# 		print("Generate backup ...... DONE")
	# 		f = commands.getoutput("ssh "+userClient+"@"+ipClient + " 'rm -f /cf/conf/config.xml ;  rm -f /conf/config.xml ;'  " )
	# 		print("Delete file in /cf/conf/config.xml & /conf/config.xml...... DONE")
	# 		f = commands.getoutput("scp /home/software/scriptsSoporte/centosFiles/pf.xml "+userClient+"@"+ipClient+":/cf/conf/config.xml")
	# 		f = commands.getoutput("scp /home/software/scriptsSoporte/centosFiles/pf.xml "+userClient+"@"+ipClient+":/conf/config.xml")
	
	# 		print("Copy in /cf/conf/config.xml & /conf/config.xml...... DONE")
	# 		f = commands.getoutput("ssh "+userClient+"@"+ipClient+ "  ' rm -f /tmp/config.cache'  " )
	# 		print("Delete cache ...... DONE")
	# 		print("Changes has successfully been applied in: " + ipClient + "\n\n\n")

	# 		print("Changes in " + userClient + "@" + ipClient + " -p " + portClient)
	# 		txt_connection_ssh.close()
	# 		break
	# 	elif counter == int(ip_with_ssh_connection):
	# 		print(str(ip_change[:-1]) + " Has no ssh connection. It isn't possible to apply Changes")
	# 		txt_connection_ssh.close()
	# 		break
	# 	counter += 1
			
