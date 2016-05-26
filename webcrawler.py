import requests
import re
from lxml import html
import argparse
parser = argparse.ArgumentParser(description='Shopping.com crawler')

parser.add_argument('--q', metavar='key', type=str, nargs='+',
                    help='Keyword to be searched')

parser.add_argument('--i', metavar='page_number', type=int, nargs='+',
                    help='Page number for the given keyword')

args = parser.parse_args()
p = re.compile(ur'of (\d+\+?)')


def get_vals(keyword, page_number=0):
    '''
        This Function takes keyword and page number(optional).
        It can return two type of value depending upon number of
        argument passed 
        Q1 = keyword 
        returns => number of product for keyword
        
        Q2 = keyword, page number
        returns = product details(name, link, price)
    '''
    page_num = 1
    p_list = []
    second_query = False
    
    # detecting type of query made
    if page_number != 0:
        page_num = page_number
        second_query = True
    # building url and fectching data
    url = "http://www.shopping.com/" + keyword + "/products~PG-" \
        + str(page_num) + "?KW=" + keyword
    timeout = 15
    response = requests.get(url, timeout=timeout,
                            headers={'Accept-Encoding': 'gzip',
                                     'User-Agent': '''Mozilla/5.0 (X11; Linux x86_64; rv:41.0)
                                      Gecko/20100101 Firefox/41.0'''})
    data = response.content
    tree = html.fromstring(data)
    total_product = (tree.xpath('//span[@class="numTotalResults"]/text()'))    
    # if its a second type of query than finding other details
    # about the product
    if second_query:
        product_name = (tree.xpath('//div[@class="gridItemBtm"]/h2'))
        price = (tree.xpath('//div[@class="gridItemBtm"]/div'
                            '/span[starts-with(@class,"productPrice")]/a'
                            '//text()|//span[starts-with'
                            '(@class,"productPrice")]/text()'))
        link = (tree.xpath('//div[@class="gridItemBtm"]/h2/a/@href'))
        product_name = [i.xpath('descendant-or-self::text()')
                        for i in product_name]
        for p in product_name:
            if p is not None:
                p_name = " ".join((" ".join(p)).strip().split())
                p_list.append(p_name)

        price = map((lambda x: x.replace('\n', "")), price)
        price = map((lambda x: x.replace('\t', "")), price)
        price = [x for x in price if x != ""]
        prod_num = len(p_list)
        link_num = len(link)
        price_num = len(price)
        print "Product Name Found=> ", prod_num
        print "Product Link Found =>", link_num
        print "Product Price => ", price_num
        if prod_num == link_num == price_num:
            out = zip(p_list, link, price)
            for o in out:
                print o
        else:
            print "[ERROR]: Any one of product name, link, price is not found"

    if total_product:
        total_list = total_product[0].split()
        if len(total_list) == 6:
            print "Total number of product found => ", total_list[5]
        else:
            print "0 product found"
    else:
        print "[ERROR]: Given page dosen't exist for given keyword"

if args.i:
    get_vals(args.q[0], args.i[0])
elif args.q:
    get_vals(args.q[0])
else:
    print "[ERROR]: No parameter were given"
    print "[Useage]: webcrawler.py [-h] [--q key [key ...]][--i page_number [page_number ...]]"
