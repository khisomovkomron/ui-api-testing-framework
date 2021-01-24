import traceback
import logging as logger
import time
import random, string

class Util(object):

    def __init__(self):
        self.log = logger

    def sleep(self, sec, info=""):

        if info is not None:
            self.log.info("Wain :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):

        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_lowercase + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, itemLength=10):
        namelist = []
        for i in range(0, listSize):
            namelist.append(self.getUniqueName(itemLength[i]))
        return namelist


    def verifyTextContains(self, actualText, expectedText):

        self.log.info("Actual Text from application Web UI --> :: " + actualText)
        self.log.info("Expected  Text from application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("$$$ VERIFICATION CONTAIN !!!")
            return True
        else:
            self.log.info('$$$ VERIFICATION DOES NOT CONTAIN!!!')
            return False

    def verifyTextMatch(self, actualText, expectedText):

        self.log.info("Actual Text from application Web UI --> :: " + actualText)
        self.log.info("Expected  Text from application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("$$$ VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("$$$ VERIFICATION DOES NOT MATCHED !!!")
            return False
    def verifyListMatch(self, expectedList, actualList):
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):

        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True
