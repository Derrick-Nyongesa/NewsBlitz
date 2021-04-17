import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    """
    Test class to test the nehaviour of the Articles class
    """
    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_article = Articles("Politico","By Benjamin Din", "2024 GOP contenders collect cash", "Republicans who led efforts to overturn the election results in January did especially well, according to the latest quarterly FEC filings.", "https://www.politico.com/news/2021/04/15/2024-gop-cash-fec-482240", "https://static.politico.com/90/a6/2eff74ff4d69b7aee677b55ae6e2/gettyimages-1230713929.jpg", "2021-04-16T02:10:04Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

