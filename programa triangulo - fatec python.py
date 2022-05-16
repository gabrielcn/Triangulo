#Programa Triangulo
A=int(input("Informe valor de A"))
B=int(input("Informe valor de B"))
C=int(input("Informe valor de C"))
if A<B+C and B<A+C and C<A+B:
    if A==B and B==C:
        print("Triangulo Equilatero")
    else:
        if A==B or A==C or C==B:
            print("Triangulo Isosceles")
        else:
            print("Triangulo Escaleno")
else:
    print("Nao forma Triangulo")
