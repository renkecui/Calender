import tkinter as tk
from controller import Controller
from view import View
from model import Model

class features:
    WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    def __init__(self):
        pass
    def year_view(self):
        pass
    def month_view(self):
        pass
    def week_view(self):
        pass
    def day_view(self):
        pass
    def add_event(self, event_name, note, add_due_date = False, due_date = None):
        pass
    def show_to_do_list(self):
        pass
    
        
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calendar')
        # create a model
        model = Model('hello@pythontutorial.net')
        # create a view and place it on the root window
        view = View(self)
        view.grid(row=100, column=100, padx=10, pady=10)
        # create a controller
        controller = Controller(model, view)
        # set the controller to view
        view.set_controller(controller)

         