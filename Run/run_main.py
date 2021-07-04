import os
import sys
run_base = os.getcwd()
sys.path.append(run_base)
from HTMLTestRunner import HTMLTestRunner
import unittest
from Run.test_case01 import TestCase01
from Run.test_case02 import TestCase02
from Run.test_case03 import TestCase03
from Run.test_case04 import TestCase04
from Run.test_case05 import TestCase05
case_01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
case_02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
case_03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
case_04 = unittest.TestLoader().loadTestsFromTestCase(TestCase04)
case_05 = unittest.TestLoader().loadTestsFromTestCase(TestCase05)
suote = unittest.TestSuite([case_01, case_02, case_03, case_04, case_05])

with open('D:\\dev\\python_project\\PythonApiTest\\Case\\report.html', 'w', encoding='utf-8') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='创建者中心接口测试', description='huangjiajia')
    runner.run(suote)

