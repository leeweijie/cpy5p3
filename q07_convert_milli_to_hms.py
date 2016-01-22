import datetime


def convert_ms(n):
    n //= 1000
    hours = n // 3600
    minutes = (n % 3600) // 60
    seconds = n - (hours*3600) - (minutes*60)
    return ":".join(str(i) for i in [hours, minutes, seconds])

print(convert_ms(555550000))
