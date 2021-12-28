import json
import datetime

d = {}

for fileCount in range(6):
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
    print(fileCount)

#print(json.dumps(d, sort_keys=False, indent=4))


a = []
totalms = 0
totalstreams = 0
for i in d:
    for j in d[i]:
        app = i,j,d[i][j]["ms_played"],d[i][j]["plays"]
        totalms = totalms + d[i][j]["ms_played"]
        totalstreams = totalstreams + d[i][j]["plays"]
        a.append(app)
        
a.sort(key=lambda x:x[2], reverse=True)
with open("500written.txt", "w") as f:
    f.write("Artist | Song name | Hours listened to | Streams | Avg\n")
    f.write(":-|:-|:-|:-|:-\n")
    for x in range(500):
        f.write(f"{a[x][0]} | {a[x][1]} | {round(a[x][2]/3600000,2)} | {a[x][3]} | {datetime.datetime.fromtimestamp(a[x][2]/a[x][3]/1000.0).strftime('%M:%S')}\n")
    print(f"Total hours played is {round(totalms/3600000,2)}")
    print(f"Total streams is {totalstreams}")
