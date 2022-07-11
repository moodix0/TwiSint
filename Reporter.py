import tweepy as tw

print("     Reporter  \n Twitter: @moodix0 \n Github: @moodix94 \n")

print(" ***  \n Before running this script! \n You Have to insert your 'API' credentials to use this tool.  \n *** ")

# Examples for API:
# use your own credentials:
consumer_key = "1234ABCD"
consumer_secret = "1234ABCD"
access_token = "1234ABCD"
access_secret = "1234ABCD"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tw.API(auth)

screen_name = input("\n # Enter Username: ")
print('\n * Wait Please..!')
perform_block = True

# you can adjust the "range" of reporting:
for i in range(1, 500):
    if perform_block:
        try:
            api.create_block(screen_name=screen_name)
            perform_block = True
        except tw.error.TweepError:
            perform_block = True
    else:
        break
print('\n # Done .. Bye ! \n')
