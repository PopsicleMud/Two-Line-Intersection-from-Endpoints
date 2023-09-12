# Import modules
import matplotlib.pyplot as plt


# Set coordinates of both lines' endpoints
xa = 2
ya = 3
xb = 8
yb = 6
xc = 1
yc = 4
xd = 10
yd = 5

# Uncomment the lines below to get user input instead of assigning the variables above.
# xa = float(input("xa? "))
# ya = float(input("ya? "))
# xb = float(input("xb? "))
# yb = float(input("yb? "))
# xc = float(input("xc? "))
# yc = float(input("yc? "))
# xd = float(input("xd? "))
# yd = float(input("yd? "))

# Prevent division by zero
if xb-xa == 0.0:
  xb += 0.000001
if xc == xd:
  xd += 0.000001


# Calculate slopes of both lines
m1 = round((yb-ya)/(xb-xa),5)
m2 = round((yd-yc)/(xd-xc),5)
print(f"Slope of line AB: {m1}")
print(f"Slope of line CD: {m2}")

# Calculate x for intersection
x = (m1*xa-ya-m2*xc+yc)/(m1-m2)

# Calculate y for intersection
y = m1*(x-xa)+ya

# Limit decimal places
x = round(x,5)
y = round(y,5)


print(f"intersection: x={x}, y={y}")
intersection_label = "intersection"
fig = plt.figure()
fig.set_size_inches(4,3)
fig.set_dpi(300)
plt.plot([xa,xb],[ya,yb], label = "line AB")
plt.plot([xc,xd],[yc,yd], label = "line CD")
plt.plot(x,y, 'o', label = intersection_label,)
plt.legend()
fig.show()
fig.savefig("IntersectionPlot.png")


