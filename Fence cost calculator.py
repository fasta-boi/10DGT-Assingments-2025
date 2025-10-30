# lachlan gaeth
#31/10/25
# v1

code_1 = "running"
code_2 = "running"
code_3 = "running"
keep_going = ""
width_error = "Please try a width that is greater than zero. "
length_error = "Please try a length that is greater than zero. "
cost_error = "Please try a cost that is greater than zero. "
while keep_going == "":

    while code_1 == "running":
        try:
            fence_width = float(input("What is the width of your fence (width above zero)? \n"))
            if fence_width > 0:
                print(f"Your fence width is {fence_width}\n")
                code_1 = "stopped"
            else:
                print(width_error)
        except ValueError:
            print (f"{width_error}\n")
    while code_2 == "running":
        try:
            fence_length = float(input("What is the length of your fence (length above zero)? "))
            if fence_length > 0:
                print(f"Your fence length is {fence_length}\n")
                code_2 = "stopped"
            else:
                print(length_error)
        except ValueError:
            print(f"{length_error}\n")
    while code_3 == "running":
        try:
            fence_cost = float(input("What is the cost of your fence (cost above zero)? "))
            if fence_cost > 0:
                print(f"Your fence cost is {fence_cost}\n")
                code_3 = "stopped"
            else:
                print(cost_error)
        except ValueError:
            print(f"{cost_error}\n")

    Perimeter = fence_length * 2 + fence_width * 2
    print(f"The perimeter of your fence is {Perimeter} meters \n")

    cost = Perimeter * fence_cost
    print(f"the cost of your fence is ${cost} \n")

    keep_going = input("Press <Enter> to do another calculation, or any other key to quit. Thanks!")
    if keep_going == "":
        code_1 = "running"
        code_2 = "running"
        code_3 = "running"