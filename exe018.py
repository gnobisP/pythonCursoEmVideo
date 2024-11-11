from math import sin, cos, tan, pi
angulo = float(input("Digite um ângulo: "))
angulo_rad = (angulo*pi)/180
print("O seno de {} vale: {:.3f}".format(angulo, sin(angulo_rad)))
print("O cosseno de {} vale: {:.3f}".format(angulo, cos(angulo_rad)))
print("A tangente de {} vale: {:.3f}".format(angulo, tan(angulo_rad)))
