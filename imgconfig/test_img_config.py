import unittest
from imgconfig import img_config as ifc

class test_ImgFileConfig(unittest.TestCase):
    def setUp(self):
        return

    def test_read_img_file_into_dictionary_pilow(self):
        aIC = ifc.ImgFileConfig()
        d = aIC.read_img_file_into_dictionary_pilow("Clippy.jpg")
        print("Pillow:{0}".format(d))
        self.assertTrue(isinstance(d,dict))
        self.assertTrue(d['name'] == 'clippy')
        self.assertTrue(d['a'] == 'one')
        self.assertTrue(d['b'] == 'two')
        self.assertTrue(d['c'] == 'three')

    def test_read_img_file_into_dictionary_exifread(self):
        aIC = ifc.ImgFileConfig()
        d = aIC.read_img_file_into_dictionary_exifread("Clippy.jpg")
        print("ExifRead:{0}".format(d))
        self.assertTrue(isinstance(d,dict))
        self.assertTrue(d['name'] == 'clippy')
        self.assertTrue(d['a'] == 'one')
        self.assertTrue(d['b'] == 'two')
        self.assertTrue(d['c'] == 'three')

if __name__ == '__main__':
    unittest.main()