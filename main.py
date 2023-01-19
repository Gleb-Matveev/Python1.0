
def calc(nm1, nm2, op):
    if op == "+":
        res = nm1 + nm2
        return res
    elif op == "-":
        res = nm1 - nm2
        return res
    elif op == "*":
        res = nm1 * nm2
        return res
    elif op == "/":
        if nm2 == 0:
            res = "undefined"
            return res
        else:
            res = nm1 / nm2
            return res


def main():
    opera = input("Enter an operation: ")
    num1 = int(input("Enter a first num: "))
    num2 = int(input("Enter a second num: "))
    print(calc(num1, num2, opera))


if __name__ == '__main__':
    main()
