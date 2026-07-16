s1 = input("Enter a string: ")
freq = {}
for ch in s1:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)
