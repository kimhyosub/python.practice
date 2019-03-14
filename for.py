
patterns = ['가위', '바위', '보','가위', '바위', '보','가위', '바위', '보','가위', '바위', '보','가위', '바위', '보']

for pattern in patterns:
    print(pattern)

for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(20):
     print(i)  

names = ['철수','영희', '바둑이','비단뱀']

for i in range(len(names)):
    print(i)

for i, name in enumerate(names):
    print('{}번: {}'.format(i+1, name))

for i in range(11172):
    print(chr(44032+i), end='')