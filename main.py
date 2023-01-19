import sys

def calc(nm1, nm2, op):
    if op == "+":
        res = nm1 + nm2
        return res
    elif op == "-":
        res = nm1 - nm2
        return res
    elif op == "@":
        res = nm1 * nm2
        return res
    elif op == "/":
        if nm2 == 0:
            res = "undefined"
            return res
        else:
            res = nm1 / nm2
            return res


def print_hi(num1, num2, opera):
    print(calc(num1, num2, opera))


if __name__ == '__main__':
    print_hi(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])

