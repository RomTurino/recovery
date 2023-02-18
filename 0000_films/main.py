from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ScreenMain(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=10, padding=[100])

        button_new_pasword = Button(
            text="New Pasword",
            background_color=[0, 1.5, 3, 1],
            size_hint=[1, 0.1],
            pos = (20, 100),
            on_press=self._on_press_button_new_pasword,
        )
        button_new_pasword2 = Button(
            text="New Pasword",
            background_color=[0, 1.5, 3, 1],
            size_hint=[1, 0.1],
            pos = (20, 150),
            on_press=self._on_press_button_new_pasword,
        )
        boxlayout.add_widget(button_new_pasword)
        boxlayout.add_widget(button_new_pasword2)
        self.add_widget(boxlayout)

    def _on_press_button_new_pasword(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'lenpasword'


class LenPasword(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        button_new_pasword = Button(
            text="Return",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_new_pasword,
        )

        boxlayout.add_widget(button_new_pasword)
        self.add_widget(boxlayout)

    def _on_press_button_new_pasword(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'


class PaswordingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='main_screen'))
        sm.add_widget(LenPasword(name='lenpasword'))

        return sm

# if __name__ == "__main__":
#     PaswordingApp().run()

# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

# Глобальные настройки
Window.size = (400, 600)
Window.clearcolor = (110/255, 217/255, 106/255, 1)
Window.title = "Конвертер"


class MyApp(App):
	
	# Создание всех виджетов (объектов)
	def __init__(self):
		super().__init__()
		self.label = Label(text='Конвертер')
		self.miles = Label(text='Мили')
		self.metres = Label(text='Метры')
		self.santimetres = Label(text='Сантиметры')
		self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)
		self.input_data.bind(text=self.on_text) # Добавляем обработчик события

	# Получаем данные и производит их конвертацию
	def on_text(self, *args):
		data = self.input_data.text
		if data.isnumeric():
			self.miles.text = 'Мили: ' + str(float(data) * 0.62)
			self.metres.text = 'Метры: ' + str(float(data) * 1000)
			self.santimetres.text = 'Сантиметры: ' + str(float(data) * 100000)
		else:
			self.input_data.text = ''

	# Основной метод для построения программы
	def build(self):
		# Все объекты будем помещать в один общий слой
		box = BoxLayout(orientation='vertical')
		box.add_widget(self.label)
		box.add_widget(self.input_data)
		box.add_widget(self.miles)
		box.add_widget(self.metres)
		box.add_widget(self.santimetres)

		return box


# Запуск проекта
if __name__ == "__main__":
	MyApp().run()