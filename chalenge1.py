import matplotlib.pyplot as plt
import numpy as np
# ----------------------------
# 1. Line plot data (sales over months)
# ----------------------------
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
# sales = [120, 135, 150, 170, 160, 180, 210, 190]

# plt.plot(months,sales)
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.title('Sales over months')
# plt.grid(axis='y',linestyle = '--',color = 'g')
# plt.show()

# 2. Bar chart data (students in classes)
# ----------------------------
classes = ["Math", "Science", "History", "English", "Art"]
students = [40, 35, 30, 50, 25]
plt.bar(classes,students,color='red')
plt.title('Students in class')
plt.xlabel('classes')
plt.ylabel('student')
plt.tight_layout()
plt.show()

# classes = ["Math", "Science", "History", "English", "Art"]
# students = [40, 35, 30, 50, 25]


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x = np.arange(len(classes))
# y = np.zeros(len(classes))  # y-axis set to 0 for all bars
# z = np.zeros(len(classes))  # bars start from height 0


# dx = np.ones(len(classes))  # width
# dy = np.ones(len(classes))  # depth
# dz = students               # height


# ax.bar3d(x, y, z, dx, dy, dz, color='mediumseagreen')
# ax.set_xticks(x)
# ax.set_xticklabels(classes)
# ax.set_xlabel('Subjects')
# ax.set_ylabel('Y')
# ax.set_zlabel('Number of Students')
# ax.set_title('3D Bar Chart: Students in Classes')

# plt.show()