from lxml import html
import requests
import urllib

f = open('Bank-Currency.txt', 'w')
URL="http://www.banquemisr.com/ar/exchangerates"

def get_URL(url):
	page = requests.get(url)
	tree = html.fromstring(page.content)

	#This will create a list of buyers:
	currencys_1 = tree.xpath('//tbody/tr/td[2]/text()')
	currencys_2 = tree.xpath('//tbody/tr/td[3]/text()')
	currencys_3 = tree.xpath('//tbody/tr/td[4]/text()')
	currencys_4 = tree.xpath('//tbody/tr/td[5]/text()')

	countries = ["US DOLLAR","EURO","GB POUND","SWISS FRANC","DENMARK KRONE","KUWAIT DINAR","SAUDI RIYAL","JORDANIAN DINAR"
	,"BAHRAIN DINAR","QATARI RIAL","OMAN RIYAL","UAE DIRHAM","SWEDISH KRONA","NORWAY KRONE","CANADA DOLLAR","AUSTRALIA DOLLAR","JAPAN YEN"]

	print "\n\n\n                              EGYPTIAN BOUND IN ALL CURRENCIES                      \n"
	a = "Coutnries"+"\t"+"BUY-BankNOTES" +"\t\t"+ "Sell-BankNote"+"\t\t" +" TransferBUY"+"\t\t"+"Transfer-Sell"+"\n";
	print a;
	print "--------------------------------------------------------------------------------------------------------"
	f.write(a);
	i=0
	for currency_1,currency_2,currency_3,currency_4 in zip(currencys_1,currencys_2,currencys_3,currencys_4):
		currency =countries[i]+"\t|\t"+ currency_1 +"\t\t\t"+ currency_2 +"\t\t\t"+ currency_3 +"\t\t"+ currency_4 +"\n"
		f.write(currency.encode('utf-8','strict'))
		print currency
		i+=1

get_URL(URL)