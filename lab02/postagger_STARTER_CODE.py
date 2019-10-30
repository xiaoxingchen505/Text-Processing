"""
USE: python <PROGNAME> (options) 
OPTIONS:
    -h : print this help message and exit
    -d FILE : use FILE as data to create a new lexicon file
    -l FILE : create OR read lexicon file FILE
    -t FILE : apply lexicon to test data in FILE
"""
################################################################

import sys, re, getopt

################################################################
# Command line options handling, and help

opts, args = getopt.getopt(sys.argv[1:],'hd:l:t:')
opts = dict(opts)

def printHelp():
    help = __doc__.replace('<PROGNAME>',sys.argv[0],1)
    print('-' * 60, help, '-' * 60, file=sys.stderr)
    sys.exit()
    
if '-h' in opts:
    printHelp()

if len(args) > 0:
    print("\n** ERROR: no arg files - only options! **", file=sys.stderr)
    printHelp()

if '-l' not in opts:
    print("\n** ERROR: must specify lexicon file name (opt: -l) **", file=sys.stderr)
    printHelp()

################################################################

for word in open(sys.argv[1],'r'):
    word_lower = word.lower()    
    
def countWords(x):
    dict_ = dict()
    stopword = readStopWords()
    
    for word in x.read().split():
        word = word.lower()
        if word in stopword:
            continue
        else:
            if word not in dict_:
                dict_[word] = 1
            else:
                dict_[word] += 1 
                
    
    return dict_

def readStopWords():
    stop = []
    for word in open(sys.argv[2],'r').read().split():
        stop.append(word)
    return stop

