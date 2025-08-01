import humanize
from datetime import timedelta
duration = timedelta(days = 2, hours=3, minutes=30)
print(humanize.precisedelta(duration))