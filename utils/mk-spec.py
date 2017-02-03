#!/usr/bin/env python

import os
import sys
import logging
import datetime

import requests

if __name__ == "__main__":

    import optparse
    opt_parser = optparse.OptionParser()

    opt_parser.add_option('-l', '--local', dest='local', action='store', default=None, help='')
    opt_parser.add_option('-r', '--remote', dest='remote', action='store', default=None, help='')
    opt_parser.add_option('-k', '--key', dest='key', action='store', default=None, help='')        

    opt_parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Be chatty (default is false)')
    options, args = opt_parser.parse_args()

    if options.verbose:	
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    if options.local == None:
        logging.error("Missing local file")
        sys.exit(1)

    if options.remote == None:
        logging.error("Missing remote URL")
        sys.exit(1)

    if options.key == None:
        logging.error("Missing key")
        sys.exit(1)
        
    fh = open(options.local, "w")
    
    rsp = requests.get(options.remote)
    spec = rsp.content
    spec = spec.strip()

    spec = spec.replace("'", "\\'")

    today = datetime.datetime.today()
    now = today.isoformat()
    
    fh.write("<?php\n\n")
    fh.write("        # this file was generated by robots on %s\n" % now)    
    fh.write("        # https://github.com/whosonfirst/flamework-whosonfirst/blob/master/utils/mk-spec.py\n")
    fh.write("        # https://github.com/whosonfirst/flamework-whosonfirst/blob/master/Makefile\n\n")
    fh.write("        ########################################################################\n\n")
    fh.write("        $GLOBALS['%s']['__SPEC__'] = '%s';\n\n" % (options.key, spec))
    fh.write("        ########################################################################\n")
    fh.write("        # the end\n")
