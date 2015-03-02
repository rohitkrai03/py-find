#!/usr/bin/env python 

import sys
import re
import os

# Get the start directory.
start = os.path.normpath(sys.argv[1])

# Get the patterns from the command line arguments.
pattern = sys.argv[2]


# Convert them to regular expressions.
expr = re.compile(pattern)

# Traverse the directory for all the files.
for root, dirs, files in os.walk(start):
	for fname in files:
		# If a file matches the pattern then print its name.
		if expr.search(fname):
			print(os.path.join(root, fname))
