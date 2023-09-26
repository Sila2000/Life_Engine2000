#Transcription

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
print("\r\r")

print("Choose STRAND 1 as Template Strand: ")
checker1 = int(input("0/1: "))
print("Or, Choose STRAND 2 as Template Strand: ")
checker2 = int(input("0/1: "))
print("\r\r")

print("After Transcription:")
if checker1 == 1 and checker2 == 0:
    for i in range(seq_len + 2):
        # Take in_pair_nucleotide2 as coding strand and replace T with U
        if in_pair_nucleotide2[i] == "T":
            in_pair_nucleotide2.remove("T")
            in_pair_nucleotide2.insert(i, "U")
    print("RNA")
    print(in_pair_nucleotide2)

elif checker1 == 0 and checker2 == 1:
    for i in range(seq_len + 2):
        # Take in_pair_nucleotide1 as coding strand and replace T with U
        if in_pair_nucleotide1[i] == "T":
            in_pair_nucleotide1.remove("T")
            in_pair_nucleotide1.insert(i, "U")
    print("RNA")
    print(in_pair_nucleotide1)
