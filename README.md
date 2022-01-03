# Spotify Wrapped
Every year when I recieve my Spotify Wrapped, I feel like there's some injustice between some of the data. For example, there are two artists I listened to a lot in 2020. Both artists had around 3000 streams. The key difference was that one of the artists had songs that averaged 10-12 minutes, while the other artist was averaging around 3-4 minutes per song. I thought of this to be dumb, and wanted a way to find out the actual time-based weighting of each artist.

This tool will use a python script to scrape the song history of Spotify data. You can get this via [Spotify's Privacy Settings](https://www.spotify.com/us/account/privacy/), but it will require a few days to process and get it emailed to you.

# Usage

After getting your data from [Spotify's Privacy Settings](https://www.spotify.com/us/account/privacy/), you must choose the correct script to use. Both scripts are used by downloading the Python file and running it in the folder with all the data.
If you have your Spotify Data from the past 12 months, use [spotifywrapped.py](https://github.com/Antichess/spotifywrapped/blob/main/spotifywrapped.py). If you have your full spotify data, also known as your **extended streaming history**, then use [full_history.py](https://github.com/Antichess/spotifywrapped/blob/main/full_history.py). Run place the script in the folder and run, it will generate text files.
