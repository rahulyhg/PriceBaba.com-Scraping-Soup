from bs4 import BeautifulSoup
import requests
import copy
#1- 2- 3- 4- 5- 6-
def retrieval(input):
    input = input -1
    base1 = "http://pricebaba.com/"
    base2 = "/pricelist/all-"
    base3 = "-in-india?page="
    category = ["Mobile","Laptop","Tablet","Smartwatch","television","refrigerators","Microwaves","Washing-Machine"]
    new_category = copy.copy(category)
    if input==0 or input==1:
        new_category[input] = new_category[input] + "s-sold"

    if input==2 or input==3 or input==4 or input==7:
        new_category[input] = new_category[input] + "s"

    if input==5:
        new_category[input] = new_category[input] + "-sold"



    range_category = [48,31,10,3,21,13]
    count = 0
    for i in range(0,range_category[input]):
        x = base1 + str(category[input]) + base2 + str(new_category[input]) + base3 + str(i)
        item = {}
        page = requests.get(x)
        souped = BeautifulSoup(page.text,"lxml")

        tag = souped.find_all('div')[0].find_all(class_='prdp')
        #tag = souped.find_all(class_='carbrandpage')[0].find_all(class_='clearfix')


        for tags in tag:
            name = tags.find_all(class_='prdp-ttl')[0].text
            price = tags.find_all(class_='prdp-prc')[0].text

            if name in item.keys() or price == " - ":
                pass
            else:
                print "%s costs%s" %(name, price)
                count = count + 1

    print "\nThe total number of items listed = %d \n\n " %(count)

def main():


    input = int(raw_input("""Which category ? \n Press 1 for Mobiles \n Press 2 for Laptops
                           \n Press 3 for Tablets \n Press 4 for Smartwatches \n Press 5 for TV's
                          \n Press 6 for Refrigerators\n Press 7 for Microwaves \n Press 8 for Washing Machines \n \n """))

    if input<=0 or input>8:
        print "Error"
        pass


    if input == 1:
        retrieval(input)

    if input == 2:
        retrieval(input)

    if input == 3:
        retrieval(input)

    if input == 4:
        retrieval(input)

    if input == 5:
        retrieval(input)

    if input == 6:
        retrieval(input)

    if input == 7:
        retrieval(input)

    if input == 8:
        retrieval(input)





main()