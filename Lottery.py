print("Welcome to our lottery station.")
red_ball = []
blue_ball = []
count_red = 1
count_blue = 1
while count_red <= 6:
    num = eval(input("[%d]select red ball:" % count_red))
    if num in red_ball:
        print("number %d is already exist in red ball list." % num)
    else:
        if 1 <= num <= 32:
            red_ball.append(num)
            count_red += 1
        else:
            print("only can select number between 1-32.")
while count_blue <= 2:
    num = eval(input("[%d]select blue ball:" % count_blue))
    if num in blue_ball:
        print("number %d is already exist in blue ball list." % num)
    else:
        if 1 <= num <= 16:
            blue_ball.append(num)
            count_blue += 1
        else:
            print("only can select number between 1-16.")
print("Red ball:", red_ball)
print("Blue ball:", blue_ball)
print("Good luck.")
