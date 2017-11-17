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

class SearchResource(object):

    def on_get(self, req, res):

        rv = self._searchTweets(urllib.parse.urlencode(req.params))
        res.media = rv

    def _searchTweets(self, search_options):
        temp = api.GetSearch(raw_query=search_options)

        results = []
        for t in temp:
            dict_status = {
                'id': t.id,
                'user': t.user.screen_name,
                'text': t.text,
                'created_at': t.created_at
            }
            results.append(dict_status)

        return "{" + json.dumps(results) + "}"

class UserTimelineResource(object):

    def on_post(self, req, res):

        print(req.context)
#        req.context.user
        res.media = req.context
 #       res.media = self._getUserTimeline()

    def _getUserTimeline(user):
        return api.GetUserTimeline(user)