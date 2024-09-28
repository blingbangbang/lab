 import nidaqmx
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Read from DAQ Device def readdaq():
task = nidaqmx.Task() task.ai_channels.add_ai_thrmcpl_chan("TC01/ai0")
task.start()
value = task.read() task.stop() task.close()
return value
# Write Data Function def writefiledata(t, x):
# Open File
file = open("tempdata.txt", "a")
# Write Data
time = str(t)
value = str(round(x, 2)) file.write(time + "\t" + value) file.write("\n")
# Close File file.close()
# Initialize Logging
Ts = 1 # Sampling Time [seconds]
N = 100
k=1
x_len = N # Number of points to display
Tmin = 15; Tmax = 28
y_range = [Tmin, Tmax] # Range of possible Y values to display data = []
# Create figure for plotting fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) xs = list(range(0, N))
ys = [0] * x_len ax.set_ylim(y_range)
