import time
x = time.time()

def fibi(y):
    if y <= 0:
        return 0
    elif y == 1:
        return 1
    else:
         return fibi(y- 1) + fibi(y - 2)

print(f'f(35) = {fibi(35)}')
print(f'runtime {time.time() - x}')