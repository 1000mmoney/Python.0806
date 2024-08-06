import matplotlib.pyplot as plt

x = [17, 18, 19, 20, 21, 22, 23]
y = [65, 70, 70, 75, 80, 85, 85]

plt.plot(x, y, marker='o', linestyle='-', color='red', label='temperature')

plt.title('Daily temperature trend')

plt.xlabel('Time (hour)')
plt.ylabel('Temperature (C)')

plt.legend()

plt.grid(True)
plt.show()

plt.savefig("./results/linechart.png")