import falcon
import api_twitter

app = falcon.API()
app.add_route("/statuses/home_timeline", api_twitter.HomeTimelineResource())
app.add_route("/statuses/user_timeline/{screen_name}", api_twitter.UserTimelineResource())
app.add_route("/search", api_twitter.SearchResource())
app.add_route("/status/{id}", api_twitter.StatusResource())

if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8008, app)
    httpd.serve_forever()
