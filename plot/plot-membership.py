import skfuzzy as fuzz
import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(0, 100, 0.01)

other_m1 = fuzz.trapmf(x, [-1, 0, 1.5, 2.5])
other_m2 = fuzz.trapmf(x, [2, 3, 10, 11])

work_m1 = fuzz.trapmf(x, [-1, 0, 4, 6])
work_m2 = fuzz.trapmf(x, [5, 7, 8, 10])
work_m3 = fuzz.trapmf(x, [9, 11, 24, 25])

health_m1 = fuzz.trapmf(x, [-1, 0, 0.5, 1])
health_m2 = fuzz.trapmf(x, [0.45, 2, 3, 4.25])
health_m3 = fuzz.trapmf(x, [2.75, 4, 10, 11])

leisure_m1 = fuzz.trapmf(x, [-1, 0, 7, 9])
leisure_m2 = fuzz.trapmf(x, [8, 10, 12, 14])
leisure_m3 = fuzz.trapmf(x, [13, 16, 24, 25])

social_m1 = fuzz.trapmf(x, [-1, 0, 1.5, 2])
social_m2 = fuzz.trapmf(x, [1, 2.25, 3.25, 4.5])
social_m3 = fuzz.trapmf(x, [3, 4, 10, 11])

ideal_score_health = fuzz.trapmf(x, [11.25, 29.75, 42, 50])

health_score_m1 = fuzz.trapmf(x, [-1, 0, 15, 20])
health_score_m2 = fuzz.trapmf(x, [11.25, 29.75, 42, 50])
health_score_m3 = fuzz.trapmf(x, [45, 60, 100, 101])

plt.figure(figsize=(6,3))
plt.plot((0, 17), (0.6, 0.6), 'k--')
plt.plot((0, 17), (0.310, 0.310), 'k--')
ax = plt.subplot(111)

ax.plot(x, health_score_m1, 'b', linewidth=1.5, label='Low Score')
ax.plot(x, health_score_m2, 'g', linewidth=1.5, label='Ideal Score')
ax.plot(x, health_score_m3, 'r', linewidth=1.5, label='High Score')
ax.axvline(17, color='k', linestyle='-')
plt.xticks(np.arange(min(x), max(x)+1, 10))
ax.legend()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlabel('Score')
ax.set_ylabel('Membership')
ax.xaxis.set_label_position('top')

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.show()