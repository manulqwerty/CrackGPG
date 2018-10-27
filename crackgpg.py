#!/usr/bin/python
import os
import gnupg
import argparse
import thread
import threading
import sys
import time
gnupg._parsers.Verify.TRUST_LEVELS["DECRYPTION_COMPLIANCE_MODE"] = 23 #https://github.com/isislovecruft/python-gnupg/issues/207
STARTTIME = time.time()
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
def print_header():
    print(color.BOLD + color.GREEN + '''
 _______  _______  _______  _______  _        _______  _______  _______ 
(  ____ \(  ____ )(  ___  )(  ____ \| \    /\(  ____ \(  ____ )(  ____ \\
| (    \/| (    )|| (   ) || (    \/|  \  / /| (    \/| (    )|| (    \/
| |      | (____)|| (___) || |      |  (_/ / | |      | (____)|| |      
| |      |     __)|  ___  || |      |   _ (  | | ____ |  _____)| | ____ 
| |      | (\ (   | (   ) || |      |  ( \ \ | | \_  )| (      | | \_  )
| (____/\| ) \ \__| )   ( || (____/\|  /  \ \| (___) || )      | (___) |
(_______/|/   \__/|/     \|(_______/|_/    \/(_______)|/       (_______)
                                                                        
                                                                       ''' + color.END + color.RED + '''by @manulqwerty 
                                                                       
''' + color.BLUE + color.BOLD + '''--------------------------------------------------------------------------------
''' + color.END)
def check_arguments():
    parser = argparse.ArgumentParser(description='GPG Cracker - By @manulqwerty from ironHackers.es')
    parser.add_argument('GPG_File', help='GPG symmetrically encrypted data',metavar='GPG_file',type=lambda x: is_valid_file(parser, x))
    parser.add_argument('Wordlist', help='Wordlist file (one pass per line)',metavar='Wordlist', type=lambda x: is_valid_file(parser, x))
    args = parser.parse_args()
    return args
    
def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error('The file {} does not exist!'.format(arg))
    else:
        # File exists so return the filename
        return arg    
    
def decrypt_file(gpg, encrypted_path,password,pass_num):
    with open(encrypted_path, 'rb') as a_file:
        status = gpg.decrypt_file(a_file, passphrase=password, output="gpg_output")
    if 'no valid OpenPGP data found' in status.stderr:
		print(color.BOLD + color.YELLOW  + '[+] Error: ' + encrypted_path + ' is not a valid OpenPGP data\n' + color.END)
		os._exit(1)
    if status.ok == True:
        pass_found(password,pass_num)
def pass_found(password,pass_num):
    percentage = 100*pass_num/size
    sys.stdout.write("\r")
    print(color.BOLD + color.PURPLE + 'Time elapsed: ' + str(round(time.time() - STARTTIME,2)) + 's - ' + str(pass_num) + '/' + str(size) + " (" + str(percentage)+ '%)' + color.END)
    print(color.BOLD + color.YELLOW + '[+] Password Found: ' + password + color.END)
    print(color.BOLD + color.YELLOW  + '[+] Output File: ' + "gpg_output" + color.END)
    os._exit(1)
if __name__ == '__main__':
    args = check_arguments()
    gpg = gnupg.GPG()
    file_name = args.GPG_File
    wordlist = args.Wordlist
    j = 1
    		
    f = open(wordlist, 'r')
    lines = f.read().splitlines()
    size=sum(1 for _ in lines)
    print_header()
    for i in lines:
        thread1 = threading.Thread(target=decrypt_file, args=[gpg,file_name,i,j,])
        thread1.start()
        time.sleep(0.04)
        percentage = 100*j/size
        sys.stdout.write("\r")
        sys.stdout.write(color.BOLD + color.PURPLE + "[*] " + i + " - " + str(j)+"/"+str(size) + " (" + str(percentage)+ '%)' +  color.END)
        sys.stdout.flush()
        j += 1
    sys.stdout.write("\n")
    sys.stdout.write("\r")
    print(color.BOLD + color.YELLOW + '[+] Password Not Found' + color.END)
