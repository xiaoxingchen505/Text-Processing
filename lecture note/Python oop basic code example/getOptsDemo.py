"""\
------------------------------------------------------------
USE: python <PROGNAME> (options) 
OPTIONS:
    -h : print this help message
    -s FILE : use stoplist file FILE (required)
    -b : use binary weighting (default is off)
------------------------------------------------------------
"""

import sys, getopt

# Usage message 
def usage():
    help = __doc__.replace('<PROGNAME>',sys.argv[0],1)
    print(help,file=sys.stderr)
    sys.exit(0)

# Set defaults
binary_weighting = 0

# Read arguments from command line and parse
opts, args = getopt.getopt(sys.argv[1:],'hs:b')

# Convert list-of-pairs to dictionary (for easy testing)
opts = dict(opts) 

# If '-h' option given, print out usage (and quit)
if '-h' in opts:
    usage()

# '-s' option is required - check whether it's there and print out usage if not
if '-s' in opts:
    stopword_file = opts['-s']
else:
    usage()

if '-b' in opts:
    binary_weighting = 1

# Print summary:

print("SUMMARY")
print("Command line strings:", sys.argv)
print("Arguments:", args)
print("Options:")
print("   Stopwords file:", stopword_file)
print("   Binary weighting:", binary_weighting)

