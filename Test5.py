import tkinter as tk
from tkinter import ttk
import datetime
import calendar

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
    
class App(tk.Tk):#, Month):

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
        
        self.labels()
    
    def labels(self):
        
        dt = datetime.datetime.now()
        # Month
        current_month = dt.month
        month_label = ttk.Label(self, text = Month(current_month))
        month_label.grid(column=3, row=0, sticky=tk.W, padx=0, pady=0)
        
        
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
        # Days of the Week
        current_year = dt.year
        days = calendar.monthcalendar(current_year, current_month)
        for week in range(len(days)-1):
            for day_of_week in range(len(days[week])):
                #print(days[week])
                #print(days[week][day_of_week])
                if days[week][day_of_week] == 0:
                    ttk.Label(self, text = "")
                else:
                    day_label = ttk.Label(self, text = days[week][day_of_week])
                    day_label.grid(column=day_of_week, row=week+2, sticky=tk.W, padx=15, pady=0)
        
        
        # previous month button
        previous_month_button = ttk.Button(self, text="<")
        previous_month_button.grid(column=2, row=0, sticky=tk.E, padx=0, pady=0)
        
        # next month button
        next_month_button = ttk.Button(self, text=">")
        next_month_button.grid(column=4, row=0, sticky=tk.E, padx=0, pady=0)
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
