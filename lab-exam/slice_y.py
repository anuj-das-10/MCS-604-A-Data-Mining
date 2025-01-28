def pretty_print(data_cube, x_axis, y_axis, z_axis, field_width = 5):
    for i in range(x_axis):
        print(f"----------- Layer-X[{i}] -------------")        
        for j in range(y_axis):
            row_data = "  ".join(f"{data_cube[i][j][k]:>{field_width}}" for k in range(z_axis))
            print(f"Y[{j}]: {row_data}")
        print() 

def slice_y(datacube, x, y, z):
    print("Slice along Y-axis!")
    slice_index = int(input(f"Select a slice index (0 to {y}): "))
    
    if(0 <= slice_index < y):
        for i in range(x):
                print("\t".join(str(datacube[i][slice_index][k]) for k in range(z)))
    else:
        print("Invalid slice index for the chosen axis.")

data_cube = [
    [[ 1,  2,  3], [ 4,  5,  6], [ 7,  8,  9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]

x, y, z = len(data_cube), len(data_cube[0]), len(data_cube[0][0])
pretty_print(data_cube, x, y, z)
slice_y(data_cube, x, y, z)