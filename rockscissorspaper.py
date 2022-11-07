import random

def switch(data):
    if data == '가위':
        return 0
    elif data == '바위':
        return 1
    elif data == '보':
        return 2

def rsp(user):
    bot = random.randrange(3)
    botstatus = lambda bot: '가위' if bot == 0 else ('바위' if bot == 1 else '보')
    print(bot)
    print(botstatus(bot))
    if user == bot:
        return "무승부", botstatus(bot)
    elif user == 0 and bot == 2:
        return "승리", botstatus(bot)
    elif user == 2 and bot == 0:
        return "패배", botstatus(bot)
    elif user > bot:
        return "승리", botstatus(bot)
    else:
        return "패배", botstatus(bot)
