# from currency_converter import CurrencyConverter
# import CurrencyConverter as CurrencyConverter
import currency_converter  as CurrencyConverter

c=CurrencyConverter()
# print(c.convert(100,'EUR','USD'))
currency=input("enrery to amount")
Cuurencys=c.convert(100,'EUR',currency)
print(Cuurencys)