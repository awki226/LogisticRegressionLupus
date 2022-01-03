import praw 
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
flair = []
score = []
post = []
for submission in reddit.subreddit("lupus").new(limit=9000):
    text = ""
    if(len(submission.selftext) > 300):
        flair.append(submission.link_flair_text)
        score.append(submission.score)
        text = submission.title + " " + submission.selftext 
        post.append(text)

df = pd.DataFrame({'score': score, 'post': post, 'flair': flair })
df.to_csv('PRAWtest3.csv')
print(df)
    
