__author__ = 'cosmo'

import opencog.cogserver
from pln_examples import *

class PLNTestModule(opencog.cogserver.Request):
    def __init__(self):
        pass

    def run(self, args, atomspace):
        raise Exception("Test exception")
        pln_examples = PLNExamples(atomspace)
        #pln_examples.test_all()
        pln_examples.run_pln_example('../tests/python/test_pln/scm/specific_rules/DeductionRule.scm')
