# NXcrypt

NXcrypt is a polymorphic 'python backdoors' crypter written in python by Hadi Mene (h4d3s) .
The output  is fully undetectable .

- In Linux , run it as root
- NXcrypt encrypted output is 99% FUD 

# Usage :

- sudo  ./NXcrypt.py --file=backdoor.py --output=output_backdoor.py # encrypt backdoor.py and output file is output_backdoor.py
- sudo ./NXcrypt.py --file=shell.py # encrypt shell.py and default output file  is backdoor.py but you can edit it in source code
 -sudo ./NXcrypt.py --help # NXcrypt help
 
 # How it work ? 
 
 - NXcrypt add some junkcode .
 - NXcrypt use a python internal module 'py_compile' who compile the code into bytecode to a .pyc file .
 - NXcrypt convert .pyc file into normal .py file .
 - And with this way we can obfuscate the code
 - The md5sum will change too
 
 
 # Test with Virustotal
 
 Before :
 
SHA256:	e2acceb6158cf406669ab828d338982411a0e5c5876c2f2783e247b3e01c2163
File name:	facebook.py
Detection ratio:	2 / 54

After :

SHA256:	362a4b19d53d1a8f2b91491b47dba28923dfec2d90784961c46213bdadc80add
File name:	facebook_encrypted.py
Detection ratio:	0 / 55


# Credits

All Credits go to Suspicious Shell Activity team
 
 
 


 
