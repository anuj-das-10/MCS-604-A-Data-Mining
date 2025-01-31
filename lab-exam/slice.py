def pretty_print(data_cube, x_axis, y_axis, z_axis, field_width = 5):
    for i in range(x_axis):
        print(f"----------- Layer-X[{i}] -------------")        
        for j in range(y_axis):
            row_data = "  ".join(f"{data_cube[i][j][k]:>{field_width}}" for k in range(z_axis))
            print(f"Y[{j}]: {row_data}")
        print()  


def slice_cube(datacube, axis, slice_index, x, y, z):
    axes = { 1: "X-axis", 2: "Y-axis", 3: "Z-axis"}

    if  (axis == 1 and 0 <= slice_index < x) or \
        (axis == 2 and 0 <= slice_index < y) or \
        (axis == 3 and 0 <= slice_index < z):

        print(f"\nSlice along {axes[axis]}:")

        if axis == 1:  
            for j in range(y):
                print("\t".join(str(datacube[slice_index][j][k]) for k in range(z)))
        elif axis == 2:  
            for i in range(x):
                print("\t".join(str(datacube[i][slice_index][k]) for k in range(z)))
        elif axis == 3:  
            for i in range(x):
                print("\t".join(str(datacube[i][j][slice_index]) for j in range(y)))
    else:
        print("Invalid slice index for the chosen axis.")


def slice_menu(datacube, x, y, z):
    print("Choose the Slicing Operation: ")
    print("1. Along X-axis")
    print("2. Along Y-axis")
    print("3. Along Z-axis")
    axis = int(input("Enter your choice:  "))

    match axis:
        case 1:
            print("You have selected Slicing along X-axis!")
            slice_index = int(input(f"Select a slice index (0 to {x}): "))
            slice_cube(datacube, axis, slice_index, x, y, z)
        case 2:
            print("You have selected Slicing along Y-axis!")
            slice_index = int(input(f"Select a slice index (0 to {y}): "))
            slice_cube(datacube, axis, slice_index, x, y, z)
        case 3:
            print("You have selected Slicing along Z-axis!")
            slice_index = int(input(f"Select a slice index (0 to {z}): "))
            slice_cube(datacube, axis, slice_index, x, y, z)
        case _:
            print("Invalid axis choice. Please select 1, 2, or 3.")


data_cube = [
    [[ 1,  2,  3], [ 4,  5,  6], [ 7,  8,  9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]

x, y, z = len(data_cube), len(data_cube[0]), len(data_cube[0][0])
pretty_print(data_cube, x, y, z)
slice_menu(data_cube, x, y, z)

