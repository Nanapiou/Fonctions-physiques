import csv
import matplotlib.pyplot as plt

x = list()
y = list()
with open("./tps/tp7/csv_2/TEK0000.CSV") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0]:
            print(f"{row[0]}: {row[1]}")
        x.append(float(row[3]))
        y.append(float(row[4]))

plt.plot(x, y, "-")
plt.show()


# for i, fm in enumerate(("r-", "g-", "b-", "y-", "m-", "c-", "k-")):
#     x = list()
#     y = list()
#     with open(f"./csv_tim/TEK000{i}.CSV") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             x.append(float(row[3]))
#             y.append(float(row[4]))
#     plt.plot(x, y, fm)
# plt.show()
