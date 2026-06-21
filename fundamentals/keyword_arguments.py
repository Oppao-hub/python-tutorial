# keyword arguments =   an argument preceded by an identifier
#                       helps with readability
#                       order of arguments doesn't matter
#                       1. positional 2.default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(greeting="Hello", title="Mr.", last="Squarepants", first="Spongebob")

def get_phone(country, area, first, last):
    return f"+{country} {area} {first} {last}"

phone_num = get_phone(country=63, area=926, first=933, last=2782)

print(phone_num)