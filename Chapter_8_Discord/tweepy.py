import tweepy

#roberto_bot

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ibasVAM1m0IU9dhImNBUvLVMe","ZapBFOgTPp0VDSoZ0yOfiCpLpp09GBxtmFeZKR3bFiHNc0qDap")
auth.set_access_token("797892297526562816-xN7RWwSxdsZXyLKynm4qaxtbImddI2E","WgJbQAmqCnGqBeaYX6gsp0YPt1speLEFA59fhOxznlTWs")
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

#--------------------------
#Methods for tweets
api.update_status("Hi Tweepy")

#--------------------------
#Methods for users
user = api.get_user("ptizei")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

#to get all friends from an user
api.friends("dermitmaria")

#--------------------------
#Methods for followers
#This code shows how you can use Tweepy to start following @realpython:
api.create_friendship("mbeisen")
api.destroy_friendship("mbeisen")


#--------------------------
#Methods for Your Account
api.update_profile(description="I like Python")

#--------------------------
#Methods for Likes
#You can mark the most recent tweet in your home timeline as Liked as follows:

tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

#--------------------------
#Methods for Blocking Users
#to list  accounts that you have blocked.
for block in api.blocks():
    print(block.name)



#--------------------------
#Methods for Streaming
#to actively search for tweets
import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
    
    def on_error(self, status):
        print("Error detected")

# This class is used for the stream listener tweets_listener. By extending Tweepy’s StreamLister, we reused code that is common to all stream listeners. Tweets from the stream are processed by on_status().
# We created the stream using tweepy.Stream, passing the authentication credentials and our stream listener. To start getting tweets from the stream, you have to call the stream’s filter(), passin
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["python"], languages=["en"])






