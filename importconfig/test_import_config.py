import unittest
from importconfig import import_config as aIC

class test_import_config(unittest.TestCase):
    def setUp(self):
        return

    def test_read_text_file(self):
        print("running import config")
        a = aIC.ImportConfig()
        d = a.read_imported_config_into_dictionary()
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(d['1'] == 'one')
        self.assertTrue(d['2'] == 'two')
        self.assertTrue(d['3'] == 'cat')


if __name__ == '__main__':
    unittest.main()