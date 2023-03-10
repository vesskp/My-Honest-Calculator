# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

with open("c:/temp/run_log.txt", "w"):
    pass


def log_msg(msg):
    with open("c:/temp/run_log.txt", "a") as lf:
        lf.write(f"{msg}\n")


def is_one_digit(v):
    if (-10 < v < 10) and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 in ["*", "+", "-"]):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


memory = 0
while True:
    result = ""
    while True:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        try:
            float(x)
            float(y)
        except Exception as exception:
            print(msg_1)
            continue
        x = float(x)
        y = float(y)
        if oper not in ["+", "-", "*", "/"]:
            print(msg_2)
            continue
        check(x, y, oper)
        if oper == "/" and y == 0:
            print(msg_3)
            continue
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif oper == "/" and y != 0:
            result = x / y
        print(result)
        break

    while True:
        print(msg_4)
        answer = input()
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(globals()[f"msg_{msg_index}"])
                    answer = input()
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            memory = result
                            break
                    elif answer == "n":
                        break
                    else:
                        continue
            else:
                memory = result
            break
        elif answer == "n":
            break
        else:
            continue

    again = True
    while True:
        print(msg_5)
        answer = input()
        if answer == "y":
            break
        elif answer == "n":
            again = False
            break
        else:
            continue

    if not again:
        break
