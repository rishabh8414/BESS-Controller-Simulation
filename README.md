# 🔋 Battery Energy Storage System (BESS) Time-Series Simulation

## 📌 Overview
This project simulates the behavior of a Battery Energy Storage System (BESS) connected to a medium-voltage electrical grid. Built using **Pandapower** and **Python**, it features a custom controller that manages the battery's charging and discharging cycles over a time-series simulation, accurately tracking the State of Charge (SOC) based on active power profiles.

This project bridges electrical grid simulation with data science, demonstrating practical applications in renewable energy systems and grid load management.

## ⚙️ Features
* **Custom BESS Controller:** Implemented a custom Pandapower controller class to govern battery behavior dynamically.
* **Time-Series Simulation:** Simulates grid interactions over 15-minute intervals.
* **Dynamic SOC Calculation:** Accurately calculates the battery's State of Charge (%) based on capacity limits and charging/discharging power (MW).
* **Automated Data Extraction:** Reads raw simulation data (Python Pickle files) and converts it into accessible pandas DataFrames and standard CSV files.
* **Data Visualization:** Generates professional, publication-ready plots of the battery's power profile and SOC curve using Matplotlib.

## 🛠️ Tech Stack
* **Language:** Python
* **Grid Simulation:** Pandapower, NetworkX
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib

---

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/BESS-Controller-Simulation.git](https://github.com/https://github.com/rishabh8414/BESS-Controller-Simulation.git)
cd BESS-Controller-Simulation