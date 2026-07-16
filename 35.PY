s1 = "How much wood would a woodchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo his wife"
words = s1.split()
result = []
for w in words:
    if len(w) >= 4 and w[0] in ('w', 'W') and w not in result:
        result.append(w)
print(result)
