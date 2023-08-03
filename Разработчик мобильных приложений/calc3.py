from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '357')
 
class CalculatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    #описаваем вывод формул на главный экран калькулятора
    def add_number(self, instance):
        if (self.formula == '0'):
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()
 
   #дополнительно описываем поведение калькулятора при выборе операции "умножение" и "деление"
    def add_operation(self, instance):
        if(str(instance.text).lower() == 'x'):
            self.formula += '*'
        elif(str(instance.text).lower() == '÷'):
            self.formula += '/'
        else:
            self.formula += str(instance.text)
        self.update_label()
    
    #функция eval() выполняет строку-выражение, переданную ей в качестве обязательного аргумента и возвращает результат выполнения этой строки
    def result(self, instance):
        self.lbl.text = str(eval(self.lbl.text ))
        self.formula = '0'
 
    #стереть формулу полностью
    def clear(self, instance):
        self.formula = '0'
        self.update_label()
 
    #стереть последний символ формулы
    def clearONE(self, instance):
        self.formula = self.formula[:-1] or '0'
        self.update_label()
    
    #построение приложения
    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation = 'vertical')

        gl = GridLayout(cols = 4, rows = 6, padding = [5], spacing = 3, row_force_default = True, row_default_height = 52.65)
 
        self.lbl= TextInput(text='0', halign = 'right', font_size = 40, multiline=False)
        self.lbl.size_hint_y = None # для правильного выставления высоты
        self.lbl.height = 70
       
        #описываем каждую кнопку: текст, действие при нажатие, цвет и размер
        gl.add_widget(Button(text = 'clear', on_press = self.clear,    background_color = [0.26, .48, 0, 1] , background_normal = '', font_size = 25))
        gl.add_widget(Button(text = '('  , on_press = self.add_number, background_color = [.2, .2, .2, 1],    background_normal = '', font_size = 21))
        gl.add_widget(Button(text = ')'  , on_press = self.add_number, background_color = [.2, .2, .2, 1],    background_normal = '', font_size = 23))
        # gl.add_widget(Button(text = 'del', on_press = self.clearONE,   background_color = [0.26, .48, 0, 1] , background_normal = '', font_size = 25))
        gl.add_widget(Button(text = '÷', on_press = self.add_operation,   background_color = [0.4, .4, 0, 1] , background_normal = '', font_size = 25))
        
        gl.add_widget(Button(text = '7', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '8', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '9', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = 'x', on_press = self.add_operation, background_color = [0.4, .4, 0, 1], background_normal = '', font_size = 21))
        
        gl.add_widget(Button(text = '4', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '5', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '6', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '-', on_press = self.add_operation, background_color = [0.4, .4, 0, 1], background_normal = '', font_size = 30))
        
        gl.add_widget(Button(text = '1', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '2', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '3', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '+', on_press = self.add_operation, background_color = [0.4, .4, 0, 1], background_normal = '', font_size = 21))
 
        gl.add_widget(Button(text = '00', on_press = self.add_number,background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '0', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '.', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '=', on_press = self.result,     background_color = [0.4, .4, 0, 1], background_normal = '', font_size = 21))
        
        bl.add_widget(self.lbl)


        bl.add_widget(gl)
        return bl
 
if __name__ == "__main__":
    CalculatorApp().run()