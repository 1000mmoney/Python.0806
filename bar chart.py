import matplotlib.pyplot as plt

categories = [ 'Apple', 'Banana', 'Orange', 'Strawberry', 'Grape']
values = [25, 30, 15, 20, 35]

plt.clf()

plt.bar(categories, values, color='skyblue')

plt.title('Fruit Sales')

plt.xlabel('Fruit')
plt.ylable('Sales')

plt.show()

plt.savefig("./results/bar_chart.png")