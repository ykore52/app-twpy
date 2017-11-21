import os
import twitter
import json
import urllib.parse

api = twitter.Api(
    consumer_key = os.environ['ConsumerKey'],
    consumer_secret = os.environ['ConsumerSecret'],
    access_token_key = os.environ['AccessTokenKey'],
    access_token_secret = os.environ['AccessTokenSecret']
)

try:
    api.VerifyCredentials()
except:
    raise Exception("Twitter Account Authentication Failed.")

class HomeTimelineResource(object):
    
    def on_get(self, req, res):
        res.media = self._getHomeTimeline()
        res.content_type = 'application/json'

    def _getHomeTimeline(self):
        rv = []
        for status in api.GetHomeTimeline():
            rv.append(str(status))
        return '{"tweets":[' + ','.join(rv) + "]}"

class UserTimelineResource(object):
    
    def on_get(self, req, res, screen_name):
        res.media = str(self._getUserTimeline(screen_name = screen_name))
        res.content_type = 'application/json'

    def _getUserTimeline(self, screen_name):
        rv = []
        for status in api.GetUserTimeline(screen_name = screen_name):
            rv.append(str(status))
        return '{"tweets":[' + ','.join(rv) + "]}"

class SearchResource(object):

    def on_get(self, req, res):
        res.media = self._searchTweets(urllib.parse.urlencode(req.params))
        res.content_type = 'application/json'

    def _searchTweets(self, search_options):
        rv = []
        for t in api.GetSearch(raw_query=search_options):
            rv.append(str(t))
        return '{"tweets":[' + ','.join(rv) + "]}"

class StatusResource(object):
    
    def on_get(self, req, res, id):
        res.media = self._getStatus(id)
        res.content_type = 'application/json'

    def _getStatus(self, id):
        return str(api.GetStatus(status_id=id))