
# Raqamli masalalar

num = float(input("Son kiriting: "))
print("Yaxlitlangan:", round(num, 2))

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
c = float(input("Uchinchi sonni kiriting: "))
print("Eng katta:", max(a, b, c))
print("Eng kichik:", min(a, b, c))

km = float(input("Kilometr kiriting: "))
print("Metr:", km * 1000)
print("Santimetr:", km * 100000)

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
print("Butun bo'lish:", a // b)
print("Qoldiq:", a % b)

celsius = float(input("Selsiy darajasini kiriting: "))
fahrenheit = (celsius * 9/5) + 32
print("Farangeyt:", fahrenheit)

num = int(input("Son kiriting: "))
print("Oxirgi raqam:", abs(num) % 10)

num = int(input("Son kiriting: "))
print("Juft" if num % 2 == 0 else "Toq")

# Matnli masalalar

ism = input("Ismingizni kiriting: ")
yil = int(input("Tug'ilgan yilingizni kiriting: "))
from datetime import datetime
yosh = datetime.now().year - yil
print(f"{ism}, siz {yosh} yoshdasiz.")

matn = input("Matn kiriting: ")
print("Uzunligi:", len(matn))
print("Katta harfda:", matn.upper())
print("Kichik harfda:", matn.lower())

text = input("Matn kiriting: ").replace(" ", "").lower()
print("Palindrom" if text == text[::-1] else "Palindrom emas")

text = input("Matn kiriting: ").lower()
unli = "aeiouаеёиоуыэюя"
undosh = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
u = sum(1 for x in text if x in unli)
c = sum(1 for x in text if x in undosh)
print("Unli:", u)
print("Undosh:", c)

s1 = input("Birinchi matnni kiriting: ")
s2 = input("Ikkinchi matnni kiriting: ")
print("Ichida bor" if s2 in s1 else "Yo'q")

text = input("Gapni kiriting: ")
old = input("Qaysi so'zni almashtirasiz: ")
new = input("Qaysi so'zga: ")
print("Natija:", text.replace(old, new))

text = input("Matn kiriting: ")
if text:
    print("Birinchi harf:", text[0])
    print("Oxirgi harf:", text[-1])

text = input("Matn kiriting: ")
print("Teskari:", text[::-1])

gap = input("Gap kiriting: ")
print("So'zlar soni:", len(gap.split()))

text = input("Matn kiriting: ")
print("Raqam bor" if any(char.isdigit() for char in text) else "Raqam yo'q")

words = input("So'zlarni kiriting (bo'sh joy bilan): ").split()
sep = input("Ajratuvchi belgini kiriting: ")
print(sep.join(words))

text = input("Matn kiriting: ")
print("Bo'shliqsiz:", text.replace(" ", ""))

s1 = input("1-matn: ")
s2 = input("2-matn: ")
print("Teng" if s1 == s2 else "Teng emas")

gap = input("Gap kiriting: ")
abbr = ''.join(word[0].upper() for word in gap.split())
print("Qisqartma:", abbr)

text = input("Matn kiriting: ")
char = input("Qaysi belgini o'chirasiz: ")
print("Natija:", text.replace(char, ""))

text = input("Matn kiriting: ")
unli = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
result = ''.join('*' if c in unli else c for c in text)
print("Natija:", result)

text = input("Matn kiriting: ")
start = input("Boshlanadi: ")
end = input("Tugaydi: ")
print("Mos" if text.startswith(start) and text.endswith(end) else "Mos emas")

# Mantiqiy masalalar

foydalanuvchi = input("Foydalanuvchi nomi: ")
parol = input("Parol: ")
print("To'ldirilgan" if foydalanuvchi and parol else "Bo'sh maydon bor")

a = int(input("1-son: "))
b = int(input("2-son: "))
print("Teng" if a == b else "Teng emas")

num = int(input("Son kiriting: "))
print("Musbat va juft" if num > 0 and num % 2 == 0 else "Mos emas")

a = int(input())
b = int(input())
c = int(input())
print("Barcha sonlar har xil" if a != b and b != c and a != c else "Tenglar bor")

s1 = input("1-matn: ")
s2 = input("2-matn: ")
print("Uzunligi teng" if len(s1) == len(s2) else "Uzunligi har xil")

num = int(input("Son kiriting: "))
print("3 va 5 ga bo'linadi" if num % 3 == 0 and num % 5 == 0 else "Bo'linmaydi")

a = float(input())
b = float(input())
print("Yig'indisi 50.8 dan katta" if a + b > 50.8 else "50.8 yoki kichik")

num = int(input("Son kiriting: "))
print("10-20 oralig'ida" if 10 <= num <= 20 else "Tashqarida")
