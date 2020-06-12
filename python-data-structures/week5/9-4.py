name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
words = list()
dic = dict()
for line in handle:
    # skips lines that do not start with 'From '
    if not line.startswith('From '):
        continue
    # stores the email into list words 
    words.append(line.split()[1])
for email in words:
    # tally of emails
    dic[email] = dic.get(email, 0) + 1
# finding largest value and corresponding key in dic
largestk = None
largestv = None
for k,v in dic.items():
    if largestv is None or v > largestv:
        largestv = v
        largestk = k
print(largestk, largestv)