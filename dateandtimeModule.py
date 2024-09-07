import datetime

print(dir(datetime))
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import datetime

y = datetime.datetime(2024,9,7)
print(y)

print(x.strftime("%B"))