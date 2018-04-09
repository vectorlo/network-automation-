#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import telnetlib

HOST = "10.0.0.1"
user = input("Enter your username:")
password = getpass.getpass("password:")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")

for n in range(2,11):
    tn.write(b"'vlan %s\n' % n" )
    tn.write(b"'name Python_VLAN %s\n' % n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
