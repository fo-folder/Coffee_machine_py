# Save the input in this variable
import re

ticket = int(input())
# Add up the digits for each half
# noinspection PyTypeChecker
if ticket < 1000:
    half1 = 0
    half2 = (ticket // 100) + ((ticket % 100) // 10) + ((ticket % 100) % 10)
else:
    half2 = (ticket // 100000) + (((ticket // 1000) % 100) // 10) + (((ticket // 1000) % 100) % 10)
    half1 = ((ticket % 1000) // 100) + (((ticket % 1000) % 100) // 10) + (((ticket % 1000) % 100) % 10)
# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")