#!/bin/python

def run(**args):
    print "[*] in environment module"
    return str(os.environ)
