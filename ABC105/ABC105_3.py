N = int(input())
result = ''
if N == 0:
    result = '0'
else:    
    while N != 0:
        if N % 2 == 1 :
            result = '1' + result
            N -= 1
        else:
            result = '0' + result
        N = -N//2

print(result)    
