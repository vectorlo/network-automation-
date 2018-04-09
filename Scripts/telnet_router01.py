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
tn.write(b"int l0\n")
tn.write(b"ip addr 1.1.1.1 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
