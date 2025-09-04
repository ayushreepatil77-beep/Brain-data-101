import pandas as pd
import matplotlib.pyplot as plt

data = {
    'time(ms)': [0, 1, 2, 3, 4],
    'firing_rate(Hz)': [5, 6, 7, 10, 4]
}

df = pd.DataFrame(data)
print(df)

plt.plot(df['time(ms)'], df['firing_rate(Hz)'], marker='o')
plt.xlabel('Time (ms)')
plt.ylabel('Firing Rate (Hz)')
plt.title('Neuron Activity Over Time')
plt.show()
