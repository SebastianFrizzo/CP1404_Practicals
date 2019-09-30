from kivy.app import App
from kivy.lang import Builder


class Grader(App):
    def build(self):
        self.title = "Pass or Fail Grader"
        self.root = Builder.load_file('grader.kv')
        return self.root

    def handle_grade(self):
        if float(self.root.ids.input_name.text) > 100:
            self.root.ids.output_label.text = 'Invalid'
        elif float(self.root.ids.input_name.text) >= 85:
            self.root.ids.output_label.text = 'HD'
        elif float(self.root.ids.input_name.text) >= 75:
            self.root.ids.output_label.text = 'D'
        elif float(self.root.ids.input_name.text) >= 65:
            self.root.ids.output_label.text = 'C'
        elif float(self.root.ids.input_name.text) >= 50:
            self.root.ids.output_label.text = 'Pass'
        else:
            self.root.ids.output_label.text = 'Fail'

    def handle_clear(self):
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


Grader().run()
