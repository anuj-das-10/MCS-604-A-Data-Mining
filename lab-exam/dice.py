def pretty_print(data_cube, x_axis, y_axis, z_axis, field_width = 5):
    for i in range(x_axis):
        print(f"----------- Layer-X[{i}] -------------")        
        for j in range(y_axis):
            row_data = "  ".join(f"{data_cube[i][j][k]:>{field_width}}" for k in range(z_axis))
            print(f"Y[{j}]: {row_data}")
        print()  

def dice_cube(datacube, axis, start_index, end_index, x, y, z, field_width=5):
    axes = { 1: "X-axis", 2: "Y-axis", 3: "Z-axis" }

    if (axis == 1 and 0 <= start_index < end_index <= x) or \
       (axis == 2 and 0 <= start_index < end_index <= y) or \
       (axis == 3 and 0 <= start_index < end_index <= z):
    
        print(f"\nSubcube along {axes[axis]} (from index {start_index} to {end_index}):")
        
        if axis == 1:  
            for j in range(y):
                for k in range(z):
                    row_data = "  ".join(f"{datacube[i][j][k]:>{field_width}}" for i in range(start_index, end_index + 1))
                    print(f"Y[{j}] Z[{k}] : {row_data}")
                print()

        elif axis == 2:  
            for i in range(x):
                for k in range(z):
                    row_data = "  ".join(f"{datacube[i][j][k]:>{field_width}}" for j in range(start_index, end_index + 1))
                    print(f"X[{i}] Z[{k}] : {row_data}")
                print()

        elif axis == 3:  
            for i in range(x):
                for j in range(y):
                    row_data = "  ".join(f"{datacube[i][j][k]:>{field_width}}" for k in range(start_index, end_index + 1))
                    print(f"X[{i}] Y[{j}] : {row_data}")
                print()
                
        else:
            print("Invalid range for the dicing operation.")
    else:
        print("Invalid range for the dicing operation.")


def dice_menu(datacube, x, y, z):
    print("Choose the Dicing Operation: ")
    print("1. Along X-axis")
    print("2. Along Y-axis")
    print("3. Along Z-axis")
    axis = int(input("Enter your choice:  "))

    match axis:
        case 1:
            print("You have selected Dicing along X-axis!")
            start_index = int(input(f"Select the starting index for the slice (0 to {x-1}): "))
            end_index = int(input(f"Select the ending index for the slice (starting from {start_index} to {x-1}): "))
            if 0 <= start_index < end_index < x:
                dice_cube(datacube, axis, start_index, end_index, x, y, z)
            else:
                print("Invalid indices. Please ensure 0 <= start_index < end_index < x.")

        case 2:
            print("You have selected Dicing along Y-axis!")
            start_index = int(input(f"Select the starting index for the slice (0 to {y-1}): "))
            end_index = int(input(f"Select the ending index for the slice (starting from {start_index} to {y-1}): "))
            if 0 <= start_index < end_index < y:
                dice_cube(datacube, axis, start_index, end_index, x, y, z)
            else:
                print("Invalid indices. Please ensure 0 <= start_index < end_index < y.")

        case 3:
            print("You have selected Dicing along Z-axis!")
            start_index = int(input(f"Select the starting index for the slice (0 to {z-1}): "))
            end_index = int(input(f"Select the ending index for the slice (starting from {start_index} to {z-1}): "))
            if 0 <= start_index < end_index < z:
                dice_cube(datacube, axis, start_index, end_index, x, y, z)
            else:
                print("Invalid indices. Please ensure 0 <= start_index < end_index < z.")

        case _:
            print("Invalid axis choice. Please select 1, 2, or 3.")


data_cube = [
    [[ 1,  2,  3], [ 4,  5,  6], [ 7,  8,  9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]

x, y, z = len(data_cube), len(data_cube[0]), len(data_cube[0][0])
pretty_print(data_cube, x, y, z)
dice_menu(data_cube, x, y, z)
