import falcon
import api_twitter

app = falcon.API()
app.add_route("/search", api_twitter.SearchResource())

if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8008, app)
    httpd.serve_forever()
