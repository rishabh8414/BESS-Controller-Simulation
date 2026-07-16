# 🔋 Battery Energy Storage System (BESS) Time-Series Simulation

## 📌 Overview
This project simulates the behavior of a Battery Energy Storage System (BESS) connected to a medium-voltage electrical grid. Built using **Pandapower** and **Python**, it features a custom controller that manages the battery's charging and discharging cycles over a time-series simulation, accurately tracking the State of Charge (SOC) based on active power profiles.

This project bridges electrical grid simulation with data science, demonstrating practical applications in renewable energy systems and grid load management.

## ⚙️ Features
- **Custom BESS Controller:** Implemented a custom Pandapower controller class to govern battery behavior dynamically.
- **Time-Series Simulation:** Simulates grid interactions over 15-minute intervals.
- **Dynamic SOC Calculation:** Accurately calculates the battery's State of Charge (%) based on capacity limits and charging/discharging power (MW).
- **Automated Data Extraction:** Reads raw simulation data (Python Pickle files) and converts it into accessible pandas DataFrames and standard CSV files.
- **Data Visualization:** Generates professional, publication-ready plots of the battery's power profile and SOC curve using Matplotlib.

## 🛠️ Tech Stack
- **Language:** Python
- **Grid Simulation:** Pandapower, NetworkX
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/rishabh8414/BESS-Controller-Simulation.git
cd BESS-Controller-Simulation
```

### 2. Install required dependencies
Ensure you have Python installed, then run:

```bash
pip install pandapower pandas numpy matplotlib numba
```

## 💻 Usage
The project is broken down into three main scripts for modularity:

### 1. Run the simulation
Executes the power grid simulation and saves the raw data to a local `/results` folder.

```bash
python bess_simulation.py
```

### 2. View and export results
Reads the generated `.p` (Pickle) files, prints the tabular data to the console, and exports a clean `soc_results_excel.csv` file.

```bash
python view_results.py
```

### 3. Generate visualizations
Creates a side-by-side graph of the Power Output and State of Charge, saving the output as `bess_performance_graph.png`.

```bash
python plot_results.py
```

## 📊 Simulation Results
The simulation executes a predefined power schedule over four 15-minute intervals.

- **Negative Power:** Battery acts as a load (Charging).
- **Positive Power:** Battery acts as a generator (Discharging).

<img width="3600" height="1500" alt="bess_performance_graph" src="https://github.com/user-attachments/assets/e8b9f934-2950-4437-8214-3da0c3d062b8" />

## 👨‍💻 Author
**Rushabh Sutariya**  
Master of Engineering, Renewable Energy Systems

- LinkedIn: [rushabh_sutariya](www.linkedin.com/in/rushabh-sutariya-337b33257)
- Email: [rushabhsutariya6.de@gmail.com](mailto:rushabhsutariya6.de@gmail.com)
