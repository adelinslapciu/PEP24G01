str1 = 'hello word'
print(type(str1))
int1 = 100
print(type(str1))
none = None
print(type(str1))

result = str1.capitalize()
print('Returned type' , type(str1))


str1 = 'hello word {} {}'
result = str1.format( 'test','test2')
print('Formatted String:', result)

str1 = ('hello word')
result = str1.center(20, '#')
print('Formatted String:', result)
