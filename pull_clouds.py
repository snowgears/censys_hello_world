from datetime import date
from censys.asm import Clouds


# --- functions ---


# --- main thread ---
c = Clouds()

count = c.get_host_counts(date(2021, 1, 1))
print(count)