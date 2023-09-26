#Cell Reproduction

gen = int(input("Enter the number of generations: "))

for i in range(1, gen+1):
    print(f"G[{i-1}]:")
    for j in range(pow(2,i-1)):
        print("O\t", end="")
    print(f"\nNumber of cells in G[{i-1}]: ", pow(2, i-1))
    print("\r")
