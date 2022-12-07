from Calendar import App

import tkinter as tk
from tkinter import ttk
import datetime
import calendar
'''
class Tasks(tk.Tk):
    
    def __init__(self, name, due_date, description):
        super().__init__()
        
        self.name = name
        self.due_date = due_date
        self.description = description
        
        # create task
        self.create_task(name, due_date, description)
        self.label_task()        
    
    def labels_tasks(self):
        # Tasks Name Label
        tasks_name_label = ttk.Label(self, text = "Name")
        tasks_name_label.grid(column=0, row=7, sticky=tk.W, padx=20, pady=20)
        # Tasks due_date Label
        tasks_due_date_label = ttk.Label(self, text = "Due Date")
        tasks_due_date_label.grid(column=0, row=7, sticky=tk.W, padx=20, pady=20)
        # Tasks description Label
        tasks_description_label = ttk.Label(self, text = "Description")
        tasks_description_label.grid(column=0, row=7, sticky=tk.W, padx=20, pady=20)
        
    def list_of_tasks(self, task):
        task_list = []
        number_of_tasks = len(task_list)
    
    def create_task(self, name, due_date, description):
        
        #task name
        task_name = ttk.Label(self, text = name)
        task_name.grid(column=0, row=7, sticky=tk.W, padx=0, pady=0)
        
        #task due date
        task_due_date = ttk.Label(self, text = due_date)
        task_due_date.grid(column=1, row=7, sticky=tk.W, padx=0, pady=0)
        
        #task description
        task_description = ttk.Label(self, text = description)
        task_description.grid(column=1, row=7, sticky=tk.W, padx=0, pady=0)
'''
class Month:
    def __init__(self, month_num):
        self.month_num = month_num
    def __str__(self):
        months = ['Junuary',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December']
        return months[self.month_num-1]
    
dt = datetime.datetime.now()
current_month = dt.month
current_year = dt.year

class App(tk.Tk):

    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width
        self.geometry(f'{height}x{width}')
        self.title('Calendar')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        self.columnconfigure(7, weight=1)
        
        self.labels_month(current_month)
        self.labels_weekddays()
        self.labels_days(current_year, current_month)
        self.labels_year(current_year)
        self.month_button()
        
        #task 
        self.labels_tasks()
        
        #Tasks
        #self.show_task_list('Homwork 1', '12/12/2022', 'HomeWork')
    
    def labels_month(self, which_month):
        
        
        # Month
        #current_month = dt.month
        month_label = ttk.Label(self, text = Month(which_month))
        month_label.grid(column=3, row=0, sticky=tk.W, padx=0, pady=0)
        
    def labels_weekddays(self):    
        # Weekdays
        # Monday
        monday_label = ttk.Label(self, text = "Mon")
        monday_label.grid(column=0, row=1, sticky=tk.W, padx=15, pady=0)
        # Tuesday
        tuesday_label = ttk.Label(self, text = "Tue")
        tuesday_label.grid(column=1, row=1, sticky=tk.W, padx=0, pady=0)
        # Wednesday
        wednesday_label = ttk.Label(self, text = "Wed")
        wednesday_label.grid(column=2, row=1, sticky=tk.W, padx=0, pady=0)
        # Thursday
        thursday_label = ttk.Label(self, text = "Thur")
        thursday_label.grid(column=3, row=1, sticky=tk.W, padx=0, pady=0)
        # Friday
        friday_label = ttk.Label(self, text = "Fri")
        friday_label.grid(column=4, row=1, sticky=tk.W, padx=0, pady=0)
        # Saturday
        saturday_label = ttk.Label(self, text = "Sat")
        saturday_label.grid(column=5, row=1, sticky=tk.W, padx=0, pady=0)
        # Sunday
        sunday_label = ttk.Label(self, text = "Sun")
        sunday_label.grid(column=6, row=1, sticky=tk.W, padx=0, pady=0)
        
    def labels_days(self, which_year, which_month):
        # Days of the Week
        days = calendar.monthcalendar(which_year, which_month)
        for week in range(len(days)-1):
            for day_of_week in range(len(days[week])):
                #print(days[week])
                #print(days[week][day_of_week])
                if days[week][day_of_week] == 0:
                    ttk.Label(self, text = "||")
                else:
                    day_label = ttk.Label(self, text = days[week][day_of_week])
                    day_label.grid(column=day_of_week, row=week+2, sticky=tk.W, padx=15, pady=0)
        
    def month_button(self):
        # previous month button
        previous_month_button = ttk.Button(self, text="<", command = self.buttons_previous_month)
        previous_month_button.grid(column=2, row=0, sticky=tk.E, padx=0, pady=0)
        
        # next month button
        next_month_button = ttk.Button(self, text=">", command = self.buttons_next_month)
        next_month_button.grid(column=3, row=0, sticky=tk.E, padx=0, pady=0)
    
    def labels_year(self, which_year):    
        # Year
        show_year = ttk.Label(self, text = which_year)
        show_year.grid(column=6, row=0, sticky=tk.W, padx=0, pady=0)
        
        
    def buttons_next_month(self):
        update_month = current_month
        update_year = current_year
        if  current_month == 12:
            update_year = update_year + 1
            update_month = 1
            self.labels_days(update_year, update_month)
            self.labels_month(update_month)
            self.labels_year(update_year)
        else:
            update_year = current_year
            update_month = update_month + 1
            self.labels_days(update_year, update_month)
            self.labels_month(update_month)
            self.labels_year(update_year)
        
    def buttons_previous_month(self):
        update_month = current_month
        update_year = current_year
        if  current_month == 1:
            update_year = update_year - 1
            update_month = 12
            self.labels_days(update_year, update_month)
            self.labels_month(update_month)
            self.labels_year(update_year)
        else:
            update_year = current_year
            update_month = update_month - 1
            self.labels_days(update_year, update_month)
            self.labels_month(update_month)
            self.labels_year(update_year)
        
        
       
    # Tasks     
    def labels_tasks(self):
        # Tasks  Label
        tasks_label = ttk.Label(self, text = "Tasks")
        tasks_label.grid(column=0, row=9, sticky=tk.W, padx=20, pady=20)
        # Tasks Name Label
        tasks_name_label = ttk.Label(self, text = "Name")
        tasks_name_label.grid(column=1, row=9, sticky=tk.W, padx=20, pady=20)
        # Tasks due_date Label
        tasks_due_date_label = ttk.Label(self, text = "Due Date")
        tasks_due_date_label.grid(column=2, row=9, sticky=tk.W, padx=20, pady=20)
        # Tasks description Label
        tasks_description_label = ttk.Label(self, text = "Description")
        tasks_description_label.grid(column=3, row=9, sticky=tk.W, padx=20, pady=20)
    
    def enter_new_task(self):
        pass
    
    def create_task(self, name, due_date, description):
        
        #task name
        task_name = ttk.Label(self, text = name)
        task_name.grid(column=0, row=7, sticky=tk.W, padx=0, pady=0)
        
        #task due date
        task_due_date = ttk.Label(self, text = due_date)
        task_due_date.grid(column=1, row=7, sticky=tk.W, padx=0, pady=0)
        
        #task description
        task_description = ttk.Label(self, text = description)
        task_description.grid(column=1, row=7, sticky=tk.W, padx=0, pady=0)
    '''
    def list_of_tasks(self, task):
        task_list = []
        number_of_tasks = len(task_list)

        '''
#    self.button['command'] = self.button_clicked
 #   self.button.pack()

 # def button_clicked(self):
  #  showinfo(title='Information', message='Hello, Tkinter!')
        
            
if __name__ == "__main__":
    app = App(1000,700)
    app.mainloop()


'''
        # Days of the week
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,  show="*")
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
'''
