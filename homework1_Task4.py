# можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками#


# чтобы можно было отломить k долек, нужно: чтобы количество долек было крат или одной или другой стороне

m=int(input('введите ширину шоколада'))
n=int(input('введите длину шоколада'))
k=int(input('введите количество долек, которое хотите отломить'))
if (n*m<k) and (k%m==0 or k%n==0):
    print('можно отломить')
else:
    print('нельзя отломить')