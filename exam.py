def count_b_bob_patterns(text):
    count = 0
    i = 0
    while i < len(text) - 3:
        if text[i].lower() == 'b' and text[i+1:].find("Bob") != -1:
            end_index = i + text[i+1:].find("Bob") + 3
            if text[i:end_index].endswith("Bob"):
                count += 1
                i = end_index - 3  # Adjust to continue search correctly
            else:
                i += 1
        else:
            i += 1
    return count

# Adjusted example call
text = "bkdsjfsBob goes to school. Bobbobob bokokkvkbob. I am friends with bbbdoiob. Such a bob guy Bob is."
count_b_bob_patterns(text)
print(count_b_bob_patterns)