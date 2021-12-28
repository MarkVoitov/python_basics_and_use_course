import datetime

date = [int(i) for i in input().split()]
days = int(input())

start_time = datetime.date(date[0], date[1], date[2])
period = datetime.timedelta(days=days)

print((start_time + period).strftime("%Y %m %d").replace(" 0", " "))
