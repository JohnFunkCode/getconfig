#a very nieve way to simply read values from a jpg with key=value
from PIL import Image
from PIL.ExifTags import TAGS
#import piexif - hard to find libary
import exifread

class ImgFileConfig:
    def __init__(self):
        pass

    def read_img_file_into_dictionary_pilow(self, filename):
        #print("done with pillow")
        d = dict()
        im = Image.open(filename)
        info = im._getexif()
        # for tag, value in info.items():
        #     key = TAGS.get(tag, tag)
        #     print("Tag: {0} Value: {1}".format(key, value))

        for tag, value in info.items():
            key = TAGS.get(tag, tag)
            if key == 'ImageDescription':
                break

        #print("value:{0}".format(value))

        lines = str(value).splitlines(False)
        #print(lines)

        for line in lines:
             values = line.rstrip().split("=")
             d[values[0]] = values[1]

        return d

    def read_img_file_into_dictionary_exifread(self,filename):
        #print("done with exifread")
        d=dict()
        f = open(filename,'rb')
        tags = exifread.process_file(f)
        # for tag in tags.keys():
        #     if not tag in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        #         print("Key: {0} value {1}".format(tag, tags[tag]))

        lines=str(tags['Image ImageDescription']).splitlines(False)
        for line in lines:
             values = line.rstrip().split("=")
             d[values[0]] = values[1]

        #print(d)
        return d

    # def read_img_file_into_dictionary_piexif(self,filename):
    #     # print("done with piexif")
    #     d=dict()
    #     dictionary=piexif.load(filename)
    #     dictionary.pop("thumbnail")
    #     # print("dictionary={0}".format(dictionary))
    #     for idf in dictionary:
    #         # print("IDF:{0}".format(idf))e
    #         for key in dictionary[idf]:
    #             v=dictionary[idf][key]
    #             #print( "Key:{0} value:{1}".format(key,v))
    #
    #     idf='0th'
    #     key=270
    #     desc=str(dictionary[idf][key],'utf-8')
    #
    #     # print(type(desc))
    #     # print("desc={}".format(desc))
    #     lines=desc.splitlines(False)
    #     # print('lines:{0}'.format(lines))
    #     for line in lines:
    #         # print('line:{0}'.format(line))
    #         values = line.rstrip().split("=")
    #         # print('Values:{}'.format(values))
    #         d[values[0]] = values[1]
    #     return d



if __name__ == '__main__':
    aIC = ImgFileConfig()
    d=aIC.read_img_file_into_dictionary_pilow("Clippy.jpg")
    print("Pillow:{0}".format(d))

    d=aIC.read_img_file_into_dictionary_exifread("Clippy.jpg")
    print("ExifRead:{0}".format(d))

#    d=aIC.read_img_file_into_dictionary_piexif("Clippy.jpg")
#    print("piexif:{0}".format(d))

