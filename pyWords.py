import random
import os.path as path
import os

#---------------------------------------------------------------------
#   CLASS ClWords
#---------------------------------------------------------------------

class ClWords:
    def __init__(self, fileName=None):
        self.clearDict()    # clearMainDict()
        self.cur_id = ""    # key of dictionary
        self.__limitAnswers = self.DEFAULT_LIMIT()  # limit for output list
        self.__bufSize = self.DEFAULT_BUFFER_SIZE() # set default value
#---------------------------------------------------------------------
#       Possible Modes
#       0 - one time of word's repeat
#       1 - six time of word's repeat
#---------------------------------------------------------------------
        self.__mode = self.DEFAULT_MODE()   # default mode from {0, 1}
        self.setCWD()       # set Current Work Directory
        if fileName == None:
            self.__fileName = ""
            self.getConfig()
            if self.__fileName != "":
                self.loadWords()
        else:
            self.__fileName = fileName
            self.loadWords()

#---------------------------------------------------------------------
#   CONSTANTS    
#---------------------------------------------------------------------
    @staticmethod
    def DICT_NAME():    # dictionary file name
        return 'Dictionary'

    @staticmethod
    def MODE():         # working mode {0, 1}
        return 'Mode'

    @staticmethod
    def DEFAULT_MODE(): # default mode - 0
        return 0

    @staticmethod
    def BUF_SIZE():     # words buffer size
        return 'BufferSize'

    @staticmethod
    def DEFAULT_BUFFER_SIZE():  # default value
        return 6

    @staticmethod
    def CONFIG_NAME():  # config file name
        return 'pyWords.ini'
    
    @staticmethod
    def ENCODING(): # enconding file
        return 'windows-1251'
    
    @staticmethod
    def NOUN():     # type of word - noun
        return 'NOUN'
    
    @staticmethod
    def VERB():     # type of word - verb
        return 'VERB'
    
    @staticmethod
    def OTHER():    # type of word - other
        return 'OTHER'
    
    @staticmethod
    def DEFAULT_LIMIT():    # default limit of answer
        return 6
    
    @staticmethod
    def LIMIT_ANSWERS():    # parameter name of limit answer
        return 'LimitAnswers'
    
#---------------------------------------------------------------------
#   Set Current Work Directory (CWD)
#---------------------------------------------------------------------
    def setCWD(self):
        fn = path.abspath(__file__)
        os.chdir(path.dirname(fn))

#---------------------------------------------------------------------
#   Read config file pyWords.ini    
#---------------------------------------------------------------------
    def getConfig(self):
        try:
            with open(self.CONFIG_NAME(), "r+", encoding = self.ENCODING()) as self.__fd:
                for buf in self.__fd:
                    try:
                        lines = buf.splitlines()
                        buf = lines[0]
                    except ValueError as err:
                        pass
                    arr = buf.split("=")
                    if arr[0] == self.DICT_NAME():
                        self.__fileName = arr[1]
                    elif arr[0] == self.MODE():
                        try:
                            self.__mode = int(arr[1])
                        except:
                            self.__mode = self.DEFAULT_MODE()
                    elif arr[0] == self.BUF_SIZE():
                        try:
                            self.__bufSize = int(arr[1])
                        except:
                            self.__bufSize = self.DEFAULT_BUFFER_SIZE()
                    elif arr[0] == self.LIMIT_ANSWERS():
                        try:
                            self.__limitAnswers = int(arr[1])
                        except:
                            self.__limitAnswers = self.DEFAULT_LIMIT()
                    else:
                        pass
        except FileNotFoundError as err:            
            print(err)
            return None
        else:
            pass
        
#---------------------------------------------------------------------
#   Set limit for output list
#---------------------------------------------------------------------
    def setLimit(self, limit):
        if limit > 1:
            self.__limitAnswers = limit

#---------------------------------------------------------------------
#   Get file name of dictionary
#---------------------------------------------------------------------
    def getFileName(self):
        return(self.__fileName)
        
#---------------------------------------------------------------------
#   Get Learning Mode
#---------------------------------------------------------------------
    def getLearningMode(self):
        return(self.__mode)
        
#---------------------------------------------------------------------
#   Set Learning Mode
#---------------------------------------------------------------------
    def setLearningMode(self):
        prompt = "Установлен режим по умолчанию - " + \
                 str(self.DEFAULT_MODE())
        try:
            self.__mode = int(input("Введите режим обучения {0,1}: "))
        except:
            self.__mode = 0 # default mode
            input(prompt)
        finally:
            if self.__mode not in [0,1]:
                self.__mode = 0 # default mode
                input(prompt)
        
#---------------------------------------------------------------------
#   Get Buffer Size
#---------------------------------------------------------------------
    def getBufSize(self):
        return(self.__bufSize)
        
#---------------------------------------------------------------------
#   Set Buffer Size
#---------------------------------------------------------------------
    def setBufferSize(self):
        prompt = "Установлен режим по умолчанию - " + \
                 str(self.DEFAULT_BUFFER_SIZE())
        try:
            self.__bufSize = int(input("Введите размер буфера слов (6): "))
        except:
            self.__bufSize = self.DEFAULT_BUFFER_SIZE() # default mode
            input(prompt)
        finally:
            if self.__bufSize < 2:
                self.__bufSize = self.DEFAULT_BUFFER_SIZE() # default mode
                input(prompt)
            
#---------------------------------------------------------------------
#   Get Limit of Answers
#---------------------------------------------------------------------
    def getLimitAnswers(self):
        return(self.__limitAnswers)
        
#---------------------------------------------------------------------
#   Set Limit of Answers
#---------------------------------------------------------------------
    def setLimitAnswers(self):
        prompt = "Количество ответов по умолчанию - " + \
                 str(self.DEFAULT_LIMIT())
        try:
            self.__limitAnswers = int(input("Введите количество ответов (5): "))
        except:
            self.__limitAnswers = self.DEFAULT_LIMIT() # default limit
            input(prompt)
        finally:
            if self.__limitAnswers < 2:
                self.__limitAnswers = self.DEFAULT_LIMIT() # default limit
                input(prompt)
            
#---------------------------------------------------------------------
#   View Config 
#---------------------------------------------------------------------
    def viewConfig(self):
        buf = self.DICT_NAME() + '=' + self.getFileName()
        print(buf)
        buf = self.MODE() + '=' + str(self.getLearningMode())
        print(buf)
        buf = self.BUF_SIZE() + '=' + str(self.getBufSize())
        print(buf)
        buf = self.LIMIT_ANSWERS() + '=' + str(self.getLimitAnswers())
        print(buf)
        
#---------------------------------------------------------------------
#   Save Config to File
#---------------------------------------------------------------------
    def saveConfig(self):
        try:
            with open(self.CONFIG_NAME(), "w+", encoding = self.ENCODING()) as self.__fd:
                buf = self.DICT_NAME() + '=' + self.getFileName() + '\n'
                self.__fd.write(buf)
                buf = self.MODE() + '=' + str(self.getLearningMode()) + '\n'
                self.__fd.write(buf)
                buf = self.BUF_SIZE() + '=' + str(self.getBufSize()) + '\n'
                self.__fd.write(buf)
                buf = self.LIMIT_ANSWERS() + '=' + str(self.getLimitAnswers()) + '\n'
                self.__fd.write(buf)
        except:
            input("Ошибка сохранения настроек. Для продолжения нажмите Enter...")

#---------------------------------------------------------------------
#   Check index for output list
#---------------------------------------------------------------------
    def checkIndex(self, idx):
        if idx >= 0 and idx < self.__limitAnswers:
            return True
        else:
            return False

#---------------------------------------------------------------------
#   Prepare Working Dictionary
#---------------------------------------------------------------------
    def clearDict(self):
        self.cacheWords = dict()
        self.cacheTrans = dict()
        self.cacheTypes = dict()
        self.cacheCount = dict()

#---------------------------------------------------------------------
#   Prepare Main Dictionary
#---------------------------------------------------------------------
    def clearMainDict(self):
        self.mainWords = dict()
        self.mainTrans = dict()
        self.mainTypes = dict()
        self.mainCount = dict()

#---------------------------------------------------------------------
#   Get Min Rank
#---------------------------------------------------------------------
    def getMinRank(self):
        minRank = 0
        for key in self.keyList:
            if minRank > int(self.mainCount[key]):
                minRank = int(self.mainCount[key])
        return minRank
    
#---------------------------------------------------------------------
#   Copy from Main Dictionary
#---------------------------------------------------------------------
    def copyFromMainDict(self, key):
        self.cacheWords[key] = self.mainWords[key]
        self.cacheTrans[key] = self.mainTrans[key]
        self.cacheTypes[key] = self.mainTypes[key]
        self.cacheCount[key] = self.mainCount[key]

#---------------------------------------------------------------------
#   Copy to Main Dictionary
#---------------------------------------------------------------------
    def copyToMainDict(self, key):
        self.mainWords[key] = self.cacheWords[key]
        self.mainTrans[key] = self.cacheTrans[key]
        self.mainTypes[key] = self.cacheTypes[key]
        self.mainCount[key] = self.cacheCount[key]

#---------------------------------------------------------------------
#   Add to Dictionary
#---------------------------------------------------------------------
    def addToDict(self, cnt, typ, key):
        if cnt[typ] < self.getBufSize():
            self.copyFromMainDict(key)
        cnt[typ] += 1
        return cnt

#---------------------------------------------------------------------
#   Check copy over
#---------------------------------------------------------------------
    def checkCopyOver(self, d):
        noun  = d[self.NOUN()] >= self.getBufSize()
        verb  = d[self.VERB()] >= self.getBufSize()
        other = d[self.OTHER()] >= self.getBufSize()
        return (noun and verb and other)
    
#---------------------------------------------------------------------
#   Get Key List
#---------------------------------------------------------------------
    def getKeyList(self):
        keys = list()
        cnt = dict()
        cnt[self.NOUN()] = 0  # noun count
        cnt[self.VERB()] = 0  # verb count
        cnt[self.OTHER()] = 0 # other count
        minRank = self.getMinRank()
        while True:
            for key in self.keyList:
                if minRank != int(self.mainCount[key]):
                    continue
                keys.append(key)
                if self.mainTypes[key] == self.NOUN():
                    cnt[self.NOUN()] += 1
                elif self.mainTypes[key] == self.VERB():
                    cnt[self.VERB()] += 1
                else:
                    cnt[self.OTHER()] += 1
            if self.checkCopyOver(cnt):
                break
            else:
                minRank += 1 # increase rank and continue
        return keys
                    
#---------------------------------------------------------------------
#   Get from Main Dictionary
#---------------------------------------------------------------------
    def getFromMainDict(self):
        self.clearDict()
        count = dict()
        count[self.NOUN()] = 0   # noun count
        count[self.VERB()] = 0   # verb count
        count[self.OTHER()] = 0  # other count
        keys = self.getKeyList() # phase 1
        while len(keys) > 0:     # phase 2
            key = random.choice(keys)
            if self.mainTypes[key] == self.NOUN():
                count = self.addToDict(count, self.NOUN(), key)
            elif self.mainTypes[key] == self.VERB():
                count = self.addToDict(count, self.VERB(), key)
            else:
                count = self.addToDict(count, self.OTHER(), key)
            del keys[key]   # delete selected key
            if self.checkCopyOver(count):
                break
            
#---------------------------------------------------------------------
#   Get File Name for Loading Dictionary
#---------------------------------------------------------------------
    def setFileName(self):
        name = input("File name of Dictionary: ")
        if name != "":
            self.__fileName = name

#---------------------------------------------------------------------
#   Load Dictionary from File
#---------------------------------------------------------------------
    def loadWords(self):
        if self.__fileName == None or self.__fileName == "":
            print("Не правильное имя файла")
            return None
        try:
            with open(self.__fileName, "r+", encoding = "windows-1251") \
                 as self.__fd:
                self.clearDict()
                for buf in self.__fd:
                    lines = buf.splitlines()
                    buf = lines[0]
                    arr = buf.split("\t")
                    self.cacheWords[arr[0]] = arr[1]
                    self.cacheTrans[arr[0]] = arr[2]
                    self.cacheTypes[arr[0]] = arr[3]
                    self.cacheCount[arr[0]] = arr[4]
        except FileNotFoundError as err:            
            print(err)
            return None
        else:
            self.keyList = list(self.cacheWords)
            print("Loaded done.")
    
#---------------------------------------------------------------------
#   Get Random Word from Dictionary
#---------------------------------------------------------------------
    def getAnyWord(self):
        self.cur_id = random.choice(self.keyList)
        return self.cacheWords[self.cur_id]

#---------------------------------------------------------------------
#   Get Translate for Current Word
#---------------------------------------------------------------------
    def getTrans(self):
        return self.cacheTrans[self.cur_id]

#---------------------------------------------------------------------
#   Get Set for Output
#---------------------------------------------------------------------
    def getSet(self):
        word = self.getAnyWord()
        answers = list()
        answers.append(self.getTrans()) # shuffle!
        while len(answers) < self.getLimitAnswers():
            cur_id = random.choice(self.keyList)
            # check type ot word
            if self.cacheTypes[cur_id] != self.cacheTypes[self.cur_id]:
                continue
            # check duplicate in answers
            if self.cacheTrans[cur_id] in answers:
                continue
            answers.append(self.cacheTrans[cur_id])
        random.shuffle(answers)    
        return word, answers

#---------------------------------------------------------------------
#   Check Translate for Current Word
#---------------------------------------------------------------------
    def checkTrans(self, trans):
        return self.cacheTrans[self.cur_id] == trans
        
#---------------------------------------------------------------------
#   Decrement Count of Word
#---------------------------------------------------------------------
    def decCount(self):
        self.cacheCount[self.cur_id] = \
            str(int(self.cacheCount[self.cur_id]) - 1)
        return self.cacheCount[self.cur_id]

#---------------------------------------------------------------------
#   Increment Count of Word
#---------------------------------------------------------------------
    def incCount(self):
        self.cacheCount[self.cur_id] = \
            str(int(self.cacheCount[self.cur_id]) + 1)
        return self.cacheCount[self.cur_id]

#---------------------------------------------------------------------
#   Save Dictionary to File
#---------------------------------------------------------------------
    def saveDict(self):
        try:
            with open(self.__fileName, "w+", encoding = "windows-1251") \
                 as self.__fd:
                for key in self.keyList:
                    buf = key + "\t" + \
                          self.cacheWords[key] + "\t" + \
                          self.cacheTrans[key] + "\t" + \
                          self.cacheTypes[key] + "\t" + \
                          self.cacheCount[key] + '\n'
                    self.__fd.write(buf)
        except FileNotFoundError as err:            
            print(err)
