# encoding:utf-8
a = 10
b = 5.0
c = float(a)
print(a)
print(b)
print(float(a))
print(int(b))
print(int(45.4))
print(float(25))
a = 4589
b = str(a)
print(b)
m = "merhaba"
print(len(m))  # len sadece stringler için
c = 45.12
d = str(c)
print(len(d))

a = "4589"
b = int(a)
print(a)
a = "25.12"
b = float(a)
print(b)

c = "45.12asdeer"
# d=float(c) #hatalı
# Matematiksel Operatorler
x = 23
y = 6
z = 12
print(x + y)
print(x + y + z)
print(x - z)
print(y * z)
print(z / y)  # int / int = float
# tam bölme
print(x // y)

# mod alma
print(x % y)
# kuvvet alma
print(z ** y)
print(2 ** 3)

print(25 ** 0.5)  # karakok
print(10 ** -3)
print(-z)
# işlem önceliği
# parantez içi
# kuvvet alma
# çarpma / bolme
# toplama / çıkarma
# sol --> sağ
print(9 + 5 // 2 - 2 * 3)
print(5 ** 4 / 2)
print(8 / 4 ** 2)
# String
print("Merhaba Dünya")
print('Merhaba Dünya')

isim = "Mustafa"
print(isim)
print(isim[-1])
a = "Python Programlama"
a[2:10]  # bitiş değeri dahil değil
print(a[2:10])
print(a[:10])
# a[başlangıç değeri : bitiş değeri (dahil değil) : artış miktari]
a[::-1]  # tersten yazdırma
print(a[::-1])
print(len(a))
x = "Merhaba"
y = "Dünya"
print(x + y)
print(x * 3)
# - / + kullanılmaz

sayi1 = 23
sayi2 = 34
sayi = sayi1 + sayi2
print(sayi)
# değişkenler sayi ile başlamaz.
