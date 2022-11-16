twoString = "hello 1 050"
oneString = "1"
number = [str(w) for w in twoString.split() if w.isdigit()]
price = number[0] + number[1]
if int(price) > 2000:
    print(True)
# print(fullString)

strf = "TINGOРазмеры:"
l = len(strf)
remove = strf[:l-8]
print(remove)
datatest = 1

print(float(datatest) * 2)