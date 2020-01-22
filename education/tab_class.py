# Save the input in this variable
import math
import re

class_a = abs(int(input()))
class_b = abs(int(input()))
class_c = abs(int(input()))

class_a /= 2
class_b /= 2
class_c /= 2

tables = math.ceil(class_a) + math.ceil(class_b) + math.ceil(class_c)

print(int(tables))
