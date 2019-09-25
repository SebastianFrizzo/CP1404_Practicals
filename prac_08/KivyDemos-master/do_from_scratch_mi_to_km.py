from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MI_TO_KM_COEFFICIENT = 1.60934
# KI_TO_MI_COEFFICIENT =


class ConvertMilesToKilometres(App):
	result = StringProperty()

	def build(self):
		Window.size = (700, 300)
		self.title = 'Convert Miles to Kilometres'
		self.root = Builder.load_file('do_from_scratch_mi_to_km.kv')
		return self.root

	def handle_convert_number(self, value):
		validated_value = self.value_validation(value)
		self.result = str(validated_value * MI_TO_KM_COEFFICIENT)
		self.root.ids.output_label.text = str(self.result)

	def handle_increment(self, value, increment_value):
		validated_value = self.value_validation(value)
		validated_value += increment_value
		self.root.ids.input_number.text = str(validated_value)

	def value_validation(self, value):
		try:
			value = float(value)
		except ValueError:
			value = 0.0
		return value


ConvertMilesToKilometres().run()
