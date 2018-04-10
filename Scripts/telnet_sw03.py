#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import telnetlib


user = "cisco"
password = "cisco"

for n in range(1,11):
    host = "10.0.0.0 %s" % n
	tn = telnetlib.Telnet(HOST)

	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	if password:
    	tn.read_until(b"Password: ")
    	tn.write(password.encode('ascii') + b"\n")

	tn.write(b"enable\n")
	tn.write(b"cisco\n")
	for n in range(2,11):
    	vlan = "vlan %s" % n
    	desc = "name Python_VLAN %s" % n
    	tn.write(vlan.encode('ascii') + b"\n")
		tn.write(desc.encode('ascii') + b"\n")
	tn.write(b"end\n")
	tn.write(b"exit\n")
	
	print(tn.read_all().decode('ascii'))
