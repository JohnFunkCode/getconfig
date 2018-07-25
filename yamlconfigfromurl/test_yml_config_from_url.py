import unittest
from yamlconfigfromurl import yml_config_from_url as ycfu

class test_TextFileConfig(unittest.TestCase):
    def setUp(self):
        return

    def test_get_yml_config_from_url(self):
        #print("running test")
        aYCFU = ycfu.YAMLConfig()
        d = aYCFU.get_yml_config_from_url("https://raw.githubusercontent.com/JohnFunkCode/getconfig/master/yamlconfigfromurl/test.yml")
        #print d
        self.assertTrue(isinstance(d, dict))
        mysql=d['mysql']
        self.assertTrue(mysql['host']=="localhost")


if __name__ == '__main__':
    unittest.main()