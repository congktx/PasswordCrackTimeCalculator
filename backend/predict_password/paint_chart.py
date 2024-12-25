import csv
import matplotlib.pyplot as plt
from base import max_characters, calculate_entropy

x_l = []
y_l = []
x_nl = [[] for _ in range(max_characters + 1)]
y_nl = [[] for _ in range(max_characters + 1)]

def getxy():
    with open("./data/data.csv", "r") as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if (index == 0):
                continue
            leng = int(row[1])
            x_l.append(leng)
            y_l.append(float(row[7]))
            # x_nl[leng].append(len(set(row[0])))
            x_nl[leng].append(calculate_entropy(row[0]))
            y_nl[leng].append(float(row[7]))

def paint_chart_l():
    plt.scatter(x_l, y_l, color='b')
    plt.title("Biểu đồ từ tập hợp các điểm (x, y)")
    plt.xlabel("X")
    plt.ylabel("crack_time")
    plt.show()

def paint_chart_nl(leng):
    plt.scatter(x_nl[leng], y_nl[leng], color='b')
    plt.title("Biểu đồ từ tập hợp các điểm (x, y)")
    plt.xlabel("X")
    plt.ylabel("crack_time")
    plt.show()

if __name__ == "__main__":
    getxy()
    # paint_chart_l()
    paint_chart_nl(10)