Coding Assignment
=========


### Reverse Hashing
    usage: reverse_hash.py [-h] hash [hash ...]

### Shopping.com crawler

    usage: webcrawler.py [-h] [--q key [key ...]][--i page_number [page_number ...]]

  1. known bugs : 
      shopping.com has lot of product link in javascript file which 
      assign link on-click event for such link crawler currently shows as "javascript:void(0)" which is intial default of product href.

### URI Parser:
URI parser for Python that supports many schemes (URLs, mailto, ...)

To see the output for URI parser please run uriparser_run.py
Doing this...

    from uriparser import URI
    uri_str = 'foo://username:password@cars.com:8042/over/there/index.dtb?type=car&name=sadan#engine'
    uri = URI(uri_str)
    print uri.summary()

...will output:

    foo://username:password@cars.com:8042/over/there/index.dtb?name=sadan&type=car#engine
    * Schema name: 'foo'
    * Authority path: '//username:password@cars.com:8042'
      . Hostname: 'cars.com'
      . User information = 'username:password'
      . Port = '8042'
    * Path: '/over/there/index.dtb'
    * Query parameters: '{'type': 'car', 'name': 'sadan'}'
    * Fragment: 'engine'


You can also serialize the structured URI as JSON. For instance, this...

    uri = URI("mailto:username@cars.com?subject=Topic")
    print uri.json()

... will output:

    {
      "authority": null, 
      "fragment": null, 
      "parameters": {
        "subject": "topic"
      }, 
      "path": "username@cars.com", 
      "scheme": "mailto"
    }
