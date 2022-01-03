import praw 
from psaw import PushshiftAPI
import datetime as dt
import pandas as pd

reddit = praw.Reddit(
    client_id = "NH6Q0tL3CPfO-QaVCwwuIw",
    client_secret = "zqB_GMzAgLTtAajHBbPAy24PUpq4fg",
    redirect_uri="http://localhost:8080",
    username = "CounterAdditional458",
    password="58je2.Wqqf~sm:B",
    user_agent="LupusScrapper by u/CounterAdditional458", 
)


#print(reddit.auth.url(["identity"], "...", "permanent"))
reddit.read_only = True

start_epoch=int(dt.datetime(2021, 4, 3).timestamp())
api = PushshiftAPI(reddit)

docs = api.search_submissions(before=start_epoch,
                            subreddit='lupus',
                            filter=['link_flair_text',
                            'selftext','score'],
                            user_removed = False,
                            mod_removed = False,
                            allow_images = False,
                            allow_videos = False,
                            allow_videogifs = False,
                            limit=1001)
thing = next(docs)

#df = pd.DataFrame([thing.d for thing in docs])

#df.to_csv('test.csv')
print(thing)

