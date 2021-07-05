import unittest
from module import Calulator

class ModuleTest(unittest.TestCase):
    #创建ModuleTest类继承unittest.Testcase
    def setUp(self):
        self.cal=Calulator(6,2)

    def tearDown(self):
        pass
   #setUp（）和tearDown()两个方法，分别在每一个测试用例的开始和结束时执行。

    def test_add(self):
        result =self.cal.add()
        self.assertEqual(result,8)

    def test_sub(self):
        result=self.cal.sub()
        self.assertEqual(result,4)

    def test_mul(self):
        result=self.cal.mul()
        self.assertEqual(result,12)

    def test_div(self):
        result=self.cal.div()
        self.assertEqual(result,3)
  #unittest要求测试用例（方法）必须以“test"开头。
if __name__=="__main__":

    #构建测试集。调用unittest.TestSuite()类的addTest（）方法向测试套件中添加测试用例。
    suite=unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_sub"))
    suite.addTest(ModuleTest("test_mul"))
    suite.addTest(ModuleTest("test_div"))
    #执行测试。通过unittest.TextTestRunner()类的run()方法运行测试套件中的测试用例。
    runner=unittest.TextTestRunner()
    runner.run(suite)
