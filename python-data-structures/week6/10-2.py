name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
times = list()
# rejects lines not starting with "From"
# adds time into list times
for line in handle:
    if not line.startswith('From '):
        continue
    times.append(line.split()[5])
# adds hour into list hours
hours = list()
for time in times:
    hours.append(time.split(':')[0])
# creates a dictionary dic and with hours as keys
dic = dict()
for hour in hours:
    dic[hour] = dic.get(hour, 0) + 1
# prints a sorted list of tuples containing key and value from dic
for k,v in sorted(dic.items()):
    print(k,v)
