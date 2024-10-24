from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.core.text import LabelBase

LabelBase.register(name='americorps',
                   fn_regular='americorps.ttf'
                   )

class CalcBox(BoxLayout):
    btn_1 = ObjectProperty(None)
    btn_2 = ObjectProperty
    btn_3 = ObjectProperty
    btn_4 = ObjectProperty
    btn_5 = ObjectProperty
    btn_6 = ObjectProperty
    btn_7 = ObjectProperty
    btn_8 = ObjectProperty
    btn_9 = ObjectProperty
    btn_10 = ObjectProperty
    btn_11 = ObjectProperty
    btn_12 = ObjectProperty
    btn_13 = ObjectProperty
    btn_14 = ObjectProperty
    btn_15 = ObjectProperty
    btn_16 = ObjectProperty
    btn_17 = ObjectProperty
    btn_18 = ObjectProperty
    btn_19 = ObjectProperty
    display = StringProperty

    def equal(self):
        try:
            if self.display.text == '21 / 08 / 15':
                self.display.text = 'Amantor <3'
                return
            self.countList = []
            self.count = ''
            if self.display.text == '':
                return
            elif self.display.text[len(self.display.text) - 1] == ' ':
                self.display.text = self.display.text[:(len(self.display.text) - 3)]
                self.display.text += 'e'
            else:
                self.display.text += 'e'
            for x in self.display.text:
                if x == '':
                    pass
                elif x == 'e':
                    self.countList.append(self.count)
                elif x != '+' and x != '-' and x != 'x' and x != '/':
                    self.count += x
                else:
                    self.countList.append(self.count)
                    self.countList.append(x)
                    self.count = ''
            while len(self.countList) != 1:
                if 'x' in self.countList or '/' in self.countList:
                    for x in range(len(self.countList)):
                        if self.countList[x] == 'x':
                            self.countList[x] = float(self.countList[x - 1]) * float(self.countList[x + 1])
                            del self.countList[x + 1]
                            del self.countList[x - 1]
                            break
                        elif self.countList[x] == '/':
                            self.countList[x] = float(self.countList[x - 1]) / float(self.countList[x + 1])
                            del self.countList[x + 1]
                            del self.countList[x - 1]
                            break


                elif '+' in self.countList or '-' in self.countList:
                    for x in range(len(self.countList)):
                        if self.countList[x] == '+':
                            self.countList[x] = float(self.countList[x - 1]) + float(self.countList[x + 1])
                            del self.countList[x + 1]
                            del self.countList[x - 1]
                            break
                        elif self.countList[x] == '-':
                            if x == 1 and self.countList[x - 1] == ' ' or x == 1 and self.countList[x - 1] == '':
                                self.countList[x] = - (float(self.countList[x + 1]))
                                del self.countList[x + 1]
                                del self.countList[x - 1]
                            else:
                                self.countList[x] = float(self.countList[x - 1]) - float(self.countList[x + 1])
                                del self.countList[x + 1]
                                del self.countList[x - 1]
                            break
            self.display.text = str(self.countList[0])
        except:
            self.display.text = 'ERRO'

    def plus_click(self):
        if len(self.display.text) - 1 > -1:
            if self.display.text[len(self.display.text) - 1] == ' ' or self.display.text[len(self.display.text) - 1] == '.':
                pass
            else:
                self.display.text += ' + '

    def minus_click(self):
        if self.display.text == '':
            self.display.text += ' - '
        elif self.display.text[len(self.display.text) - 1] == ' ' or self.display.text[len(self.display.text) - 1] == '.':
            pass
        else:
            self.display.text += ' - '

    def mult_click(self):
        if len(self.display.text) - 1 > -1:
            if self.display.text[len(self.display.text) - 1] == ' ' or self.display.text[len(self.display.text) - 1] == '.':
                pass
            else:
                self.display.text += ' x '

    def div_click(self):
        if len(self.display.text) - 1 > -1:
            if self.display.text[len(self.display.text) - 1] == ' ' or self.display.text[len(self.display.text) - 1] == '.':
                pass
            else:
                self.display.text += ' / '

    def dot_click(self):
        if self.display.text == '':
            self.display.text += '.'
        elif self.display.text[len(self.display.text) - 1] == '.':
            pass
        else:
            self.display.text += '.'

    def update(self, dt):
        #BUTTON 1 and display
        if self.btn_1.background_color[0] >= 1 and self.btn_1.background_color[1] <= 1 and self.btn_1.background_color[2] <= 0:
            self.btn_1.background_color[1] += .01
            self.display.background_color[1] += .01
        elif self.btn_1.background_color[0] >= 0 and self.btn_1.background_color[1] >= 1 and self.btn_1.background_color[2] <= 0:
            self.btn_1.background_color[0] -= .01
            self.display.background_color[0] -= .01
        elif self.btn_1.background_color[0] <= 0 and self.btn_1.background_color[1] >= 1 and self.btn_1.background_color[2] <= 1:
            self.btn_1.background_color[2] += .01
            self.display.background_color[2] += .01
        elif self.btn_1.background_color[0] <= 0 and self.btn_1.background_color[1] >= 0 and self.btn_1.background_color[2] >= 1:
            self.btn_1.background_color[1] -= .01
            self.display.background_color[1] -= .01
        elif self.btn_1.background_color[0] <= 1 and self.btn_1.background_color[1] <= 0 and self.btn_1.background_color[2] >= 1:
            self.btn_1.background_color[0] += .01
            self.display.background_color[0] += .01
        else:
            self.btn_1.background_color[2] -= .01
            self.display.background_color[2] -= .01
            
        #BUTTON 2 and 5
        if self.btn_2.background_color[0] >= 1 and self.btn_2.background_color[1] <= 1 and self.btn_2.background_color[2] <= 0:
            self.btn_2.background_color[1] += .01
            self.btn_5.background_color[1] += .01
        elif self.btn_2.background_color[0] >= 0 and self.btn_2.background_color[1] >= 1 and self.btn_2.background_color[2] <= 0:
            self.btn_2.background_color[0] -= .01
            self.btn_5.background_color[0] -= .01
        elif self.btn_2.background_color[0] <= 0 and self.btn_2.background_color[1] >= 1 and self.btn_2.background_color[2] <= 1:
            self.btn_2.background_color[2] += .01
            self.btn_5.background_color[2] += .01
        elif self.btn_2.background_color[0] <= 0 and self.btn_2.background_color[1] >= 0 and self.btn_2.background_color[2] >= 1:
            self.btn_2.background_color[1] -= .01
            self.btn_5.background_color[1] -= .01
        elif self.btn_2.background_color[0] <= 1 and self.btn_2.background_color[1] <= 0 and self.btn_2.background_color[2] >= 1:
            self.btn_2.background_color[0] += .01
            self.btn_5.background_color[0] += .01
        else:
            self.btn_2.background_color[2] -= .01
            self.btn_5.background_color[2] -= .01
            
        #BUTTON 3, 6, 9
        if self.btn_3.background_color[0] >= 1 and self.btn_3.background_color[1] <= 1 and self.btn_3.background_color[2] <= 0:
            self.btn_3.background_color[1] += .01
            self.btn_6.background_color[1] += .01
            self.btn_9.background_color[1] += .01
        elif self.btn_3.background_color[0] >= 0 and self.btn_3.background_color[1] >= 1 and self.btn_3.background_color[2] <= 0:
            self.btn_3.background_color[0] -= .01
            self.btn_6.background_color[0] -= .01
            self.btn_9.background_color[0] -= .01
        elif self.btn_3.background_color[0] <= 0 and self.btn_3.background_color[1] >= 1 and self.btn_3.background_color[2] <= 1:
            self.btn_3.background_color[2] += .01
            self.btn_6.background_color[2] += .01
            self.btn_9.background_color[2] += .01
        elif self.btn_3.background_color[0] <= 0 and self.btn_3.background_color[1] >= 0 and self.btn_3.background_color[2] >= 1:
            self.btn_3.background_color[1] -= .01
            self.btn_6.background_color[1] -= .01
            self.btn_9.background_color[1] -= .01
        elif self.btn_3.background_color[0] <= 1 and self.btn_3.background_color[1] <= 0 and self.btn_3.background_color[2] >= 1:
            self.btn_3.background_color[0] += .01
            self.btn_6.background_color[0] += .01
            self.btn_9.background_color[0] += .01
        else:
            self.btn_3.background_color[2] -= .01
            self.btn_6.background_color[2] -= .01
            self.btn_9.background_color[2] -= .01
            
        #BUTTON 4, 7, 10, 13
        if self.btn_4.background_color[0] >= 1 and self.btn_4.background_color[1] <= 1 and self.btn_4.background_color[2] <= 0:
            self.btn_4.background_color[1] += .01
            self.btn_7.background_color[1] += .01
            self.btn_10.background_color[1] += .01
            self.btn_13.background_color[1] += .01
        elif self.btn_4.background_color[0] >= 0 and self.btn_4.background_color[1] >= 1 and self.btn_4.background_color[2] <= 0:
            self.btn_4.background_color[0] -= .01
            self.btn_7.background_color[0] -= .01
            self.btn_10.background_color[0] -= .01
            self.btn_13.background_color[0] -= .01
        elif self.btn_4.background_color[0] <= 0 and self.btn_4.background_color[1] >= 1 and self.btn_4.background_color[2] <= 1:
            self.btn_4.background_color[2] += .01
            self.btn_7.background_color[2] += .01
            self.btn_10.background_color[2] += .01
            self.btn_13.background_color[2] += .01
        elif self.btn_4.background_color[0] <= 0 and self.btn_4.background_color[1] >= 0 and self.btn_4.background_color[2] >= 1:
            self.btn_4.background_color[1] -= .01
            self.btn_7.background_color[1] -= .01
            self.btn_10.background_color[1] -= .01
            self.btn_13.background_color[1] -= .01
        elif self.btn_4.background_color[0] <= 1 and self.btn_4.background_color[1] <= 0 and self.btn_4.background_color[2] >= 1:
            self.btn_4.background_color[0] += .01
            self.btn_7.background_color[0] += .01
            self.btn_10.background_color[0] += .01
            self.btn_13.background_color[0] += .01
        else:
            self.btn_4.background_color[2] -= .01
            self.btn_7.background_color[2] -= .01
            self.btn_10.background_color[2] -= .01
            self.btn_13.background_color[2] -= .01
            
        #BUTTON 8, 11, 14, 17
        if self.btn_8.background_color[0] >= 1 and self.btn_8.background_color[1] <= 1 and self.btn_8.background_color[2] <= 0:
            self.btn_8.background_color[1] += .01
            self.btn_11.background_color[1] += .01
            self.btn_14.background_color[1] += .01
            self.btn_17.background_color[1] += .01
        elif self.btn_8.background_color[0] >= 0 and self.btn_8.background_color[1] >= 1 and self.btn_8.background_color[2] <= 0:
            self.btn_8.background_color[0] -= .01
            self.btn_11.background_color[0] -= .01
            self.btn_14.background_color[0] -= .01
            self.btn_17.background_color[0] -= .01
        elif self.btn_8.background_color[0] <= 0 and self.btn_8.background_color[1] >= 1 and self.btn_8.background_color[2] <= 1:
            self.btn_8.background_color[2] += .01
            self.btn_11.background_color[2] += .01
            self.btn_14.background_color[2] += .01
            self.btn_17.background_color[2] += .01
        elif self.btn_8.background_color[0] <= 0 and self.btn_8.background_color[1] >= 0 and self.btn_8.background_color[2] >= 1:
            self.btn_8.background_color[1] -= .01
            self.btn_11.background_color[1] -= .01
            self.btn_14.background_color[1] -= .01
            self.btn_17.background_color[1] -= .01
        elif self.btn_8.background_color[0] <= 1 and self.btn_8.background_color[1] <= 0 and self.btn_8.background_color[2] >= 1:
            self.btn_8.background_color[0] += .01
            self.btn_11.background_color[0] += .01
            self.btn_14.background_color[0] += .01
            self.btn_17.background_color[0] += .01
        else:
            self.btn_8.background_color[2] -= .01
            self.btn_11.background_color[2] -= .01
            self.btn_14.background_color[2] -= .01
            self.btn_17.background_color[2] -= .01
            
        #BUTTON 12, 15, 18
        if self.btn_12.background_color[0] >= 1 and self.btn_12.background_color[1] <= 1 and self.btn_12.background_color[2] <= 0:
            self.btn_12.background_color[1] += .01
            self.btn_15.background_color[1] += .01
            self.btn_18.background_color[1] += .01
        elif self.btn_12.background_color[0] >= 0 and self.btn_12.background_color[1] >= 1 and self.btn_12.background_color[2] <= 0:
            self.btn_12.background_color[0] -= .01
            self.btn_15.background_color[0] -= .01
            self.btn_18.background_color[0] -= .01
        elif self.btn_12.background_color[0] <= 0 and self.btn_12.background_color[1] >= 1 and self.btn_12.background_color[2] <= 1:
            self.btn_12.background_color[2] += .01
            self.btn_15.background_color[2] += .01
            self.btn_18.background_color[2] += .01
        elif self.btn_12.background_color[0] <= 0 and self.btn_12.background_color[1] >= 0 and self.btn_12.background_color[2] >= 1:
            self.btn_12.background_color[1] -= .01
            self.btn_15.background_color[1] -= .01
            self.btn_18.background_color[1] -= .01
        elif self.btn_12.background_color[0] <= 1 and self.btn_12.background_color[1] <= 0 and self.btn_12.background_color[2] >= 1:
            self.btn_12.background_color[0] += .01
            self.btn_15.background_color[0] += .01
            self.btn_18.background_color[0] += .01
        else:
            self.btn_12.background_color[2] -= .01
            self.btn_15.background_color[2] -= .01
            self.btn_18.background_color[2] -= .01
            
        #BUTTON 16 and 19
        if self.btn_16.background_color[0] >= 1 and self.btn_16.background_color[1] <= 1 and self.btn_16.background_color[2] <= 0:
            self.btn_16.background_color[1] += .01
            self.btn_19.background_color[1] += .01
        elif self.btn_16.background_color[0] >= 0 and self.btn_16.background_color[1] >= 1 and self.btn_16.background_color[2] <= 0:
            self.btn_16.background_color[0] -= .01
            self.btn_19.background_color[0] -= .01
        elif self.btn_16.background_color[0] <= 0 and self.btn_16.background_color[1] >= 1 and self.btn_16.background_color[2] <= 1:
            self.btn_16.background_color[2] += .01
            self.btn_19.background_color[2] += .01
        elif self.btn_16.background_color[0] <= 0 and self.btn_16.background_color[1] >= 0 and self.btn_16.background_color[2] >= 1:
            self.btn_16.background_color[1] -= .01
            self.btn_19.background_color[1] -= .01
        elif self.btn_16.background_color[0] <= 1 and self.btn_16.background_color[1] <= 0 and self.btn_16.background_color[2] >= 1:
            self.btn_16.background_color[0] += .01
            self.btn_19.background_color[0] += .01
        else:
            self.btn_16.background_color[2] -= .01
            self.btn_19.background_color[2] -= .01
            

class CalcApp(App):
    def build(self):
        calculator = CalcBox()
        Clock.schedule_interval(calculator.update, .01)
        return calculator

if __name__ == '__main__':
    CalcApp().run()