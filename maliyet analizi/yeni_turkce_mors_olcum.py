harf_maliyetleri = {
    'a': 1, 'e': 3, 'i': 3, 'n': 5, 'r': 5, 'l': 5, 
    'd': 7, 'k': 7, 'ı': 7, 'm': 7, 't': 7, 
    'y': 9, 'u': 9, 's': 9, 'b': 9, 'o': 9, 'ü': 9, 'z': 9, 'ş': 9, 
    'g': 11, 'h': 11, 'ç': 11, 'c': 11, 'ğ': 11, 'v': 11, 'p': 11, 'ö': 11, 'f': 11, 'j': 11
}

metin_maliyeti = 0
bosluklar=0

with open("metin.txt", "r", encoding="utf-8") as dosya:
    metin = dosya.read().lower()
    
    for harf in metin:
        if harf in harf_maliyetleri:
            metin_maliyeti += harf_maliyetleri[harf] 
            bosluklar += 3
            
        elif harf == ' ' or harf == '\n':
            bosluklar += 4

metin_maliyeti -= 1

toplam_karakter = sum(1 for h in metin if h in harf_maliyetleri or h == ' ' or h == '\n')
print(f"Harf Maliyeti: {metin_maliyeti} Boşluk Maliyeti: {bosluklar} Toplam Maliyet: {metin_maliyeti+bosluklar} | Toplam Karakter: {toplam_karakter} | Ort. İletim Hızı: {(metin_maliyeti+bosluklar)/toplam_karakter:.4f}")