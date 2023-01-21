d={
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
    2: ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
    3: ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
    4: ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'],
    5: ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
    8: ['J', 'X', 'Ш', 'Э', 'Ю'],
    10: ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
}

a= str(input('введите слово ')).upper()
sum=0
for  i in a:
    for k, v in d.items():
        if i in v:
            sum = sum + k

print(sum)


# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

# word = input().upper()
# count = 0

# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count += j

#     else:
#         for j in points_ru:
#             if i in points_ru[j]:
#                 count += j

# print(count)
