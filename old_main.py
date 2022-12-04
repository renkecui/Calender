from Calendar import features
# Calendar app functions
# Default displays is a month view 

# Displays a menu to the user that will 
# allow them to choose from the following:
# Show Year view
# Show Month view
# Show Week View
# SHow Day View
# Add an event 
# Show To-Do List
# Exit

menu = {
'1' : "Year View",
'2' : "Month View",
'3' : "Week View",
'4' : "Day Viewr",
'5' : "Add event",
'6' : "Show To-Do List",
'7' : "Exit"}

print("")
for key, value in menu.items():
        print(key, ' : ', value)
print("")
while True:
    selection = input("Please Select a Menu Option: ")    
    if selection =='1': 
        # Show a Year view of Calendar
        pass
    elif selection == '2': 
        # Show a Month view of Calendar
        pass
    elif selection == '3':
        # Show a Week view of Calendar
        pass
    elif selection == '4': 
        # Show a Day view of Calendar
        pass
    elif selection == '5': 
        # Add event
        pass
    elif selection == '6': 
        # Show To-Do List
        pass
    elif selection == '7': 
        # Exit Application
        break
    else: 
        print("Unknown Option Selected!")
            