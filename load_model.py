"""load_model.py: 

    Script to load SBML model into MOOSE.
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import moose
import logging
import sys

def load_model(model_path):
    moose.readSBML(model_path, '/model')
    logging.info("Done loading model %s " % model_path)


def main():
    modelpath = sys.argv[1]
    load_model(modelpath)

if __name__ == '__main__':
    main()
