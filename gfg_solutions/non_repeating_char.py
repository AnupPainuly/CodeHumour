A = input()
char_counts = {}
result = ""
for char in A:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
for char in char_counts.keys():
    if char_counts[char] == 1:
        result += char
    elif char_counts[char] > 1:
        result += char+"#"+char*(char_counts[char] - 2)
print(result)
