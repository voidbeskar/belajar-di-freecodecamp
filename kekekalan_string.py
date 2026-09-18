#contoh
my_str_1 = 'Hello'
my_str_2 = "World"

#string multi_baris
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''

#Gunakan jenis tanda kutip yang berlawanan. Artinya, jika string Anda berisi tanda kutip tunggal, gunakan tanda kutip ganda untuk membungkus string, dan sebaliknya:
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

#Gunakan garis miring terbalik (\) untuk mengescape tanda kutip tunggal atau ganda dalam string \. Dengan metode ini, Anda dapat menggunakan tanda kutip tunggal atau ganda untuk membungkus string itu sendiri:
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

#contohy_str = 'Hello world'

my_str = "hello world"

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

#proses pengindeksan 
y_str = 'Hello world'
print(len(my_str))  # 11

#posisi indeks
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

#Pengindeksan negatif
my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l

#penugasan ulang utable (dapat diubah) atau immutable (tidak dapat diubah).
#contoh

#utable
reeting = 'hi'
greeting = 'hello'
print(greeting) # hello

#immutable
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment



