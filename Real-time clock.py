import tkinter as tk
from time import strftime

def update_time():
    # Get the current time
    current_time = strftime('%H:%M:%S %p')
    
    # Update the label text
    time_label.config(text=current_time)
    
    # Call the update_time function after 1000 milliseconds (1 second)
    time_label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Real-Time Clock")

# Create a label to display the time
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')

# Pack the label into the window
time_label.pack(anchor='center')

# Call the update_time function to start the clock
update_time()

# Run the Tkinter event loop
root.mainloop()
