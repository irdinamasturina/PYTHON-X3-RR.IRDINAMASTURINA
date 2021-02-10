num = int(input('bilangan : '))

faktorial = 1

if num < 0:
    print('Maaf, faktorial tidak bisa untuk bilangan negatif')
elif num == 0:
    print('Faktorial dari 0 adalah 1')
else:
    for i in range(1,num+1):
        faktorial = faktorial*i
    print('Faktorial dari',num,'adalah',faktorial)