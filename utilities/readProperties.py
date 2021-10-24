import configparser
config=configparser.ConfigParser()
config.read("D:\work_pycharm\PythonProjects\Pytestframwork1\Configurations\config.ini")
class readfiles:
    @staticmethod
    def readurl():  #if  it is static method no need to give self here///to call these methods, no need to create object of the class
        url=config.get('common info','url')
        return url

