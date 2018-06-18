#!c:\bin\python36\python.exe

import os
import sys

# from random import randint
from pyWords import *


#---------------------------------------------------------------------
#   Class Constants for Command
#---------------------------------------------------------------------
class ClConst:
    def __init__(self):
        pass
    
#---------------------------------------------------------------------
#   CONFIG MAIN COMMAND
#---------------------------------------------------------------------
    @staticmethod
    def CMD_EXIT():
        return '0'
    
    @staticmethod
    def CMD_LEARN():
        return '1'

    @staticmethod
    def CMD_LOAD_DICT():
        return '2'

    @staticmethod
    def CMD_SAVE_DICT():
        return '3'

    @staticmethod
    def CMD_CONFIG():
        return '4'

#---------------------------------------------------------------------
#   CONFIG MENU COMMAND
#---------------------------------------------------------------------
    @staticmethod
    def CMD_DICT():
        return '1'

    @staticmethod
    def CMD_MODE():
        return '2'

    @staticmethod
    def CMD_BUF_SIZE():
        return '3'

    @staticmethod
    def CMD_LIMIT_ANSWERS():
        return '4'

    @staticmethod
    def CMD_VIEW_CONFIG():
        return '5'

    @staticmethod
    def CMD_SAVE_CONFIG():
        return '6'

#---------------------------------------------------------------------
#   CLEAR SCREEN
#---------------------------------------------------------------------
def clear_screen():
    if os.name == 'nt':             # check operation system
        os.system('cls')            # command for windows
    else:
        os.system('clear')          # command for others
            

#---------------------------------------------------------------------
# SHOW_MENU FUNCTION
#---------------------------------------------------------------------
def show_menu():
    clear_screen()
    print("1. Учить слова")
    print("2. Загрузить словарь")
    print("3. Сохранить результаты")
    print("4. Настройка")
    print("0. Выйти")
    cmd = input("Введите команду: ")
    return cmd

#---------------------------------------------------------------------
# SHOW_MENU FUNCTION
#---------------------------------------------------------------------
def showConfigMenu():
    clear_screen()
    print("1. Файл словаря")
    print("2. Режим обучения")
    print("3. Размер буфера слов")
    print("4. Количество ответов")
    print("5. Просмотр настроек")
    print("6. Сохранение настроек")
    print("0. Выйти")
    cmd = input("Введите команду: ")
    return cmd

#---------------------------------------------------------------------
# LEARN A WORD
#---------------------------------------------------------------------
def learnWord(words):
    word, answers = words.getSet()
    print(word, '\n')
    num = 1
    yes = ['Y', 'y', 'Д', 'н']
    for answer in answers:
        print(num, answer)
        num += 1
    status = True
    sel = input('Выберите вариант ответа: ')
    prompt = "Введите число от 1 до " + \
            str(words.getLimitAnswers()) + ": "
    while status:
        if sel == "" or sel == None:
            sel = input("Выйти, Вы уверены? (Y/n)")
            if sel in yes:
                status = False
                break
            else:
                continue
        try:
            idx = int(sel) - 1
        except:
            sel = input(prompt)
            continue
        else:
            if not words.checkIndex(idx):
                sel = input(prompt)
                continue
        if words.checkTrans(answers[idx]):
            words.incCount()
            break
        else:
            words.decCount()
            sel = input('Неправильно! Выберите вариант ответа: ')
    return status

#---------------------------------------------------------------------
# WORKING CONFIG
#---------------------------------------------------------------------
def configMenu(words):
    cfg_cmd = ClConst.CMD_DICT()
    while cfg_cmd != ClConst.CMD_EXIT():
        cfg_cmd = cmdConfig(showConfigMenu(), words)
        
#---------------------------------------------------------------------
# LEARN WORDS
#---------------------------------------------------------------------
def learnWords(words):
    while True:
        cnt = input("Сколько слов будем учить? ")
        try:
            num = int(cnt)
        except:
            print("Введите число > 0") 
            num = 0
        else:
            if num <= 0:
                print("Введите число > 0") 
        finally:
            if num > 0:
                break
    for idx in range(num):
        clear_screen()
        if not learnWord(words):
            return False
    return True

#---------------------------------------------------------------------
# MAIN FUNCTION
#---------------------------------------------------------------------
def do_command(cmd, words):
    if cmd == ClConst.CMD_EXIT():
        # input("Для продолжения нажмите Enter...")
        return cmd

    elif cmd == ClConst.CMD_LEARN():
        learnWords(words)
        return cmd

    elif cmd == ClConst.CMD_LOAD_DICT():
        words.setFileName()
        words.loadWords()
        # input("Для продолжения нажмите Enter...")
        return cmd
    
    elif cmd == ClConst.CMD_SAVE_DICT():
        words.saveDict()
        input("\nСохранение результатов. Для продолжения нажмите Enter...")
        return cmd

    elif cmd == ClConst.CMD_CONFIG():
        configMenu(words)
        return cmd

    else:
        input("\nНеизвестная команда. Для продолжения нажмите Enter...")
        return cmd
        
#---------------------------------------------------------------------
#   Config Menu Commands
#---------------------------------------------------------------------
def cmdConfig(cmd, words):
    if cmd == ClConst.CMD_EXIT():
        # input("\nВыход. Для продолжения нажмите Enter...")
        return cmd
    elif cmd == ClConst.CMD_DICT():
        print(words.DICT_NAME() + '=' + words.getFileName())
        words.setFileName()
        return cmd
    elif cmd == ClConst.CMD_MODE():
        print(words.MODE() + '=' + str(words.getLearningMode()))
        words.setLearningMode()
        return cmd
    elif cmd == ClConst.CMD_BUF_SIZE():
        print(words.BUF_SIZE() + '=' + str(words.getBufSize()))
        words.setBufferSize()
        return cmd
    elif cmd == ClConst.CMD_LIMIT_ANSWERS():
        print(words.LIMIT_ANSWERS() + '=' + str(words.getLimitAnswers()))
        words.setLimitAnswers()
        return cmd
    elif cmd == ClConst.CMD_VIEW_CONFIG():
        words.viewConfig()
        input("\nДля продолжения нажмите Enter...")
        return cmd
    elif cmd == ClConst.CMD_SAVE_CONFIG():
        words.saveConfig()
        input("\nСохранение настроек. Для продолжения нажмите Enter...")
        return cmd
    else:
        input("\nНеизвестная команда. Для продолжения нажмите Enter...")
        return cmd

#---------------------------------------------------------------------
# MAIN FUNCTION
#---------------------------------------------------------------------
def main():
    cmd = ClConst.CMD_LEARN()
    dictWord = ClWords()
    while cmd != ClConst.CMD_EXIT():
        cmd = do_command(show_menu(), dictWord)


#---------------------------------------------------------------------
# RUN MAIN FUNCTION
#---------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
