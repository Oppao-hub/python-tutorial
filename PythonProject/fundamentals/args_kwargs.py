# *args = allow you to pass multiple non-key arguments
# **kwargs = allow you to pass multiple keyword-arguments
#             *unpacking operator
#             1. positional 2.default 3. keyword 4. Arbitrary

from multiprocessing import Value


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

print(add(1,2,3,4))
print()

print_address(
    street="Malatapay", 
    barangay="Maluay", 
    city="Zamboanguita", 
    province="Negros Oriental",
    country="Philippines",
    pobox="PO box #1005"
)
print()

shipping_label(
    "Dr.",
    "Spongebob",
    "Squarepants",
    "III",
    street="Malatapay",
    barangay="Maluay",
    city="Zamboanguita",
    province="Negros Oriental",
    country="Philippines"
)