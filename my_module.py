
def random_rsp():
    """무작위로 가위나 바위나 보를 낸다 """
    import random
    return random.choice(['가위', '바위', '보'])


PAPER = '보'
ROCK = '바위'
SCISSOR = '가위'