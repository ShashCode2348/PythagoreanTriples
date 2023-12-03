from sys import exit as ex
def method1(inp_len, inp_type): #Gives a Pythagorean triple if the short side is odd
    if inp_type == 0:           #Short side(a) given
        a = inp_len
        b = inp_len**2/2 - 0.5
        c = b + 1
    elif inp_type == 1:         #Long side(b) given
        a = (2*inp_len + 1)**(1/2)
        b = inp_len
        c = inp_len + 1
    elif inp_type == 2:         #Hypotenuse(c) given
        a = (2*inp_len - 1)**(1/2)
        b = inp_len - 1
        c = inp_len
    else:
        ex('Incorrect input')
    return [a, b, c]

def method2(inp_len, inp_type): #Gives a Pythagorean triple if the short side is even
    if inp_type == 0:           #Short side(a) given
        a = inp_len
        b = inp_len**2/4 - 1
        c = b + 2
    elif inp_type == 1:         #Long side(b) given
        a = (4*inp_len + 4)**(1/2)
        b = inp_len
        c = inp_len + 2
    elif inp_type == 2:         #Hypotenuse(c) given
        a = (4*inp_len - 4)**(1/2)
        b = inp_len - 2
        c = inp_len
    else:
        ex('Incorrect input')
    return [a, b, c]

input_length = int(input('Enter the length of the given side: '))
input_type = int(input('Enter 0 if the given side is the shortest side(a), 1 if it is the longer side(b), and 2 if it is the hypotenuse(c): '))
if input_type == 0:
    if input_length % 2 == 0:
        [a, b, c] = method2(input_length, 0)
    elif input_length % 2 == 1:
        [a, b, c] = method1(input_length, 0)
elif input_type == 1:
    [a1, b1, c1] = method1(input_length, 1)
    if list(map(int, [a1, b1, c1])) == [a1, b1, c1]:
        a, b, c = a1, b1, c1
    else:
        [a2, b2, c2] = method2(input_length, 1)
        if list(map(int, [a2, b2, c2])) == [a2, b2, c2]:
            a, b, c = a2, b2, c2
        else:
            ex('The given length cannot form a Pythagorean triple')
elif input_type == 2:
    [a1, b1, c1] = method1(input_length, 2)
    if list(map(int, [a1, b1, c1])) == [a1, b1, c1]:
        a, b, c = a1, b1, c1
    else:
        [a2, b2, c2] = method2(input_length, 2)
        if list(map(int, [a2, b2, c2])) == [a2, b2, c2]:
            a, b, c = a2, b2, c2
        else:
            ex('The given length cannot form a Pythagorean triple')
else:
    ex('An incorrecct value has been entered')
print(f'The Pythagorean triple is {int(a)}, {int(b)}, {int(c)}')
