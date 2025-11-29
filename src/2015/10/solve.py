#!/usr/local/bin/python3

def next_seq(input):
    counter = 1
    current_ch = ''
    ns = ""
    for i in range(len(input) - 1):
        current_ch = input[i]
        if current_ch == input[i+1]:
            counter += 1
        else:
            ns += f"{counter}{current_ch}"
            counter = 1

    current_ch = input[-1:]
    ns += f"{counter}{current_ch}"
    return ns

value = "1321131112"
for i in range(40):
    value = next_seq(value)

print(f"value length, 40 iterations {len(value)}")

for i in range(10):
    value = next_seq(value)

print(f"value length, 50 iterations {len(value)}")
