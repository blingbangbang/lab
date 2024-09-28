import nidaqmx
import time
import numpy as np
import matplotlib.pyplot as plt

# Initialize Logging
Tstop = 10 # Logging Time [seconds]
Ts = 2 # Sampling Time [seconds]
N = int(Tstop/Ts)
data = []

# Initialize DAQ Device
task = nidaqmx.Task()
task.ai_channels.add_ai_thrmcpl_chan("TC01/ai 0")
task.start()

# Open File
file = open("tempdata.txt", "w")

# Write Data Function
def writefiledata(t, x):
    time = str(t)
    value = str(round(x, 2))
    file.write(time + "\t" + value)
    file.write("\n")
  
# Logging Temperature Data from DAQ Device
for k in range(N):
    value = task.read()
    print("T =", round(value,1), "[degC]")
    data.append(value)
    time.sleep(Ts)
    writefiledata(k*Ts, value)
  
# Terminate DAQ Device
task.stop()
task.close()

# Close File
file.close()

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
