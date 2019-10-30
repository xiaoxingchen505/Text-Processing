"""\
------------------------------------------------------------
USE: python <PROGNAME> (options) file1...fileN
OPTIONS:
    -h : print this help message
    -b : use BINARY weights (default: count weighting)
    -s FILE : use stoplist file FILE
    -I PATT : identify input files using pattern PATT, 
              (otherwise uses files listed on command line)
------------------------------------------------------------
"""

import sys, re, getopt, glob

opts, args = getopt.getopt(sys.argv[1:], 'hs:bI:')
opts = dict(opts)
filenames = args

##############################
# HELP option

if '-h' in opts:
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print(help, file=sys.stderr)
    sys.exit()

##############################
# Identify input files, when "-I" option used

if '-I' in opts:
    filenames = glob.glob(opts['-I'])

print('INPUT-FILES:', ' '.join(filenames))

##############################
# STOPLIST option

stops = set()
if '-s' in opts:
    with open(opts['-s'], 'r') as stop_fs:
        for line in stop_fs :
            stops.add(line.strip())

##############################
#tokenisation

#text_file_1 = open(sys.argv[3],'r')
#text_file_2 = open(sys.argv[4],'r')


for word in open(sys.argv[3],'r'):
    word_lower = word.lower()
    
for word in open(sys.argv[4],'r'):
    word_lower = word.lower()
##############################
    
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

def comparison(x,y):

    A = countWords(x)
    B = countWords(y)
    #print(A)
    #print(countWords(x))
    jaccard_co = len(set(A.keys())&set(B.keys()))/len(set(A.keys())|set(B.keys()))
    print(jaccard_co)
    
def  jaccard_metric(x,y):
    A = countWords(x)
    B = countWords(y)
    #print(A)
    #print(countWords(x))
    jaccard_co = len(set(A.keys())&set(B.keys()))/len(set(A.keys())|set(B.keys()))
    print(jaccard_co)
#countWords(open(sys.argv[3],'r'))
comparison(open(sys.argv[3],'r'),open(sys.argv[4],'r'))