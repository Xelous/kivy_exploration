from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

class Gui(App):
	def build(self):
		root = RelativeLayout()
		l_label = Label(text="Hello World")
		root.add_widget(l_label)

		#l_label.to_parent(5, 5);

		print (l_label.get_parent_window())


		#l_label.center_x = -200
		#l_label.center_y = 250
		return root

if __name__ == "__main__":
	Gui().run()
