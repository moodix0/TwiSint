import tweepy
import pandas as pd

print(" \n    TwiSint  \n Twitter: @moodix0 \n Github: @moodix94 \n")

print("\n *** \n Before start using script, you have to insert your own credentials! \n *** ")

# Examples for API:
# use your own credentials:

consumer_key = "1234ABCD"
consumer_secret = "1234ABCD"
access_token = "1234ABCD"
access_secret = "1234ABCD"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

number_of_tweets = int(input("\n Enter number of tweets: "))
tweets = []
likes = []
times = []

user = input("\n Enter Username: ")
print("\n Please wait ...")
for i in tweepy.Cursor(api.user_timeline, user_id=user, tweet_mode='extended').items(number_of_tweets):
    likes.append(i.favorite_count)
    tweets.append(i.full_text)
    times.append(i.created_at)
df = pd.DataFrame({"Tweets": tweets, "Likes": likes, "Times": times})

# following line, you can comment on it if you don't want the retweets:

df = df[~df['Tweets'].str.contains('RT')]
df = df.reset_index(drop=True)
print(df)
mostliked = df.loc[df['Likes'].idxmax()]
print(mostliked)
df.to_csv("TwiSint.csv")

print("\nDone\nit's saved: 'TwiSint.csv' \n ")
