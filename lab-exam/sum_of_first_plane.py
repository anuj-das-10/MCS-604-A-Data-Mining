def pretty_print(data_cube, x_axis, y_axis, z_axis, field_width = 5):
    for i in range(x_axis):
        print(f"----------- Layer-X[{i}] -------------")        
        for j in range(y_axis):
            row_data = "  ".join(f"{data_cube[i][j][k]:>{field_width}}" for k in range(z_axis))
            print(f"Y[{j}]: {row_data}")
        print()  


x = int(input("Enter the dimension x: "))
y = int(input("Enter the dimension y: "))
z = int(input("Enter the dimension z: "))

datacube = [[[0 for _ in range(z)] for _ in range(y)] for _ in range(x)]

print("Enter the data:")
for i in range(x):
    for j in range(y):
        for k in range(z):
            datacube[i][j][k] = int(input(f"Enter value for a[{i}][{j}][{k}]: "))

print("\nThe entered cube is:")
pretty_print(datacube, x, y, z)

sum_first_plane = 0
print("Data in the first plane:")
for j in range(y):
    for k in range(z):
        print(datacube[0][j][k], end="\t")
        sum_first_plane += datacube[0][j][k]
    print()
print(f"\nThe sum in the first plane is: {sum_first_plane}")
