#building DNA portion from a given strand

in_pair_nucleotide1 = []
in_pair_nucleotide2 = []
base_pair = {"A": "T", "T": "A", "G": "C", "C": "G"}

seq_len = int(input("Enter the number of base pairs: "))

for i in range(seq_len):
    nucleotide1 = input()
    in_pair_nucleotide1.append(nucleotide1)
    in_pair_nucleotide2.append(base_pair[nucleotide1])

in_pair_nucleotide1.insert(0, "3'")
in_pair_nucleotide1.insert(seq_len+1, "5'")
in_pair_nucleotide2.insert(0, "5'")
in_pair_nucleotide2.insert(seq_len+1, "3'")

print("DNA")
print("STRAND 1: ", in_pair_nucleotide1)
print("STRAND 2: ", in_pair_nucleotide2)
