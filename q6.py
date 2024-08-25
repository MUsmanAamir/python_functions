
def secConvertor(second: int)->int:
    minutes: int = second // 60
    seconds: int = second % 60
    print(minutes, "min", seconds, "s")


second = int(input("Enter the number of seconds: "))
print(secConvertor(second))
