import tkinter as tk

def calculate_rmr():
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if gender_var.get() == 1:
            rmr = 10 * weight + 6.25 * height - 5 * age - 161
        else:  # Male
            rmr = 10 * weight + 6.25 * height - 5 * age + 5
        rmr_label.config(text=f"Your Resting Metabolic Rate (RMR) is {rmr:.2f} calories/day.")
    except ValueError:
        rmr_label.config(text="Please enter valid inputs.")

root = tk.Tk()
root.title("RMR Calculator")
gender_label = tk.Label(root, text="Select your gender:")
gender_label.grid(row=0, column=0, sticky="w")
gender_var = tk.IntVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value=0)
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value=1)
male_radio.grid(row=1, column=0, sticky="w")
female_radio.grid(row=1, column=1, sticky="w")
age_label = tk.Label(root, text="Enter your age:")
age_label.grid(row=2, column=0, sticky="w")
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)
weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.grid(row=3, column=0, sticky="w")
weight_entry = tk.Entry(root)
weight_entry.grid(row=3, column=1)
height_label = tk.Label(root, text="Enter your height (cm):")
height_label.grid(row=4, column=0, sticky="w")
height_entry = tk.Entry(root)
height_entry.grid(row=4, column=1)
calculate_button = tk.Button(root, text="Calculate RMR", command=calculate_rmr)
calculate_button.grid(row=5, columnspan=2)
rmr_label = tk.Label(root, text="")
rmr_label.grid(row=6, columnspan=2)
root.mainloop()