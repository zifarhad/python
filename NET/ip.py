#!/usr/bin/python3

from pierky.ipdetailscache import IPDetailsCache
cache = IPDetailsCache()
result = cache.GetIPInformation('178.22.122.248')
print(result)

