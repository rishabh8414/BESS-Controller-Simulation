import os
import pandas as pd
import pandapower as pp
# ... (rest of your imports)

import pandapower.networks as nw
from pandapower import control
from pandapower.timeseries import DFData
from pandapower.timeseries import OutputWriter
from pandapower.timeseries.run_time_series import run_timeseries

# 1. YOUR STORAGE CLASS (The Brain)
class Storage(control.basic_controller.Controller):
    def __init__(self, net, element_index, data_source=None, p_profile=None, in_service=True,
                 recycle=False, order=0, level=0, **kwargs):
        super().__init__(net, in_service=in_service, recycle=recycle, order=order, level=level,
                         initial_run=True)
        
        self.element_index = element_index
        self.bus = net.storage.at[element_index, "bus"]
        self.p_mw = net.storage.at[element_index, "p_mw"]
        self.q_mvar = net.storage.at[element_index, "q_mvar"]
        self.sn_mva = net.storage.at[element_index, "sn_mva"]
        self.name = net.storage.at[element_index, "name"]
        self.gen_type = net.storage.at[element_index, "type"]
        self.in_service = net.storage.at[element_index, "in_service"]
        self.applied = False

        self.max_e_mwh = net.storage.at[element_index, "max_e_mwh"]
        self.soc_percent = net.storage.at[element_index, "soc_percent"] = 0
        
        self.data_source = data_source
        self.p_profile = p_profile
        self.last_time_step = None
        
    def get_stored_energy(self):
        return self.max_e_mwh * self.soc_percent / 100        
    
    def is_converged(self, net):
        return self.applied
    
    def write_to_net(self, net):
        net.storage.at[self.element_index, "p_mw"] = self.p_mw
        net.storage.at[self.element_index, "q_mvar"] = self.q_mvar
        net.storage.at[self.element_index, "soc_percent"]= self.soc_percent
        
    def control_step(self, net):
        self.write_to_net(net)
        self.applied = True
        
    def time_step(self, net, time):
        if self.last_time_step is not None:
            # Updating the State of Charge
            self.soc_percent -= (self.p_mw * (time-self.last_time_step) * 15 / 60) / self.max_e_mwh * 100
        self.last_time_step = time

        if self.data_source:
            if self.p_profile is not None:
                self.p_mw = self.data_source.get_time_step_value(time_step=time, profile_name=self.p_profile)

        self.applied = False 


# 2. THE SIMULATION SETUP (The Body)
def run_bess_simulation():
    # A. Create a standard medium voltage grid from the library
    print("Creating grid...")
    net = nw.mv_oberrhein()

    # B. Add a Battery Storage unit to the grid (at Bus 0)
    # 1 MW power, 2 MWh capacity
    pp.create_storage(net, bus=0, p_mw=0.0, max_e_mwh=2.0, name="My_BESS")

    # C. Create a mock daily profile for the battery (charging and discharging)
    # We will simulate 4 time steps (e.g., 4 periods of 15 mins)
    # Negative values mean charging (drawing from grid), positive means discharging
    battery_schedule = pd.DataFrame({
        "power_profile": [-1.0, -0.5, 0.5, 1.0] 
    })
    
    # D. Convert the pandas DataFrame into a Pandapower data source
    data_source = DFData(battery_schedule)

    # E. Attach your custom Storage controller to the battery
    # element_index=0 refers to the first storage unit we created in step B
    Storage(net, element_index=0, data_source=data_source, p_profile="power_profile")

    # F. Setup an OutputWriter to record the results of the simulation
    # 1. Automatically find the folder where this Python file is saved (your D: drive folder)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # 2. Tell it to create the "results" folder inside that specific directory
    results_path = os.path.join(script_directory, "results")
    # 3. Pass this exact path to the OutputWriter
    ow = OutputWriter(net, time_steps=[0, 1, 2, 3], output_path=results_path)
    ow.log_variable('res_storage', 'p_mw')
    ow.log_variable('storage', 'soc_percent')
    # G. Run the time-series simulation!
    print("Running time-series simulation...")
    run_timeseries(net, time_steps=[0, 1, 2, 3])
    print("Simulation complete. Check the 'results' folder for output files.")

# Execute the simulation
if __name__ == "__main__":
    run_bess_simulation()