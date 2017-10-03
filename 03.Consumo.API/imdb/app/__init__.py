from tweepy import Stream, OAuthHandler, API, Cursor
from tweepy.streaming import StreamListener

cke = "S4IYPnnEScDG2USwBVke3MCdZ"
cse = "FVJbpmKAhFO8jVWiOoRl1gt5tDCeyy0RTkZheAmHT7lVm7tfj2"
ato = "137520613-tyW9Ecq8P2Q8mmk2OFS41re1nDKbkDNn8JCJT4R9"
ase = "MZPl8APzi746wnob4lP0FZefFnOB0mtcH0sAHOWZKHbB5"

auth = OAuthHandler(cke, cse)
auth.set_access_token(ato, ase)

# api = API(auth)
#
# for tuit in Cursor(api.home_timeline).items(10):
#     print(tuit.text)
#
# for seguidor in Cursor(api.friends).items():
#     print(seguidor._json)
#
# for tuit in Cursor(api.user_timeline).items(2):
#     print(tuit.text)

class TLListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)

twStream = Stream(auth, TLListener())
twStream.filter(track=["#uip"])