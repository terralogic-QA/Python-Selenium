import re

topDomainList = []
websites = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]

for website in websites:
    topDomain = re.findall(r'\w+$', website)
    topDomainList.append(topDomain)

print(topDomainList)
