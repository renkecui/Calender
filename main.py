from Calendar import App
from tkinter import Text
import tkinter as tk
from tkinter import ttk
import datetime
import calendar
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror


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
task_list = []
reminder_list = []
class App(tk.Tk):

    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width
        self.geometry(f'{height}x{width}')
        self.title('Calendar')
        #self.resizable(0, 0)

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
        self.task_check_marks()
        self.labels_tasks()
        self.enter_new_task()
        #self.task_number()
        self.enter_task_button()
        
        
        #reminders
        self.reminder_label()
        self.enter_reminder_button()
        self.add_reminder()
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
        monday_label.grid(column=0, row=1, sticky=tk.W, padx=10, pady=0)
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
        for week in range(len(days)):
            for day_of_week in range(len(days[week])):
                #print(days[week])
                #print(days[week][day_of_week])
                if days[week][day_of_week] == 0:
                    ttk.Label(self, text = "||")
                else:
                    #print(day_of_week)
                    day_label = ttk.Label(self, text = days[week][day_of_week])
                    day_label.grid(column=day_of_week, row=week+2, sticky=tk.W, padx=0, pady=0)
        
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
 
    def task_check_marks(self):
        tasks_done = ttk.Label(self, text = "Completed?")
        tasks_done.grid(column=0, row=9, sticky=tk.W, padx=10, pady=10)
        tasks_done_spacer = ttk.Label(self, text = "  --")
        tasks_done_spacer.grid(column=0, row=10, sticky=tk.W, padx=10, pady=10)

    def labels_tasks(self):
        tasks_number_spacer = ttk.Label(self, text = "  --")
        tasks_number_spacer.grid(column=1, row=10, sticky=tk.W, padx=0, pady=10)
        # Tasks  Label
        tasks_label = ttk.Label(self, text = "Tasks")
        tasks_label.grid(column=1, row=9, sticky=tk.W, padx=0, pady=10)
        # Tasks Name Label
        tasks_name_label = ttk.Label(self, text = "Name")
        tasks_name_label.grid(column=2, row=9, sticky=tk.W, padx=0, pady=10)
        # Tasks due_date Label
        tasks_due_date_label = ttk.Label(self, text = "Due Date")
        tasks_due_date_label.grid(column=3, row=9, sticky=tk.W, padx=0, pady=10)
        # Tasks description Label
        tasks_description_label = ttk.Label(self, text = "Description")
        tasks_description_label.grid(column=4, row=9, sticky=tk.W, padx=0, pady=10)

    # Adding a Task
    def enter_new_task(self):
        # Name
        self.text_name = tk.StringVar()
        entry_text_name = ttk.Entry(self, textvariable = self.text_name)
        entry_text_name.grid(column=2, row=10, sticky=tk.W, padx=0, pady=0)
        #entry_text_name.insert('1.0', 'Enter the Task name...')
        # Due Date
        self.text_due_date = tk.StringVar()
        entry_text_due_date = ttk.Entry(self, textvariable = self.text_due_date)
        entry_text_due_date.grid(column=3, row=10, sticky=tk.W, padx=0, pady=0)
        #entry_text_due_date.insert('1.0', 'Enter the Task due date...')

        # Description
        self.text_description = tk.StringVar()
        entry_text_description = ttk.Entry(self, textvariable = self.text_description)
        entry_text_description.grid(column=4, row=10, sticky=tk.W, padx=0, pady=0)
        #entry_text_description.insert('1.0', 'Enter the Task description...')
    
    def enter_task_button(self):
        Enter_task = ttk.Button(self, text='Enter task', command = self.create_new_task)
        Enter_task.grid(column=5, row=10, sticky='W')
    
    def create_new_task(self):
        task_list.append(self.text_name.get())
        #check box
        task_checkbox = ttk.Checkbutton(self)
        task_checkbox.grid(column=0, row=len(task_list)+10, sticky=tk.W, padx=10, pady=0)
        #task number
        task_num = ttk.Label(self, text = len(task_list))
        task_num.grid(column=1, row=len(task_list)+10, sticky=tk.W, padx=0, pady=0)
        # name
        task1 = ttk.Label(self, text = self.text_name.get())
        task1.grid(column=2, row=len(task_list)+10, sticky=tk.W, padx=0, pady=0)
        # due_date
        task1 = ttk.Label(self, text = self.text_due_date.get())
        task1.grid(column=3, row=len(task_list)+10, sticky=tk.W, padx=0, pady=0)
        # descrption
        task1 = ttk.Label(self, text = self.text_description.get())
        task1.grid(column=4, row=len(task_list)+10, sticky=tk.W, padx=0, pady=0)
    
    # Reminders 
    def reminder_label(self):
        reminder_list_label= ttk.Label(self, text = "Reminders:")
        reminder_list_label.grid(column=6, row=9, sticky=tk.W, padx=0, pady=0)
        
    def add_reminder(self):
        self.reminder_item = tk.StringVar()
        reminder_label_title = ttk.Entry(self, textvariable = self.reminder_item)
        reminder_label_title.grid(column=6, row=10, sticky=tk.W, padx=0, pady=0)
    
    def enter_reminder_button(self):
        enter_reminder = ttk.Button(self, text='Enter reminder', command = self.reminder_item_label)
        enter_reminder.grid(column=7, row=10, sticky='W')
        
    def reminder_item_label(self):
        reminder_list.append(self.reminder_item.get())
        reminder_item = ttk.Label(self, text = self.reminder_item.get())
        reminder_item.grid(column=6, row=len(reminder_list)+10, sticky=tk.W, padx=0, pady=0)
            
            
if __name__ == "__main__":
    app = App(1200,800)
    app.mainloop()

