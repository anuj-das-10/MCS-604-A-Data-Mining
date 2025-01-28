def pretty_print(data_cube, x_axis, y_axis, z_axis, field_width = 5):
    for i in range(x_axis):
        print(f"----------- Layer-X[{i}] -------------")        
        for j in range(y_axis):
            row_data = "  ".join(f"{data_cube[i][j][k]:>{field_width}}" for k in range(z_axis))
            print(f"Y[{j}]: {row_data}")
        print()  

def dice_z(datacube, x, y, z, field_width=5):
    print("Dicing along Z-axis!")
    start_index = int(input(f"Select the starting index for the slice (0 to {z-1}): "))
    end_index = int(input(f"Select the ending index for the slice (starting from {start_index} to {z-1}): "))

    if(0 <= start_index < end_index <= z):
        print(f"\nSubcube along Z-axis (from index {start_index} to {end_index}):")
        for i in range(x):
            for j in range(y):
                row_data = "  ".join(f"{datacube[i][j][k]:>{field_width}}" for k in range(start_index, end_index + 1))
                print(f"X[{i}] Y[{j}] : {row_data}")
            print()
    else:
        print("Invalid range for the dicing operation.")

data_cube = [
    [[ 1,  2,  3], [ 4,  5,  6], [ 7,  8,  9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]

x, y, z = len(data_cube), len(data_cube[0]), len(data_cube[0][0])
pretty_print(data_cube, x, y, z)
dice_z(data_cube, x, y, z)