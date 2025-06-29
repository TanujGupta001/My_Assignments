import pandas as pd
import numpy as np
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)


date_str = "2025-06-29 11:30:00"
dt_object = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt_object)

from datetime import datetime, timedelta
future_date = datetime.now() + timedelta(days=7)
past_time = datetime.now() - timedelta(hours=3)
print(future_date)
print(past_time)


original_dt = datetime(2025, 6, 29, 10, 0, 0)
new_dt = original_dt.replace(hour=15, minute=30)
print(new_dt)