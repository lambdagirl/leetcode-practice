# expr := int | ( op expr+ )
def eval(expr):
    # TODO: dead with empty expr
    tokens = tokenize(expr)
    if len(tokens) == 1:
        return evalInt(tokens[0])
    op = tokens[1]
    xs = []  # store list of expressions (string)
    i, j = 2, 2
    counter = 0
    while j < len(tokens) - 1:
        if tokens[j] == '(':
            counter += 1
        if tokens[j] == ')':
            counter -= 1

        if counter == 0:
            x = " ".join(tokens[i:j + 1])
            xs.append(x)
            i = j + 1
            j = i
            counter = 0
        else:
            j += 1
    print("DEBUG: xs =", xs)
    if op == "*":
        res = 1
    if op == "+":
        res = 0

    for x in xs:
        if op == '+':
            res += eval(x)
        else:
            res *= eval(x)
    return res


def evalInt(numStr):
    return int(numStr)


def tokenize(expr):
    return expr.split(' ')


if __name__ == "__main__":
    print(eval("3"))  # => 3
    print(eval("( + 1 2 )"))  # => [ '(', '+', '1', '2', ')' ]
    print(eval("( + 3 4 5 )"))  # => 12
    print(eval("( + ( * 2 2 ) ( + 3 3 ) )"))  # => 10
    print(eval("( + 7 ( * 8 9 ) ( * 2 ( + 9 4 ) 7 ) 3 )")
          )  # => 7 + (8 * 9) + (2 * 13 * 7) + 3
