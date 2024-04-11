ip = list(input().split(':'))

if ip[0] == '':
    ip = ip[1:]
if ip[-1] == '':
    ip = ip[:-1]

result = ''
for i in ip:
    if i == '':
        result += '0000'  * (8 - len(ip) + 1)
    else:
        result += i.zfill(4) + ':'

print(result[:-1])