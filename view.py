from tkinter import *
from tkinter import messagebox



class View:
    _name = 'Packet Sniffer'
    _resolution = '700x400'

    def __init__(self):
        self.view = Tk()
        self.view.title(self._name)
        self.generate_scroll()
        self.generate_traffic_view()
        self.view.geometry(self._resolution)

    def generate_traffic_view(self):
        self.textarea = Text(self.view, yscrollcommand=self.scroll_bar.set)
        self.textarea.pack(expand=0, fill=BOTH)

    def generate_scroll(self):
        self.scroll_bar = Scrollbar(self.view)
        self.scroll_bar.pack(side=RIGHT, fill="y")

    def add_trafic_record(self, record):
        self.textarea.insert(END, record)
        self.textarea.see(END)

    def update_view(self):
        self.view.update()

