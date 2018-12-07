#!/usr/bin/env python
# This code has been developed by Eduardo Marquez --- nose238@hotmail.com
import commands


txt_ctrlz = open("/var/www/html/centralizedConsole/web/centralizedConsole/ctrlz.txt", "r") # ip addresses which you want to be affected by changes
print("IP addresses will be modified: \
 " + str(len( open("/var/www/html/centralizedConsole/web/centralizedConsole/ctrlz.txt").readlines())))

ip_with_ssh_connection = len(open("/var/www/html/centralizedConsole/web/centralizedConsole/ipListSSH.txt").readlines() ) # ip addresses which have ssh connection


for ip_change in txt_ctrlz:
	txt_connection_ssh = open("/var/www/html/centralizedConsole/web/centralizedConsole/ipListSSH.txt", "r")
	print("************************************")
	print("Changes in : " + ip_change[:-1])
	counter = 1
	
	# compare ip addresses in changes.txt with ip addresses in ipListSSH.txt. If an IP is in both files, changes have been applied
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

			# Backup of the client's configuration is generated, then python2 is executed to apply changes 
			f = commands.getoutput("ssh "+userClient+"@"+ipAdClient+ " -p " + portClient + " ' if [ -d /backupCentralizedConsole ]; \
				then echo \"Enter to backup directory\"; \
				else echo \"backup does not exist\"; \
				fi; \
				rm -f /cf/conf/config.xml;    \
				cp  /backupCentralizedConsole/cfconf.xml /cf/conf/config.xml; \
				cp  /backupCentralizedConsole/conf.xml /conf/config.xml ; \
				rm  -f /tmp/config.cache ; ' ")
			print(f)
			print("backup applied....... DONE")
		elif counter == int(ip_with_ssh_connection):
			print(str(ip_change[:-1]) + " Has no ssh connection. It isn't possible to apply Changes")
			txt_connection_ssh.close()
			break
		counter += 1
