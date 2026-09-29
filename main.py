from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from backend import NUp, split
from pathlib import Path
# from kivy.uix.

class myLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file = [None]
        home = Path.home()
        self.path = f"{home}/pyDouplexer/" 

    def set_file(self, *args):
        self.file = self.ids.file_chooser.selection

    def update_run_btn(self, *args):
        bs = [self.ids.btn1.state, self.ids.btn2.state, self.ids.btn3.state]
        if bs[0] == "down" or bs[1] == "down" or bs[2] == "down":
            if self.file[0] != None :
                self.ids.runButton.disabled = False
            else:
                self.ids.runButton.disabled = True

        else:
            self.ids.runButton.disabled = True

    def call_backend(self, *args):
        if self.ids.btn1.state == "down" and self.ids.btn3.state == "down":
            NUp(self.file[0], rtl=True)
            split(f"{self.path}output.pdf")
        elif self.ids.btn2.state == "down" and self.ids.btn3.state == "down":
            NUp(self.file[0], rtl=False)
            split(f"{self.path}output.pdf")
        elif self.ids.btn1.state == "down":
            NUp(self.file[0], True)
        elif self.ids.btn2.state == "down":
            NUp(self.file[0], False)
        elif self.ids.btn3.state == "down":
            split(self.file[0])

class pdfApp(App):
    def build(self):

        return myLayout()

pdfApp().run()
