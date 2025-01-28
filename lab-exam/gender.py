def pretty_print(data_cube, x_axis, y_axis, z_axis, field_width = 5):
    for i in range(x_axis):
        print(f"----------- Layer-X[{i}] -------------")        
        for j in range(y_axis):
            row_data = "  ".join(f"{data_cube[i][j][k]:>{field_width}}" for k in range(z_axis))
            print(f"Y[{j}]: {row_data}")
        print()

def sliced_view(sliced_array, caption, rowdata_alignment = "left", field_width = 6):
    X = len(sliced_array)    
    Y = len(sliced_array[0])

    print(caption)
    print("-" * (field_width * Y + X))

    if rowdata_alignment.lower() == "right":
        for i in range(X):
            row_data = "  ".join(f"{item:>{field_width}}" for item in sliced_array[i])
            print(row_data)
    else:
        for i in range(X):
            row_data = "  ".join(f"{item:<{field_width}}" for item in sliced_array[i])
            print(row_data)
    print("-" * (field_width * Y + X))


def slice_by_gender(data_cube, gender):
    gender = gender.lower()
    sex = {
        "male": 0,
        "female": 1
    }

    sliced = []
    for x in range(len(data_cube)):
        row = []
        for y in range(len(data_cube[x])):
            row.append(data_cube[x][y][sex[gender]])
        sliced.append(row)
    return sliced


X , Y, Z = 7, 4, 2

data_cube = [
    [[2017, 2017], [2018, 2018], [2019, 2019], [2020, 2020]],
    [[150, 145],   [140, 138],   [130, 132],   [145, 140]],
    [[170, 155],   [160, 146],   [145, 142],   [130, 148]],
    [[130, 120],   [120, 115],   [125, 130],   [135, 125]],
    [[160, 150],   [130, 140],   [145, 140],   [140, 145]],
    [[110, 90],    [100, 85],    [95, 75],     [105, 80]],
    [[125, 120],   [110, 105],   [110, 120],   [115, 90]]]


pretty_print(data_cube, X, Y, Z)
parameter = input("Enter gender to slice:  ").lower()

match parameter:
    case "male": 
        male = slice_by_gender(data_cube, "male")
        sliced_view(male, "Male Slice, i.e., (Z = 0):", "right")

    case "female": 
        female = slice_by_gender(data_cube, "female")
        sliced_view(female, "Female Slice, i.e., (Z = 1):", "right")

    case _: print("Invalid Choice!")


