import time
import datetime

# TODO: print two lines:
# Line 1: "Seconds since January 1, 1970: <seconds>, <scientific> in scientific notation"
# Line 2: the current date formatted as "Mon DD YYYY"  (e.g. "Oct 21 2022")
#
# Hints:
#   time.time()               -> float: seconds since epoch
#   f"{num:.4f}"              -> 4 decimal places
#   f"{num:.2e}"              -> scientific notation
#   datetime.datetime.now().strftime(...)  -> formatted date
#   strftime format codes: %b = abbreviated month, %d = day, %Y = 4-digit year

# Expected output (values will differ — format must match):
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation
# Oct 21 2022
import time
import datetime

# time since epoch
secs = time.time()

# datetime module has a datetime class 
# but since from x import y is not allowed access goes like this
now = datetime.datetime.now()

print(f"Seconds since January 1, 1970: {secs:,.4f} or {secs:.2e} in scientific notation")
print(now.strftime("%b %d %Y"))       # "formatted to Jun DD MM YYYY"

# scientific notation
