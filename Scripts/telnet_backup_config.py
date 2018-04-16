#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import telnetlib

#Ask for usrname and password
user = input("Enter your username:")
password = getpass.getpass("password:")

#Telnet to swtichs and get the running config
with open("switchs_info.txt", "r") as f:
    for host in f:
        print("get running config from %s" % host )
        tn = telnetlib.Telnet(host)

        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")

        tn.write(b"enable\n")
        tn.write(b"cisco\n")
        tn.write(b"terminal lenth 0\n")
        tn.write(b"show run\n")
        tn.write(b"exit\n")
        
        readoutput = tn.read_all().decode('ascii')
        saveoutput = open("'%s.txt' % host", "w")
        saveoutput.write(readoutput)
        saveoutput.close()
        
        
            
