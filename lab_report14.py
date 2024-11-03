import cmath

def find_roots(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + d) / (2*a)
    root2 = (-b - d) / (2*a)
    
    return root1, root2


a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))


roots = find_roots(a, b, c)

print(f"The roots of the equation are: {roots}")

