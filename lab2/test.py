f1 = lambda x, y, z, k: (5.679 - 1.44 * x + 2.112 * y - 0.413 * z) / 5.934
f2 = lambda x, y, z, k: (12.031 - 0.311 * x + 3.541 * y - 0.709 * k) / 14.241
f3 = lambda x, y, z, k: (8.578 - 0.341 * x + 1.647 * z - 0.342 * k) / 9.542
f4 = lambda x, y, z, k: (3.104 + 0.515 * y - 0.321 * z + 0.321 * k) / 3.141

x0 = 0
y0 = 0
z0 = 0
k0 = 0
count = 1
e = float(input('Enter tolerable error: '))

print('\nCount\tk\tz\ty\tx\n')
condition = True
while condition:    
    k1 = f1(x0, y0, z0, k0)
    z1 = f2(x0, y0, z0, k1)    
    y1 = f3(x0, y0, z1, k1)
    x1 = f4(x0, y1, z1, k1)    
    e1 = abs(k0 - k1)
    e2 = abs(z0 - z1)    
    e3 = abs(y0 - y1)
    e4 = abs(x0 - x1)
    print(f'{count}\t{k1:.4f}\t{z1:.4f}\t{y1:.4f}\t{x1:.4f}')
    count += 1    
    k0 = k1
    z0 = z1    
    y0 = y1
    x0 = x1    
    condition = e1 > e and e2 > e and e3 > e and e4 > e
print('\nFinal values:')
print(f'k = {k1:.4f}, z = {z1:.4f}, y = {y1:.4f}, x = {x1:.4f}')
