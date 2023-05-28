import unittest
import HtmlTestRunner

from test_homepage_manduka import Test_Home_Page
from test_search_manduka import Test_Manduka_Search


class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Test_Home_Page),
                                 unittest.defaultTestLoader.loadTestsFromTestCase(Test_Manduka_Search)])


        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Test Execution Report",
            report_name="Test Results"
        )

        runner.run(teste_de_rulat)