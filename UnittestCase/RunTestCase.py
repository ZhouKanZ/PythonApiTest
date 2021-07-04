import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

import unittest

'''
from UnittestCase.test_case_01 import TestCase01
from UnittestCase.test_case_02 import TestCase02
from UnittestCase.test_case_03 import TestCase03
case_01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
case_02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
case_03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
suote = unittest.TestSuite([case_01, case_02, case_03])
unittest.TextTestRunner().run(suote)
'''
discover = unittest.defaultTestLoader.discover(base_path)
unittest.TextTestRunner().run(discover)


