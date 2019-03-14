def print_root(a, b, c):
    r1 = (-b + (b** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('하는 {} 또는 {}'.format(r1, r2))


a = 1
b = 2
c = -8

# a * x^2 + b * x + c = 0, a != 0 인 x에 관한 2차방정식에 대해,
# 근의 공식은

print_root(a, b, c)

a = 2
b = -6
c = -8

print_root(a, b, c)

def print_round(number):
    rounded = round(number)
    print(rounded)

print_round(4.6)
print_round(2.2)
print_round(1.2)