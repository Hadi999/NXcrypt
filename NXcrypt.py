#! /usr/bin/env python
#! coding : utf-8
""" usage :

sudo ./nxcrypt.py --file=file_to_encrypt 
sudo ./nxcrypt.py --file=file_to_encrypt --output=output_file
sudo ./nxcrypt.py --help 

"""

# modules
import sys
import py_compile
import optparse
import os
import commands
import time

_output_ = "backdoor.py" # edit this line is you want edit default output .
_byte_ = (_output_) + "c"

# if platform is linux and NXcrypt isn't launched  as root
if (sys.platform.startswith("linux")) :
	if (commands.getoutput("whoami")) != "root" :
		print ("run it as root")
		sys.exit() #exit
	else:
		pass
else:
    pass
    

#menu     
menu = """

d8b   db db    db  .o88b. d8888b. db    db d8888b. d888888b
888o  88 `8b  d8' d8P  Y8 88  `8D `8b  d8' 88  `8D `~~88~~'
88V8o 88  `8bd8'  8P      88oobY'  `8bd8'  88oodD'    88
88 V8o88  .dPYb.  8b      88`8b      88    88~~~      88
88  V888 .8P  Y8. Y8b  d8 88 `88.    88    88         88
VP   V8P YP    YP  `Y88P' 88   YD    YP    88         YP
                                        (python backdoor encryption tool)                                      
       """
menu_linux = "\033[32m" + (menu) + "\033[37m"
      
name = """
 -NXcrypt is a tool for bypass AV 
 -It encrypt python backdoors   and payloads in bytecode
 -author: Hadi tux (had3s)
 -only for penetration testing 
 
	   """
name_linux = "\033[31m" +  (name) + "\033[37m"

#options 
parser = optparse.OptionParser()
parser.add_option("--file", "-f", help="python file to encrypt ", action="store", dest="file")
parser.add_option("--output", "-o", help="output of crypted python file ", dest="out", action="store")
option , arg = parser.parse_args()
if not option.file :
	parser.error("file to encrypt hasn't given type --help for help ")
	sys.exit()
elif  option.file :
	payload = (option.file)
	
	if not option.out :
		if (sys.platform.startswith("linux")) :
			print (menu_linux)
			print ("")
			print (name_linux)
		else:
			print (menu)
			print ("")
			print (name)
			
		try:
			py_compile.compile(payload, cfile=_byte_, dfile=None, doraise=False, ) #compilation
		except (py_compile.PyCompileError,IOError,TypeError) :
			sys.exit("encryption error :  file  {} don't exist or it's already crypted ".format(option.file)) #error
		print ("[*] file : {}".format(option.file))
		print ("[*] default output : {}".format(_output_))
		if (sys.platform.startswith("linux"))  :
			os.system(" mv  {} {} ".format(_byte_,_output_))

		elif (sys.platform.startswith("windows")) :
			os.system(" rename {} {} ".format(_byte_,_output_))
			
		elif (sys.platform.startswith("darwin")):
			os.system(" mv {}  {} ".format(_byte_,_output_))
		print ("[+] encryption finished  100% ")
		print time.strftime('[*] time : %H:%M ',time.localtime()) 
		print time.strftime('[*] date :%d/%m/%y ',time.localtime())
		print ("[+] file : {} ".format(_output_))
	elif option.out  :
		output = option.out
		bytecode = (option.out) + "c"
		if (sys.platform.startswith("linux")) :
			print (menu_linux)
			print ("")
			print (name_linux)
		else:
			print (menu)
			print ("")
			print (name)
		print ("[*] file : {}".format(option.file))
		print ("[*] output : {}".format(output))
		try :
			py_compile.compile(payload, cfile=bytecode, dfile=None, doraise=False, ) #compilation
		except (py_compile.PyCompileError,IOError,TypeError) :
			sys.exit("encryption error : file don't exist or it's already crypted ")
		if (sys.platform.startswith("linux")):
			os.system("mv {}  {} ".format(bytecode,output))
		elif (sys.platform.startswith("windows")):
			os.system("rename {}  {} ".format(bytecode,output))
		elif (sys.platform.startswith("darwin")):
			os.system("mv {}  {} ".format(bytecode,output))	
		print ("[+] encryption finished 100% ")
		print time.strftime('[*] time : %H:%M ',time.localtime()) 
		print time.strftime('[*] date :%d/%m/%y ',time.localtime())
		print ("[*] file : {} ".format(output))	
