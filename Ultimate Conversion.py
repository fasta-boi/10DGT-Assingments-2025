# lachlan gaeth
# 7/11/25
# v1

dc_selected = "You have selected distance conversion \n"
mass_selected = "You have selected mass conversion \n"
time_selected = "You have selected time conversion \n"
keep_going = ""

while keep_going == "":
    code_open = input("Welcome to ultimate conversion, what tpye of conversion would you like to do? \n"
    "type number corrolating to desired conversion: \n"
    "1 = Distance conversion \n"
    "2 = Mass conversion \n"
    "3 = time conversion \n"
    "Enter your chosen conversion type below. \n")
    
    if code_open == "1":
        print(dc_selected)
        keep_going = "code stop"

    elif code_open == "2":
        print(mass_selected)
        keep_going = "code stop"

    elif code_open == "3":
        print(time_selected)
        keep_going = "code stop"

    if code_open == "1":
        input("please insert your distance below to be converted \n")

keep_going = input("Press <Enter> to do another calculation, or any other key to quit. Thanks! \n")