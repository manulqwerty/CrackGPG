# CrackGPG

[![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-yellow.svg)](https://www.python.org/) [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://raw.githubusercontent.com/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@manulqwerty-blue.svg)](https://twitter.com/manulqwerty) 

CrackGPG is an open source CTF tool used to crack GPG (GNU Privacy Guard) / PGP (Pretty Good Privacy) files
**Developed by [@manulqwerty - IronHackers](https://ironhackers.es).**

Screenshots
----
[GIF]

Instalation
----
You can download CrackGPG by clonin the [Git](https://github.com/manulqwerty/CrackGPG/) repository:
	
    git clone https://github.com/manulqwerty/CrackGPG.git
    cd CrackGPG && pip install -r requirements.txt
	
CrackGPG works out of the box with [Python](http://www.python.org/download/) version **2.6.x** and **2.7.x** on any platform.
	
Usage
----
To get help:

    python crackgpg.py -h
  	
To crack a GPG_FILE using a custom WORDLIST.TXT:

    python crackgpg.py GPG_FILE WORDLIST.TXT
    
You can also use the compiled format:

    ./crackgpg.pyc -h
