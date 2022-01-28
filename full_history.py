import json
import datetime
import os

numberOfFiles = 0

directory = os.getcwd()
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.startswith("endsong_"):
         numberOfFiles = numberOfFiles + 1

d = {}
print(f"{numberOfFiles} files loaded")

for fileCount in range(numberOfFiles):
    name = "endsong_" + str(fileCount) + ".json"
    with open(name,encoding="utf8") as f:
        data = json.load(f)
        for c in data:
            if int(c["ms_played"]) > 29999:
                if c["master_metadata_album_artist_name"] not in d:
                    d[c["master_metadata_album_artist_name"]] = {}
                    d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]] = {}
                    d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]]["ms_played"] = int(c["ms_played"])
                    d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]]["plays"] = 1
                else:
                    if c["master_metadata_track_name"] in d[c["master_metadata_album_artist_name"]]:
                        d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]]["ms_played"] = d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]]["ms_played"] + int(c["ms_played"])
                        d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]]["plays"] = d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]]["plays"] + 1
                    else:
                        d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]] = {}
                        d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]]["ms_played"] = int(c["ms_played"])
                        d[c["master_metadata_album_artist_name"]][c["master_metadata_track_name"]]["plays"] = 1
    print(f"endsong_{fileCount}.json")

#print(json.dumps(d, sort_keys=False, indent=4))


a = []
artists = []
totalms = 0
totalstreams = 0
for i in d:
    for j in d[i]:
        app = i,j,d[i][j]["ms_played"],d[i][j]["plays"]
        totalms = totalms + d[i][j]["ms_played"]
        totalstreams = totalstreams + d[i][j]["plays"]
        a.append(app)
        
a.sort(key=lambda x:x[2], reverse=True)

for i in d:
    s = 0
    p = 0
    for j in d[i]:
        s = s + d[i][j]["ms_played"]
        p = p + d[i][j]["plays"]
    app = i,s,p
    artists.append(app)

artists.sort(key=lambda x:x[1], reverse=True)

with open("500topartists.txt", "w") as f:
    f.write("# | Artist | Hours listened to | Streams\n")
    f.write(":-|:-|:-|:-\n")
    for x in range(len(artists)):
        try:
            f.write(f"{x+1} | {artists[x][0]} | {round(artists[x][1]/3600000,2)} | {artists[x][2]}\n")
        except:
            pass

with open("500topsongs.txt", "w") as f:
    f.write("# | Artist | Song name | Hours listened to | Streams | Avg\n")
    f.write(":-|:-|:-|:-|:-|:-\n")
    for x in range(len(a)):
        try:
            f.write(f"{x+1} | {a[x][0]} | {a[x][1]} | {round(a[x][2]/3600000,2)} | {a[x][3]} | {datetime.datetime.fromtimestamp(a[x][2]/a[x][3]/1000.0).strftime('%M:%S')}\n")
        except:
            pass
    print(f"Total hours played is {round(totalms/3600000,2)}")
    print(f"Total days played is {round(totalms/3600000/24,2)}")
    print(f"Total streams over 30 seconds is {totalstreams}")
