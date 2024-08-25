
def secConvertor(second: int)->int:
    minutes: int = second // 60
    seconds: int = second % 60
    minSec = f"{minutes} min {seconds} s"
    return minSec;


second = int(input("Enter the number of seconds: "))
min_sec : int = secConvertor(second)
print(min_sec)
