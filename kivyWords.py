import sys
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from pyWords import ClWords
from kivy.config import Config


class KivyWordsApp(App):
    def build(self):
        self.__words = ClWords()
        self.__word, self.__answers = self.__words.getSet()
#-----------------------------------------------------------------------        
        lo = BoxLayout(orientation = 'vertical', spacing = 10)
        self.btn = dict()
        self.y = 540
        self.x = 100
        self.w = 0.6
        self.h = 0.1
        self.lblWord = Label(text = self.__word,
            size_hint=(.7, 1)
            )
        lo.add_widget(self.lblWord)
#-----------------------------------------------------------------------        
        self.btnTrans1 = Button(text = self.__answers[0],
            size_hint=(.7, 1),
            pos_hint = {'center_x': 0.5}
            )
        self.btnTrans1.bind(on_press = self.pressButton)
        self.btn[hash(self.btnTrans1)] = self.btnTrans1.text
        lo.add_widget(self.btnTrans1)
#-----------------------------------------------------------------------        
        self.__background_color = self.btnTrans1.background_color
        self.__background_normal = self.btnTrans1.background_normal
#-----------------------------------------------------------------------        
        self.btnTrans2 = Button(text = self.__answers[1],
            size_hint=(.7, 1),
            pos_hint = {'center_x': 0.5}
            )
        self.btnTrans2.bind(on_press = self.pressButton)
        self.btn[hash(self.btnTrans2)] = self.btnTrans2.text
        lo.add_widget(self.btnTrans2)
#-----------------------------------------------------------------------        
        self.btnTrans3 = Button(text = self.__answers[2],
            size_hint=(.7, 1),
            pos_hint = {'center_x': 0.5}
            )
        self.btnTrans3.bind(on_press = self.pressButton)
        self.btn[hash(self.btnTrans3)] = self.btnTrans3.text
        lo.add_widget(self.btnTrans3)
#-----------------------------------------------------------------------        
        self.btnTrans4 = Button(text = self.__answers[3],
            size_hint=(.7, 1),
            pos_hint = {'center_x': 0.5}
            )
        self.btnTrans4.bind(on_press = self.pressButton)
        self.btn[hash(self.btnTrans4)] = self.btnTrans4.text
        lo.add_widget(self.btnTrans4)
#-----------------------------------------------------------------------        
        self.btnTrans5 = Button(text = self.__answers[4],
            size_hint=(.7, 1),
            pos_hint = {'center_x': 0.5}
            )
        self.btnTrans5.bind(on_press = self.pressButton)
        self.btn[hash(self.btnTrans5)] = self.btnTrans5.text
        lo.add_widget(self.btnTrans5)
#-----------------------------------------------------------------------        
        self.btnTrans6 = Button(text = self.__answers[5],
            size_hint=(.7, 1),
            pos_hint = {'center_x': 0.5}
            )
        self.btnTrans6.bind(on_press = self.pressButton)
        self.btn[hash(self.btnTrans6)] = self.btnTrans6.text
        lo.add_widget(self.btnTrans6)
#-----------------------------------------------------------------------        
        self.btnClose = Button(text = 'Close App',
            size_hint=(.7, 1),
            pos_hint = {'center_x': 0.5}
            )
        self.btnClose.bind(on_press = self.pressClose)
        lo.add_widget(self.btnClose)
        return lo

#-----------------------------------------------------------------------        
    def nextWord(self):
        self.__word, self.__answers = self.__words.getSet()
        self.lblWord.text = self.__word
        # restore color
        self.btnTrans1.background_color = self.__background_color
        self.btnTrans1.background_normal = self.__background_normal
        self.btnTrans2.background_color = self.__background_color
        self.btnTrans2.background_normal = self.__background_normal
        self.btnTrans3.background_color = self.__background_color
        self.btnTrans3.background_normal = self.__background_normal
        self.btnTrans4.background_color = self.__background_color
        self.btnTrans4.background_normal = self.__background_normal
        self.btnTrans5.background_color = self.__background_color
        self.btnTrans5.background_normal = self.__background_normal
        self.btnTrans6.background_color = self.__background_color
        self.btnTrans6.background_normal = self.__background_normal
        # set new translates
        self.btnTrans1.text = self.__answers[0]
        self.btnTrans2.text = self.__answers[1]
        self.btnTrans3.text = self.__answers[2]
        self.btnTrans4.text = self.__answers[3]
        self.btnTrans5.text = self.__answers[4]
        self.btnTrans6.text = self.__answers[5]
        # refresh in dictionary
        self.btn[hash(self.btnTrans1)] = self.btnTrans1.text
        self.btn[hash(self.btnTrans2)] = self.btnTrans2.text
        self.btn[hash(self.btnTrans3)] = self.btnTrans3.text
        self.btn[hash(self.btnTrans4)] = self.btnTrans4.text
        self.btn[hash(self.btnTrans5)] = self.btnTrans5.text
        self.btn[hash(self.btnTrans6)] = self.btnTrans6.text
        
#-----------------------------------------------------------------------        
    def pressButton(self, instance):
        text = self.btn[hash(instance)]
        if self.__words.checkTrans(text):
            self.nextWord()
        else:
            instance.background_color = [1, 0, 0, 1]
            instance.background_normal = ''
        
#-----------------------------------------------------------------------        
    def pressClose(self, instance):
        self.stop()

if __name__ == '__main__':
    KivyWordsApp().run()
