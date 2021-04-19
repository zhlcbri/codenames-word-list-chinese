import glob

# merge all files into one file
files = glob.glob("../categories/*.txt")
with open("../word_list.txt", "wb") as out_file:
    for file in files:
        with open(file, "rb") as in_file:
            out_file.write(in_file.read())
