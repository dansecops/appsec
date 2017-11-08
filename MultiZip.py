from zipfile import ZipFile

import os


class MultiZip():

    times = 0;

    def __init__(self, times):
        self.times = times

    def getTimes(self):
        print("Times: {0} %f".format(self.times) %(2.33333))

    def setTimes(self, times):
        self.times = times

    def createFile(self):
        print("Times: %s" % str(self.times))
        if os.path.isfile("spam.zip") is False:
            print("File does not exist, so we create it.")
            with ZipFile('spam.zip', 'a') as myzip:
                myzip.write('secret.txt')
                myzip.close()
                filename = os.path.realpath('secret.txt')
                print("File has been zipped: {} ".format(filename))

        else:
            with ZipFile('spam2.zip', 'a') as myzip:
                myzip.write('spam.zip')
                #print(ZipFile.getinfo(myzip, 'secret.txt'))
                #os.remove("resources/spam.zip")


mz = MultiZip(1000)
mz.createFile()









