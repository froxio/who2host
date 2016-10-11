from __future__ import absolute_import
from celery import task
from streamer.models import Streamer
from twitchapp.settings import TWITCH_CLIENT_ID
import json
import urllib
import requests


@task(name='tasks.populate')
def populate():
    Streamer.objects.all().delete()
    games_req = requests.get('https://api.twitch.tv/kraken/games/top'
                             +
                             '?client_id=' + TWITCH_CLIENT_ID,
                             headers={'Accept':
                                      'application/vnd.twitchtv.v2+json'})
    for top_game in json.loads(games_req.text)['top']:
        game_req = requests.get('https://api.twitch.tv/kraken/streams?game='
                                + urllib.quote_plus(top_game['game']['name'])
                                +
                                '&limit=6&client_id=' + TWITCH_CLIENT_ID,
                                headers={'Accept':
                                         'application/vnd.twitchtv.v3+json'})
        game_streams = json.loads(game_req.text)['streams']
        for stream in game_streams:
            channel = stream['channel']
            Streamer.objects.create(
                streamer_name=channel['name'],
                streamer_views=channel['views'],
                streamer_follows=channel['followers'],
                streamer_avatar=channel['logo'],
                stream_game=stream['game'],
                stream_title=channel['status'],
                stream_language=channel['broadcaster_language'],
                stream_viewers=stream['viewers'],
                stream_thumbnail=stream['preview']['large'],
                stream_link=channel['url'],
            )
