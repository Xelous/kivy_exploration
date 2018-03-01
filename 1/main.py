from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label



class Application(App):
	def build(self):
		l_Layout = FloatLayout()
		l_Layout.add_widget(Label(text="hello", size_hint=(.2,.2), pos_hint={'x':.01, 'y':.01}))
		return l_Layout


if __name__ == "__main__":
	Application().run()
