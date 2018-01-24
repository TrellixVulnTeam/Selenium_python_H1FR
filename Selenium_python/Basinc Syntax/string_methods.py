"""
Examples to show available string methods in python
"""

# Accessing characters in a string
#index starts from zero

first = "nyc"[0]
print(first)

city = "sfo"
ft = city[0]
print(ft)


"""
len()
lower()
upper()
str()
"""

string_var = "This is a mixed case "

print(string_var.lower())
print(string_var.upper())
print(len(string_var))

print(string_var + str(2)) # in ruby .to_s

"""
Concationation
"""

print("Hello" + " " + "Worlds")
