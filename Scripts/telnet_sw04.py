#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import telnetlib

user = input("Enter your username:")
password = getpass.getpass("password:")

with open("switchs_info.txt", "r") as f:
    for host in f:
        tn = telnetlib.Telnet(host)

        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")

        tn.write(b"enable\n")
        tn.write(b"cisco\n")
        tn.write(b"conf t\n")

        for n in range(2,11):
            vlan = "vlan %s" % n
            desc = "name Python_VLAN%s" % n
            tn.write(vlan.encode('ascii') + b"\n")
            tn.write(desc.encode('ascii') + b"\n")

        tn.write(b"end\n")
        tn.write(b"exit\n")
        print(tn.read_all().decode('ascii'))
