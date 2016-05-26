from uriparser import URI

uri_str = 'foo://username:password@cars.com:8042/over/there/index.dtb?type=car&name=sadan#engine'
uri = URI(uri_str)
print uri.summary()

uri = URI("mailto:username@example.com?subject=Topic")
print uri.json()
