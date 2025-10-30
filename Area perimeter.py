# 29/10/25
# Week 1

# Area,Perimeter calculator
code_ = "running"
code_2 = "running"
keep_going = ""
while keep_going == "":
    error = "Please try a number that is gretaer than zero. "
    while code_ == "running":
        try:
            shape_width = float(input("What is the width of your shape(Number above zero)? "))
            if shape_width > 0:
                print(f"Your shapes width is {shape_width}\n")
                code_ = "stopped"
            else:
                print(error)
        except ValueError:
            print (f"{error}\n")
    while code_2 == "running":
        try:
            shape_height = float(input("What is the height of your shape(Number above zero)? "))
            if shape_height > 0:
                print(f"Your shapes height {shape_height}\n")
                code_2 = "stopped"
            else:
                print(error)
        except ValueError:
            print(f"{error}\n")


    area = shape_width * shape_height
    print(f"The area of your shape is {area} square units \n")

    Perimeter = shape_width * 2 +  shape_height * 2
    print(f"The perimeter of your shape is {Perimeter} untis \n")

    keep_going = input("Press <Enter> to continue, or any other key to quit. Thanks!\n")
    if keep_going == "":
        code_ = "running"
        code_2 = "running"