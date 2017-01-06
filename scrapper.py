from bs4 import BeautifulSoup
import requests


def main():

    base = "http://pricebaba.com/mobile/pricelist/android-phones-price-list?page="
    count = 0
    for i in range(0,48:
        x = base+str(i)
        mobile = {}
        page = requests.get(x)
        souped = BeautifulSoup(page.text,"lxml")

        tag = souped.find_all('div')[0].find_all(class_='prdp')
        #tag = souped.find_all(class_='carbrandpage')[0].find_all(class_='clearfix')


        for tags in tag:
            name = tags.find_all(class_='prdp-ttl')[0].text
            price = tags.find_all(class_='prdp-prc')[0].text

            if name in mobile.keys() or price == " - ":
                pass
            else:
                print "%s costs%s" %(name, price)
                count = count + 1

    print "The total number of phones = %d" %(count)
main()
