import time

print("Hitunglah ( a * b ) + ( c / d )")
print("=====================")
a = raw_input("Masukkan nilai a : ")
b = raw_input("Masukkan nilai b : ")
c = raw_input("Masukkan nilai c : ")
d = raw_input("Masukkan nilai d : ")
print("=====================")

t1 = time.time()

if a == 'satu':
        a=1
elif a == 'dua':
        a=2
elif a == 'tiga':
        a=3
elif a == 'empat':
        a=4
elif a == 'lima':
        a=5
elif a == 'enam':
        a=6
elif a == 'tujuh':
        a=7
elif a == 'delapan':
        a=8
elif a == 'sembilan':
        a=9
else :
        a=0

if b == 'satu':
        b=1
elif b == 'dua':
        b=2
elif b == 'tiga':
        b=3
elif b == 'empat':
        b=4
elif b == 'lima':
        b=5
elif b == 'enam':
        b=6
elif b == 'tujuh':
        b=7
elif b == 'delapan':
        b=8
elif b == 'sembilan':
        b=9
else :
        b=0

if c == 'satu':
        c=1
elif c == 'dua':
        c=2
elif c == 'tiga':
        c=3
elif c == 'empat':
        c=4
elif c == 'lima':
        c=5
elif c == 'enam':
        c=6
elif c == 'tujuh':
        c=7
elif c == 'delapan':
        c=8
elif c == 'sembilan':
        c=9
else :
        c=0

if d == 'satu':
        d=1
elif d == 'dua':
        d=2
elif d == 'tiga':
        d=3
elif d == 'empat':
        d=4
elif d == 'lima':
        d=5
elif d == 'enam':
        d=6
elif d == 'tujuh':
        d=7
elif d == 'delapan':
        d=8
elif d == 'sembilan':
        d=9
else :
        d=0


hasil = float((float(a)*float(b))+(float(c)/float(d)))
print 'Hasil : (',a,'*',b,') + (',c,'/',d,') = ', hasil

t2 = time.time()
time =  t2 - t1
print 'Durasi Waktu : %s Detik'% time