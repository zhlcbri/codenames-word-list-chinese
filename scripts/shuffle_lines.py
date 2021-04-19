import random

# shuffle all lines and write to a new file
with open("../word_list.txt") as original_file:
    lines = original_file.readlines()

random.shuffle(lines)

with open("../word_list_shuffled.txt", "w") as new_file:
    new_file.writelines(lines)
