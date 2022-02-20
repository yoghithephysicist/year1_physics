import math


def calcvolsph(r):
    return (4/3) * math.pi * (r ** 3)


def sigmavolsph(r, sigma):
    return sigma * 4 * math.pi * (r ** 2)


def calcvolprll(x, y, z):
    return x * y * z


def sigmavolprll(x, y, z, sigma):
    return math.sqrt(((sigma * y * z) ** 2) + ((sigma * x * z) ** 2) + ((sigma * x * y) ** 2))


def calcvolclnd(r, h):
    return (r ** 2) * math.pi * h


def sigmavolclnd(r, h, sigma):
    return math.sqrt(((sigma * 2 * r * h) ** 2) + ((sigma * (r ** 2)) ** 2))


def calcdens(m, v):
    return m / v


def sigmadens(m, vol, sigma_m, sigma_vol):
    return math.sqrt(((sigma_m * (1 / vol)) ** 2) + ((sigma_vol * (m / -(vol ** 2))) ** 2))


'''raggio = float(input("Diametro [mm]: ")) / 2
sigma_raggio = float(input("Sigma Diametro [mm]: ")) / 2
result1 = f"Volume Sphere [mm^3] = {calcvolsph(raggio)} +/ {sigmavolsph(raggio, sigma_raggio)}"
print(result1)

lung = float(input("Lunghezza [mm]: "))
larg = float(input("Larghezza [mm]: "))
alt = float(input("Altezza [mm]: "))
sigma_dim = float(input("Sigma Dimension [mm]: "))
result2 = f"Volume Parallelepipedo [mm^3] = {calcvolprll(lung, larg, alt)} +/ {sigmavolprll(lung, larg, alt, sigma_dim)}"
print(result2)'''

'''raggio = float(input("Diametro [mm]: ")) / 2
alt = float(input("Altezza [mm]: "))
sigma_raggio = float(input("Sigma Diametro [mm]: ")) / 2
result3 = f"Volume Cilindro [mm^3] = {calcvolclnd(raggio, alt)} +/ {sigmavolclnd(raggio, alt, sigma_raggio)}"
print(result3)'''

'''massa = float(input("Massa [g]: "))
volume = float(input("Volume [mm^3]: "))
sigma_massa = float(input("Sigma Massa [g]: "))
sigma_volume = float(input("Sigma Volume [mm^3]: "))
result4 = f"Densità Sfera [g/mm^3] = {calcdens(massa, volume)} +/ {sigmadens(massa, volume, sigma_massa, sigma_volume)}"
print(result4)'''

