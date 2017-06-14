def salgan(numero):
    a="salgan al sol, "
    b=["revienten", "", "idiotas","paquetes"]
    if numero == 1:
        for i in range(2):
            print (a + b[i])
        print(a + b[3])
    else:
        for i in range(2):
            print(a + b[i])
        print(a + b[2])
