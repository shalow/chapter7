#!/bin/python

def run(**args):
    print "[*] In dirlister module"
    files = os.listdir(".")

    return str(files)
