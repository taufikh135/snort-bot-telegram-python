import re

text = '05/25-07:52:55.923404  [**] [1:1228:7] SCAN nmap XMAS [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.5.100:47222 -> 192.168.5.98:23'
regex = r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
result = re.findall(regex, text)
print(result)