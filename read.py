#!/bin/python3

import os;
server_list = open("/home/mkhan/ready","r")
for servers in server_list.readlines():
	ssh(servers)
server_list.close()
