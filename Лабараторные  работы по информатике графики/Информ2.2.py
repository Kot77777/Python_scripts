import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1000, 10001, 91)
y = (10**(-9))*np.array([0, 0, 0, 0, 991400, 0, 0, 0, 0, 1000200, 0, 0, 0, 999900, 0, 0, 999600, 0, 0, 1010200, 0, 998900, 0, 991300, 0, 999400, 0, 1000200, 0, 1008300, 0, 1001400, 0, 998600, 1000000, 0, 1000200, 0, 0, 1000100, 990500, 0, 1007900, 1003300, 994900, 0, 1002300, 1000500, 999500, 991900, 0, 1012900, 995500, 991100, 1008300, 991100, 1000200, 999900, 1009700, 991600, 1008400, 999400, 999300, 992500, 1009900, 997400, 1000000, 1000800, 999000, 2018800, 999700, 999900, 991900, 1011000, 1000300, 988300, 2011800, 999800, 999600, 999900, 999800, 2000300, 524400, 1065400, 1002700, 996800, 1999500, 1005800, 1005000, 1993000, 1000900])
xc = np.linspace(1000, 10001, 91)
yc = (10**(-9))*np.array([0, 0, 520100, 0, 0, 516500, 0, 0, 0, 0, 1062000, 0, 598000, 0, 589800, 0, 0, 1090200, 0, 594500, 583300, 0, 0, 1091500, 0, 999000, 0, 1013500, 0, 996000, 0, 1001900, 0, 992400, 0, 1000600, 0, 997700, 1009800, 0, 990900, 997000, 0, 0, 991300, 1003800, 0, 996900, 1001800, 1003500, 1005800, 997500, 997000, 0, 990300, 1000300, 1000400, 1002800, 997600, 1021500, 1001500, 0, 0, 0, 1992500, 1008000, 999600, 1001100, 1103000, 987900, 1002500, 993500, 998300, 1001700, 999700, 1000400, 1023200, 987300, 1985900, 1002600, 1000000, 1588200, 1088500, 1012800, 990300, 1003200, 1003700, 995800, 999700, 2009500, 1000400])
xr = np.linspace(1000, 10001, 91)
yr = (10**(-9))*np.array([0, 0, 0, 0, 1011600, 0, 0, 988300, 0, 0, 0, 0, 1091000, 0, 0, 906900, 0, 1023300, 0, 0, 977200, 0, 0, 0, 0, 1004500, 0, 997700, 0, 1016300, 0, 1091500, 0, 1000200, 1002200, 0, 998000, 997600, 0, 1005600, 997500, 0, 1002700, 0, 1005000, 1016200, 977300, 1002500, 0, 1000000, 1000600, 595900, 1089900, 1005100, 995900, 998200, 1002900, 1001100, 1001900, 998000, 1002600, 997500, 1001000, 993200, 1000800, 1004800, 995600, 1001600, 998600, 1002900, 999000, 1000400, 1000400, 1005100, 994000, 1998400, 1022300, 979200, 998600, 1001300, 2004000, 1000800, 995400, 998600, 1001700, 1999800, 1001900, 1009100, 1990200, 1018100, 981500])

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

for i in range(91):
    if y[i] != 0:
        x1.append(x[i])
        y1.append(y[i])
for i in range(91):
    if yc[i] != 0:
        x2.append(xc[i])
        y2.append(yc[i])
for i in range(91):
    if yr[i] != 0:
        x3.append(xr[i])
        y3.append(yr[i])

x1 = np.array(x1)
y1 = np.array(y1)
y_1 = (1/(x1*np.log(x1)))*y1
x2 = np.array(x2)
y2 = np.array(y2)
y_2 = (1/(x2*np.log(x2)))*y2
x3 = np.array(x3)
y3 = np.array(y3)
y_3 = (1/(x3*np.log(x3)))*y3

fig, ax = plt.subplots(nrows= 3 , ncols= 2)

ax[0, 0].plot(x1, y1, label = "график сортировки кучей")
ax[0, 1].plot(x1, y_1, label = "график сортировки кучей")
ax[0, 1].set_ylabel("t/Nlog(N), t - время в нс.", fontsize=8)
ax[0, 1].set_xlabel("N, N - количество элементов в массиве", fontsize=8)
ax[0, 0].set_ylabel("t, t - время в нс.", fontsize=8)
ax[0, 0].set_xlabel("N, N - количество элементов в массиве", fontsize=8)

ax[1, 0].plot(x2, y2, label = "график сортировки слиянием", c = "r")
ax[1, 1].plot(x2, y_2, label = "график сортировки слиянием", c = "r")
ax[1, 1].set_ylabel("t/Nlog(N), t - время в нс.", fontsize=8)
ax[1, 1].set_xlabel("N, N - количество элементов в массиве", fontsize=8)
ax[1, 0].set_ylabel("t, t - время в нс.", fontsize=8)
ax[1, 0].set_xlabel("N, N - количество элементов в массиве", fontsize=8)

ax[2, 0].plot(x3, y3, label = "график сортировки расческой", c = "g")
ax[2, 1].plot(x3, y_3, label = "график сортировки расческой", c = "g")
ax[2, 1].set_ylabel("t/Nlog(N), t - время в нс.", fontsize=8)
ax[2, 1].set_xlabel("N, N - количество элементов в массиве", fontsize=8)
ax[2, 0].set_ylabel("t, t - время в нс.", fontsize=8)
ax[2, 0].set_xlabel("N, N - количество элементов в массиве", fontsize=8)

ax[0,0].legend()
ax[0,1].legend()
ax[1,0].legend()
ax[1,1].legend()
ax[2,0].legend()
ax[2,1].legend()
plt.show()