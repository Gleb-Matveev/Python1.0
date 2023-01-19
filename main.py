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
 
 
def print_hi(name):
    print(f'Hi, {name}')
 
 
if __name__ == '__main__':
    print_hi('PyCharm')
