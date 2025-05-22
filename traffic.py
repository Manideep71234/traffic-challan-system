import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re
import os

# Function to validate vehicle number (TG format)
def is_valid_tg_number(number):
    pattern = r'^TG\d{2}[A-Z]{2}\d{4}$'
    return re.match(pattern, number) is not None

# Function to log the results to a file
def log_result(vehicle_number, speed, over_speed, challan):
    log_path = "challan_log.txt"
    with open(log_path, "a") as log_file:
        log_file.write(f"Vehicle: {vehicle_number}, Speed: {speed} km/h, Exceeded: {over_speed} km/h, Fine: ₹{challan}\n")

# Function to check speed and calculate challan
def check_speed():
    vehicle_number = entry_vehicle.get().upper()
    speed_input = entry_speed.get()

    if not is_valid_tg_number(vehicle_number):
        messagebox.showerror("Invalid Vehicle Number", "Please enter vehicle number in format: TG09AB1234")
        return

    if not speed_input.isdigit():
        messagebox.showerror("Invalid Speed", "Please enter a valid numeric speed.")
        return

    speed = int(speed_input)
    speed_limit = 80

    if speed <= speed_limit:
        messagebox.showinfo("Result", "✅ You are under the speed limit. Proceed safely to avoid accidents 😊")
    else:
        over_speed = speed - speed_limit
        if over_speed <= 10:
            challan = 1000
        elif over_speed <= 20:
            challan = 1500
        else:
            challan = 2000

        result = (
            f"🚨 You have crossed the speed limit!\n"
            f"Speed limit: {speed_limit} km/h\n"
            f"Your speed: {speed} km/h\n"
            f"You exceeded by: {over_speed} km/h\n"
            f"Traffic Challan for vehicle {vehicle_number}: ₹{challan}"
        )

        # Show the result in a pop-up
        messagebox.showwarning("Overspeeding", result)

        # Log the result to a file
        log_result(vehicle_number, speed, over_speed, challan)

# GUI window setup
root = tk.Tk()
root.title("Telangana Traffic Challan System")
root.geometry("400x250")

# Style the window with ttk (themed widget)
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 12))

# Labels and input fields
tk.Label(root, text="Enter your vehicle number (TG09AB1234):", font=('Helvetica', 12)).pack(pady=10)
entry_vehicle = tk.Entry(root, font=('Helvetica', 12))
entry_vehicle.pack(pady=5)

tk.Label(root, text="Enter your speed (km/h):", font=('Helvetica', 12)).pack(pady=10)
entry_speed = tk.Entry(root, font=('Helvetica', 12))
entry_speed.pack(pady=5)

# Button to check speed
ttk.Button(root, text="Check Speed", command=check_speed).pack(pady=20)

# Run the GUI loop
root.mainloop()
