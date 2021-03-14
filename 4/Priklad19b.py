'''https://www.kurzy.cz/komodity/bitcoin-graf-vyvoje-ceny/'''
'''https://github.com/MicroPyramid/forex-python/blob/master/tests/test_bitcoin.py'''

from forex_python.bitcoin import (get_btc_symbol, convert_btc_to_cur_on, convert_to_btc_on,
                            convert_btc_to_cur, convert_to_btc, get_latest_price,
                            get_previous_price, get_previous_price_list, BtcConverter)

prevodnik = BtcConverter()

print(prevodnik.get_latest_price('USD'))
print(prevodnik.get_latest_price('CZK'))

kolik = int(input("Jaké množství Kč chcete vyměnit: "))
print(prevodnik.convert_to_btc(kolik, 'CZK'))
