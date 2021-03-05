'''Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede
následující činnosti:
- Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
- Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:
První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné
(pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí
hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla.
Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí
její cenu, kterou vypíše uživateli.'''

def kontrolaCisla(cislo):
    cislo = cislo.replace(" ", "")
    if(len(cislo) == 9 or (len(cislo) == 13 and cislo[0] == "+")):
        return True
    else:
        return False

def cenaSMSky(text):
    text = text.replace(" ", "")
    if(text != ""):
        # přičtu si jedničku, abych spočítal cenu SMS
        cenaSMS = ((len(text) // 180) + 1) * 3
        return cenaSMS
    else:
        # pro případ, že nezadáme text
        cenaSMS = 0
        return cenaSMS

cislo = input("Zadej číslo, kam máme poslat SMSku: ")
if(kontrolaCisla(cislo)):
    zprava = input("Zadej zprávu, kterou chceš odeslat: ")
    print("Cena vaší SMSky je: " + str(cenaSMSky(zprava)) + " Kč.")
else:
    print("Vaše číslo má chybný formát!")