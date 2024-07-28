import sys
sys.path.append('/home/ec2-user/.local/lib/python3.11/site-packages')

import snscrape.modules.twitter as sntwitter

import csv

def scrape_tweets(usernames, limit=100):
    all_tweets = []
    for username in usernames:
        for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
            if i >= limit:
                break
            all_tweets.append({
                "username": username,
                "date": tweet.date,
                "content": tweet.content,
                "retweets": tweet.retweetCount,
                "likes": tweet.likeCount,
                "replies": tweet.replyCount,
                "hashtags": [hashtag.lower() for hashtag in tweet.hashtags] if tweet.hashtags else [],
                "link": f"https://twitter.com/{username}/status/{tweet.id}"
            })
    return all_tweets

def export_to_csv(tweets, filename='tweets.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "date", "content", "retweets", "likes", "replies", "hashtags", "link"])
        writer.writeheader()
        for tweet in tweets:
            writer.writerow(tweet)

if __name__ == "__main__":
    usernames = [
        "WatcherGuru", "VitalikButerin", "rovercrc", "_RichardTeng", "justinsuntron", "BitcoinMagazine",
        "Cointelegraph", "CryptoCapo_", "TheCryptoLark", "binance", "zerohedge", "saylor", "lookonchain",
        "ElonMuskAOC", "greg16676935420", "MrBeast", "BillyM2k", "tier10k", "coinmarketcap", "100trillionUSD",
        "MMCrypto", "BTC_Archive", "cz_binance"
    ]
    tweets = scrape_tweets(usernames)
    export_to_csv(tweets)
