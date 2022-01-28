import re

pattern = '.*replace_functions\.py'

path = r"C:\Users\danie\Code\python-templates\packaging-python\mycodemod\replace_functions.py"

print(re.fullmatch(pattern, path))