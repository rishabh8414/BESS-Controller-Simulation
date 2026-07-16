import pandas as pd
import os

# 1. Automatically find your results folder
script_directory = os.path.dirname(os.path.abspath(__file__))
soc_file_path = os.path.join(script_directory, "results", "storage", "soc_percent.p")
power_file_path = os.path.join(script_directory, "results", "res_storage", "p_mw.p")

# 2. Read the Pickle (.p) files using Pandas
print("Reading Python Pickle files...\n")
soc_data = pd.read_pickle(soc_file_path)
power_data = pd.read_pickle(power_file_path)

# 3. Print the results to your terminal so you can see them!
print("--- BATTERY POWER OUTPUT (MW) ---")
print("Negative = Charging | Positive = Discharging")
print(power_data)
print("\n")

print("--- BATTERY STATE OF CHARGE (%) ---")
print("How full the battery is at each 15-min time step")
print(soc_data)
print("\n")

# 4. Convert and save them as standard CSV files for Excel
csv_output_path = os.path.join(script_directory, "results", "soc_results_excel.csv")
soc_data.to_csv(csv_output_path)
print(f"Success! A standard CSV file has been saved at: {csv_output_path}")