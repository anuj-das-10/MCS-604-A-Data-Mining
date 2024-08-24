import pprint as _

def ThreeD(x, y, z):
	lst = [[ ["#" for col in range(x)] for col in range(y)] for row in range(z)]
	return lst
	

x_axis = 3
y_axis = 3
z_axis = 3
# used the pretty printed function
_.pprint(ThreeD(x_axis, y_axis, z_axis))



