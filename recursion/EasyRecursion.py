
# simple recursion practice using python

n = 10
def print_numbers_from10to1(n):
    if n == 0:
        return 

    print(n, "n")
    print_numbers_from10to1(n - 1)

print_numbers_from10to1(n)


m = 1
def print_numbers_from1to10(m):
    if m > 10:
        return
    
    print(m, "m")
    print_numbers_from1to10(m + 1)

print_numbers_from1to10(m)


o = 10
def print_nums_from1to10(o):
    if o > 1:
      print_nums_from1to10(o - 1)

    print(o, "o")
    return

print_nums_from1to10(o)


p = 1
def print_nums_from10to1(p):
    if p < 10:
      print_nums_from10to1(p + 1)

    print(p, "p")
    return

print_nums_from10to1(p)

