strings = ["level", "hi", "aba", "1991", "python", "noon", "cat", "a"]
count = 0
for s in strings:
    if len(s) > 2 and s == s[::-1]:
        count += 1
print("Number of palindromic strings (length > 2):", count)
