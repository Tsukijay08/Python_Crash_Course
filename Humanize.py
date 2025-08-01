import humanize
from datetime import datetime

some_date = datetime(1996,12,8)
print(humanize.naturaldate(some_date))
