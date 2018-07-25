import unittest
from fileconfig import textfile_config as tfc

class test_TextFileConfig(unittest.TestCase):
    def setUp(self):
        return

    def test_read_text_file(self):
        print("running textfile config")
        aTFC = tfc.TextFileConfig()
        d=aTFC.read_text_file_into_dictionary("test.txt")
        self.assertTrue(isinstance(d,dict))
        self.assertTrue(d['a'] == '1')
        self.assertTrue(d['c'] == 'cat')
        
if __name__ == '__main__':
    unittest.main()