# TODO Найдите количество книг, которое можно разместить на дискете
V = 4
Pages = 100
Strings = 50
Elements = 25
All_V = 1.44
x = int(Pages*Strings*Elements*V)
y = int(All_V*1024**2)
print("Количество книг, помещающихся на дискету:", int(y/x))
