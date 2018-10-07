print("   ", end="")

for i in range(10):
    print(f'{i:6}', end='')
print()
print()
for rzad in range(10):
    print(rzad, "  ", end='')
    for i in range(10):
        print(f'{i*rzad:6}', end='')
    print()
