import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#################
##Define variable:
a1 = float(3.16)
a2 = float(3.16)
gamma1 = float(60)
# b1 = float(3.32)
# b2 = float(3.32)
# gamma2 = float(60)
# phi = float(10)
b1 = float(12.4)
b2 = float(19.7)
gamma2 = float(88.8)
phi = float(12.7)

##########
##Define lattice points:
A1 = np.array([a1, 0])
A2 = np.array([a2 * np.cos(np.deg2rad(gamma1)), a2 * np.sin(np.deg2rad(gamma1))])
B1 = np.array([b1 * np.cos(np.deg2rad(phi)), -b1 * np.sin(np.deg2rad(phi))])
B2 = np.array([b2 * np.cos(np.deg2rad(gamma2 - phi)), b2 * np.sin(np.deg2rad(gamma2 - phi))])

matrix = []
matrix_second = []
matrix_third = []
# Define lattice translations:
for n1 in range(51):
    first_matrix_row = []
    second_matrix_row = []
    third_matrix_row = []
    # fourth_matrix_row = []
    for n2 in range(51):
        T = n1 * B1 + n2 * B2 #+ 0.5*(B1+B2)
        P1 = (np.dot(T, A1)) / (np.linalg.norm(A1))
        P1 = P1 - np.floor(P1)
        P2 = np.dot(T, A2) / (np.linalg.norm(A2))
        P2 = P2 - np.floor(P2)
        first_matrix_row.append(P1)
        second_matrix_row.append(P2)
        third_matrix_row.append(T)
    matrix.append(first_matrix_row)
    matrix_second.append(second_matrix_row)
    matrix_third.append(third_matrix_row)
# print(matrix_third)
p1 = []
p2 = []
x_coordinate = []
y_coordinate = []
# print(matrix)
for i in matrix:
    for j in i:
        p1.append(j)
# print(matrix_second)
for i in matrix_second:
    for j in i:
        p2.append(j)
for i in matrix_third:
    for j in i:
        x_coordinate.append(j[0])
        y_coordinate.append(j[1])

csv_file = open("moire_data0.5.csv", "w")
header = "x,y,p1,p2"+"\n"
csv_file.writelines(header)
for i in range(0,len(x_coordinate)):
    line_to_write = str(x_coordinate[i])+","+str(y_coordinate[i])+","+str(p1[i])+","+str(p2[i])+"\n"
    csv_file.write(line_to_write)
csv_file.close()
# print(matrix_third)
# print(matrix_second)
# print(matrix)

plt.rcParams['figure.dpi'] = 300
plt.xlim(0, 3000)
plt.ylim(0, 3000)
sns.color_palette("hls")
ax = sns.heatmap(matrix, cmap="hsv", square=True)
ax.invert_yaxis()
plt.savefig('T_A1.png')
plt.show()
ax = sns.heatmap(matrix_second, cmap="hsv", square=True)
ax.invert_yaxis()
plt.savefig('T_A2.png')
plt.show()

# sns scatterplot

df = pd.read_csv('moire_data0.5.csv')
sns.scatterplot(data = df, x = "x", y = "y", hue = "p1",  palette = "hls")
plt.show()

###combined this data to the body center in excel to get the complete picture