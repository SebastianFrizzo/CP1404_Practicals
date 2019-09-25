from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometres(App):
    def build(self):
        Window.size = (900, 400)
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('do_from_scratch_mi_to_km.kv')
        return self.root

    def handle_convert_number(self, value):
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    # def handle_increase_counter(self, value):
    #     value += 1
    #     self.root.ids.input_number.text = value
    #
    # def handle_decrease_counter(self, value):
    #     value -= 1
    #     self.root.ids.input_number.text = value


ConvertMilesToKilometres().run()