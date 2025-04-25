# 4: reverse string
def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1): # loop from the end to the beginning
        reversed_str += s[i]
    return reversed_str

# test
text = "python"
print(f"Original: {text}")
print(f"Reversed: {reverse_string(text)}")
