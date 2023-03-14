print("Hafta 2")
sayi1 = 5
sayi2 = 10
sayi1, sayi2 = sayi2, sayi1

print(sayi1)
print(sayi2)

a = 4
a = a+1
a += 1
print(a)

# Stringler

print("Merhaba Dünya")

print("Merhaba", 4, 5, 2.3, 89.9)
print("Merhaba", "Dünya")

print("Merhaba\nnasılsınız?")

print("Merhaba \tnasılsınız?")

# type fonksiyonu

a = 55
print(type(a))

b = 5.48
print(type(b))

c = "Merhaba"
print(type(c))

# sep parametresi

print(1, 2, 3, 4, 5, sep=",")
print(1, 2, 3, 4, 5, sep=", ")
print(1, 2, 3, 4, 5, sep="-")
print(1, 2, 3, 4, 5, sep="/")

# formatlama

x = 4
y = 8
print("{}+{} nın toplamı {}dir".format(x, y, x+y))
print("{}+{} nın toplamı {}dir".format(3, 9, 9+3))

print("{0} {1} {2}".format(14, 3, 2023))
print("{1} {0} {2}".format(14, 3, 2023))

print("{:.4f} {:.3f} {:.2f}".format(3.234234, 5.8497, 6.1234))

# Liste

list1 = [1, 22, 3, 4, 5, 6]
print(list)
print(type(list))
list2 = ["a", "b", "c"]
print(list2)
list3 = ["merhaba", "dünya"]
print(list3)
emptyList = []
print(type(emptyList))

# Listenin boyutu

print(len(list1))
s = "mustafa"
listee = list(s)
print(listee)

list5 = [1, 2, 3, 4, 5]
print(list5[2])

# Listenin ilk elemanına ulaşmak için
print(list5[-len(list5)])

print(list5[:3])
print(list5[::2])
print(list5[::-1])

# liste işlemleri

list5 = list1+list2
print(list5)

list3.extend(list1)
print(list3)

list1 = list1+[4]
print(list1)
emptyList = emptyList+[1]
print(emptyList)

empty = [200, 300, 400]
print(empty)

list2 = list2 + ["d"]
print(list2)

print(list2 * 2)


liste1 = [0, 1, 2, 3]
liste1. append(4)
print(liste1)
bos_liste3 = []
bos_liste3. append(200)
# reverse
liste1. reverse()
print(liste1)
# pop
liste1. pop()
print(liste1)
liste1.pop(0)
print(liste1)
# son eleman1 cikarir ve yazdirir
# indeksi 0 olan elamn1 cikar ve yazdir

liste1 = [2, 3, 56, 8, 9, 4, 8, 1, 99, 45]
liste1. sort()
print(liste1)
liste1.sort(reverse=True)  # b -> k

# iç içe listeler
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
listeb = [11, 12, 13]
listeb =[l1,l2,l3]
print(len(listeb))
print(listeb)
