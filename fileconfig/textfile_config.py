#a very nieve way to simply read values from a textfile with key=value
class TextFileConfig:
    def read_text_file_into_dictionary(self,filename):
        d=dict()
        with open(filename,'r') as text_file:
            for line in text_file:
                values=line.rstrip().split("=")
                d[values[0]]=values[1]
        return d