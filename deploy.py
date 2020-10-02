#!/usr/bin/python
#
##############################################
'''
name: deploy.py
author : Shashank Kharel
email: shahsank.kharel@hms.com
date: 01/19/2019


This script uses WLST to perform deployment and restart JVM. Since Jython being used is old and doesnt support yaml, yaml config file has been converted to json dictionary using yaml2dict.py script. 
Jython 2.7
weblogic 12.1.3

'''

import wl
import os
import sys
import re
import ast
import json

from java.lang import System
from time import sleep

with open("app_endpoint.cfg", 'r') as configFile:
	Config=configFile.read()

masterConfig = ast.literal_eval(Config)

SSL_prefix = masterConfig["SSL_prefix"]
non_SSL_prefix = masterConfig["NON_SSL_prefix"]

'''
App name and environment needs to be passed as command line arguement

'''
APP_NAME = "IDM_iam_im"
ENV = "DEV"

app_endpoint_details = masterConfig[APP_NAME]
env = ENV.lower()

stackNum = masterConfig[APP_NAME]["admin_server_stack_num"]
stackOS = masterConfig[APP_NAME]["admin_server_os"].lower()
stackDomain = masterConfig[APP_NAME]["admin_server_domain"].lower()
stackSuffix = masterConfig[APP_NAME]["admin_server_suffix"].lower()
artifactFullName = masterConfig[APP_NAME]["name"]
jvmTargetName = masterConfig[APP_NAME]["environment"][ENV]["jvm_target"]
artifactName = os.path.splitext(artifactFullName)[0]
artifactExtention = os.path.splitext(artifactFullName)[-1][1:]
SSL_port = int(str(SSL_prefix) + str(stackNum))
non_SSL_port = int(str(non_SSL_prefix) + str(stackNum))
wlConfigFile = '/home/cascm/wlsecurity/DevUserConfig.secure'
wlKeyFile = '/home/cascm/wlsecurity/DevUserKey.secure'

if stackOS == 'linux':
	stackPrefix = 'l'
elif stackOS == 'Windows':
	stackPrefix = 'w'
else:
	print("Unsupported OS, please check and retry")

if env == "dev":
	envltr = 'd'
elif env == "test":
	envltr = 't'
elif env == "prod":
	envltr = 'p'
else:
	print("Unsupported environment, please check app_endpoint.yml and retry")


adminServerURL = "t3://" + stackPrefix + envltr + stackSuffix + str(stackNum) + "." + stackDomain + ":" + str(non_SSL_port)
ssladminServerURL = "t3s://" + stackPrefix + envltr + stackSuffix + str(stackNum) + "." + stackDomain + ":" + str(SSL_port)

print(adminServerURL)
print(ssladminServerURL)


wl.connect(userConfigFile=wlConfigFile,userKeyFile=wlKeyFile,url=ssladminServerURL)
wl.redirect('temp.txt','False')
wl.listApplications()
wl.stopRedirect()

my_file = open('temp.txt','r')
appList = my_file.readlines()[:-1]
my_file.close
appList = [x[:-1] for x in appList]
appList = [x[1:] for x in appList]
os.remove("temp.txt")


if artifactName in appList:
  print("Deployment found")
  #initiate stop app
  #initiate undeploy
  #write function to deploy and restart called deploy_app()
else:
  print("No deployment found")
  # call deploy_app()


# match the app with the list and find if its deployed


print("\n")
wl.disconnect()


# Enhancements
# there should be an option to (un)deploy from 1 or multiple targets depending on command line arguement
# there should be option to set deployment order
