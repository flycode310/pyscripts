# coding=utf-8
'''
author : chen
2014/10/15
'''
import os

# the required libs
soot = 'soot-trunk.jar:'
sootInfoflow = 'soot-infoflow.jar:'
sootInflowAndroid = 'soot-infoflow-android.jar:'
slf4jApi = 'slf4j-api-1.7.5.jar:'
#slf4jSimple = 'slf4j-simple-1.7.5.jar;'
slf4jSimple = ''
axml = 'axml-2.0.jar'

# the parameters of the cmd
classpath = soot + sootInfoflow + sootInflowAndroid + slf4jApi + slf4jSimple + axml
mainclass = 'soot.jimple.infoflow.android.TestApps.Test'
apkPath = '/opt/apks/网易新闻.apk'
platforms = '/opt/adt-bundle-linux-x86_64-20140702/sdk/platforms'

# the cmd string
cmdString = 'java -cp ' + classpath + ' ' + mainclass + ' ' + apkPath + ' ' + platforms

os.system(cmdString)
