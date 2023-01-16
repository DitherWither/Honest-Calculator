msg = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
]


def main():
    memory = 0
    while True:
        calc = input(msg[0])
        equation = calc.split()

        x = equation[0]
        y = equation[2]

        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        operator = equation[1]

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg[1])
            continue

        if operator not in ['+', '-', '*', '/']:
            print(msg[2])
            continue

        check(x, y, operator)

        if operator == '+':
            result = x + y
        elif operator == '-':
            result = x - y
        elif operator == '*':
            result = x * y
        elif operator == '/':
            if y == 0:
                print(msg[3])
                continue
            result = x / y

        print(result)
        save_result = input(msg[4])
        no_save = False
        if save_result == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    answer = input(msg[msg_index])
                    if answer == 'y':
                        if msg_index >= 12:
                            break
                        msg_index += 1
                    if answer == 'n':
                        no_save = True
                        break

            if not no_save:
                memory = result

        rerun = 'd'
        while True:
            rerun = input(msg[5])
            if rerun == 'n':
                break
            elif rerun == 'y':
                break

        if rerun == 'n':
            break
        elif rerun == 'y':
            continue


def check(x: float, y: float, operator: str):
    lazy_msg = ''
    if is_one_digit(x) and is_one_digit(y):
        lazy_msg += msg[6]

    if (x == 1 or y == 1) and operator == '*':
        lazy_msg += msg[7]

    if (x == 0 or y == 0) and operator in ['*', '+', '-']:
        lazy_msg += msg[8]

    if lazy_msg != '':
        print(msg[9] + lazy_msg)


def is_one_digit(n) -> bool:
    return 10 > n > -10 and n.is_integer()


if __name__ == "__main__":
    main()
