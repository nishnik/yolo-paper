import skfuzzy as fuzz
import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(0, 5, 0.01)

mem1 = fuzz.trapmf(x, [0.45, 2, 3, 4.25])
mem2 = fuzz.trapmf(x, [8, 10, 12, 14])
mem3 = fuzz.trapmf(x, [13, 16, 24, 25])

plt.figure(figsize=(10,8))
ax = plt.subplot(111)

ax.plot(x, mem1, 'b', linewidth=1.5, label='Fit')
plt.xticks(np.arange(min(x), max(x)+1, 0.5))
ax.legend()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlabel('Time')
ax.set_ylabel('Membership')

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.show()