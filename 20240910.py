def dividir(a:float, b:float):
    try:
        return a / b
    except:
        print ("não é possível dividir por zero")
    return ""

print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, 5))

dividir(input())
