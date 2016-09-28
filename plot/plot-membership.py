import skfuzzy as fuzz
import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(0, 5, 0.01)

mem1 = fuzz.trapmf(x, [0.45, 2, 3, 4.25])
mem2 = fuzz.trapmf(x, [1, 2.25, 3.25, 4.5])
mem3 = fuzz.trapmf(x, [3, 4, 10, 11])

plt.figure(figsize=(10,5))
#plt.plot((0, 0.9), (0.2, 0.2), 'k--')
#plt.plot((0, 0.9), (0.12, 0.12), 'k--')
ax = plt.subplot(111)

ax.plot(x, mem1, 'b', linewidth=1.5, label='Fit')
#ax.plot(x, mem2, 'g', linewidth=1.5, label='Sociable')
#ax.plot(x, mem3, 'r', linewidth=1.5, label='Over-social')
#ax.axvline(0.9, color='k', linestyle='-')
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