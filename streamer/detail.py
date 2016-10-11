import requests
import json
from twitchapp.settings import TWITCH_CLIENT_ID


def get_streamer_info(streamer_name):
    req = requests.get('https://api.twitch.tv/kraken/channels/'
                       + streamer_name
                       + '?client_id=' + TWITCH_CLIENT_ID,
                       headers={'Accept': 'application/vnd.twitchtv.v3+json'})
    streamer = json.loads(req.text)
    return {
        'streamer_name': streamer['name'],
        'streamer_views': streamer['views'],
        'streamer_follows': streamer['followers'],
        'streamer_avatar': streamer['logo'],
        'stream_link': streamer['url'],
    }
