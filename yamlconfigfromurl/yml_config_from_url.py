# a very simple example of reading a yml config file from a url
import yaml
import requests

class YAMLConfig():
    def get_yml_config_from_url(self, url):
        response = requests.get(url)
        if (response.status_code == 200):
            d = yaml.load(response.text)
        #print(d)
        return d

if __name__ == '__main__':
    aYC = YAMLConfig()
    aYC.get_yml_config_from_url("https://raw.githubusercontent.com/JohnFunkCode/getconfig/master/yamlconfigfromurl/test.yml")