"""
Exsmples to show available string methods in python
"""
# Replace method
a = "asdfllkjoasdfqwirue"

print(a.replace('asdf','ASDF'))

# Sub-strings
# Staring index is inclusive / ending index is exclusive
sub = a[1:6] # in ruby 1..6
step = a[1:6:2]
print(sub)
