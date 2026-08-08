harf_maliyetleri = {
    'a': 5,   # .-       (1 + 1 + 3)
    'b': 9,   # -...     (3 + 1 + 1 + 1 + 1 + 1 + 1)
    'c': 11,  # -.-.     (3 + 1 + 1 + 1 + 3 + 1 + 1)
    'ç': 13,  # -.-..    (3 + 1 + 1 + 1 + 3 + 1 + 1 + 1 + 1)
    'd': 7,   # -..      (3 + 1 + 1 + 1 + 1)
    'e': 1,   # .        (1)
    'f': 9,   # ..-.     (1 + 1 + 1 + 1 + 3 + 1 + 1)
    'g': 9,   # --.      (3 + 1 + 3 + 1 + 1)
    'ğ': 15,  # --.-.    (3 + 1 + 3 + 1 + 1 + 1 + 3 + 1 + 1)
    'h': 7,   # ....     (1 + 1 + 1 + 1 + 1 + 1 + 1)
    'ı': 3,   # ..       (1 + 1 + 1)
    'i': 3,   # ..       (1 + 1 + 1)
    'j': 13,  # .---     (1 + 1 + 3 + 1 + 3 + 1 + 3)
    'k': 9,   # -.-      (3 + 1 + 1 + 1 + 3)
    'l': 9,   # .-..     (1 + 1 + 3 + 1 + 1 + 1 + 1)
    'm': 7,   # --       (3 + 1 + 3)
    'n': 5,   # -.       (3 + 1 + 1)
    'o': 11,  # ---      (3 + 1 + 3 + 1 + 3)
    'ö': 13,  # ---.     (3 + 1 + 3 + 1 + 3 + 1 + 1)
    'p': 11,  # .--.     (1 + 1 + 3 + 1 + 3 + 1 + 1)
    'r': 7,   # .-.      (1 + 1 + 3 + 1 + 1)
    's': 5,   # ...      (1 + 1 + 1 + 1 + 1)
    'ş': 15,  # ----     (3 + 1 + 3 + 1 + 3 + 1 + 3)
    't': 3,   # -        (3)
    'u': 7,   # ..-      (1 + 1 + 1 + 1 + 3)
    'ü': 11,  # ..--     (1 + 1 + 1 + 1 + 3 + 1 + 3)
    'v': 9,   # ...-     (1 + 1 + 1 + 1 + 1 + 1 + 3)
    'y': 13,  # -.--     (3 + 1 + 1 + 1 + 3 + 1 + 3)
    'z': 11   # --..     (3 + 1 + 3 + 1 + 1 + 1 + 1)
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