import json
import datetime

def add_data(a,c,ms,s):
    found = False
    for x in range(len(a)):
        if c == a[x][0]:
            a[x] = (c, a[x][1] + ms, a[x][2] + s)
            found = True
            break
    if not found:
        append = (c, ms, s)
        a.append(append)

f = open("full.json",encoding="utf8") 
data = json.load(f)
f.close()

s = []
a = []
stream = 0
finalsum = 0
found = False

for x in data:
    found = False
    if int(x["msPlayed"]) > 30000:
        finalsum = finalsum + x["msPlayed"]
        stream = 1
    else:
        stream = 0
        
    for c, i in enumerate(s):
        if x["trackName"] == i[1]:
            append = (i[0],i[1],i[2]+int(x["msPlayed"]),i[3]+stream)
            s[c] = append
            found = True
            break
    if found is False:
        append = x["artistName"],x["trackName"],int(x["msPlayed"]),stream
        s.append(append)
    

for x in s:
    add_data(a,x[0],x[2],x[3])


s.sort(key=lambda x:x[2], reverse=True)
print("Artist | Song name | Hours listened to | Streams | Avg")
print(":-|:-|:-|:-|:-")
for x in range(30):
    print(f"{s[x][0]} | {s[x][1]} | {round(s[x][2]/3600000,2)} | {s[x][3]} | {datetime.datetime.fromtimestamp(s[x][2]/s[x][3]/1000.0).strftime('%M:%S')}")

for x in range(5):
    print()

s.sort(key=lambda x:x[3], reverse=True)
print("Artist | Song name | Hours listened to | Streams | Avg")
print(":-|:-|:-|:-|:-")
for x in range(100):
    print(f"{x+1} {s[x][0]} | {s[x][1]} | {round(s[x][2]/3600000,2)} | {s[x][3]} | {datetime.datetime.fromtimestamp(s[x][2]/s[x][3]/1000.0).strftime('%M:%S')}")

for x in range(5):
    print()

a.sort(key=lambda x:x[1], reverse=True)
print("Artist | Hours listened to | Streams")
print(":-|:-|:-")
for x in range(30):
     print(f"{a[x][0]} | {round(a[x][1]/3600000,2)} | {a[x][2]}")

print(str(finalsum/60000))
