import nidaqmx
import time
import numpy as np
import matplotlib.pyplot as plt

# Initialize Logging
Tstop = 60 # Logging Time [seconds]
Ts = 2 # Sampling Time [seconds]
N = int(Tstop/Ts)
data = []

# Initialize DAQ Device
task = nidaqmx.Task()
task.ai_channels.add_ai_thrmcpl_chan("TC01/ai0")
task.start()

#Logging Temperature Data from DAQ Device
for k in range(N):
    value = task.read()
    print("T =", round(value,1), "[degC]")
    data.append(value)
    time.sleep(Ts)
  
# Terminate DAQ Device
task.stop()
task.close()

# Plotting
t = np.arange(0,Tstop,Ts)
plt.plot(t,data, "-o")
plt.title('Temperature')
plt.xlabel('t [s]')
plt.ylabel('Temp [degC]')
plt.grid()
Tmin = 18; Tmax = 28
plt.axis([0, Tstop, Tmin, Tmax])
plt.show()
