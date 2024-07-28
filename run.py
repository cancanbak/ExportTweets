import asyncio
import csv
from twscrape import API, gather

async def fetch_tweets(username):
    api = API()
    user = await api.user_by_login(username)
    tweets = await gather(api.user_tweets(user.id, limit=100))
    return tweets

async def main(usernames):
    all_tweets = []
    for username in usernames:
        tweets = await fetch_tweets(username)
        for tweet in tweets:
            all_tweets.append({
                "username": username,
                "date": tweet.date,
                "content": tweet.content,
                "retweets": tweet.retweets,
                "likes": tweet.likes,
                "replies": tweet.replies,
                "hashtags": tweet.hashtags,
                "link": f"https://twitter.com/{username}/status/{tweet.id}"
            })

    # CSV'ye yazma
    with open('tweets.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "date", "content", "retweets", "likes", "replies", "hashtags", "link"])
        writer.writeheader()
        for tweet in all_tweets:
            writer.writerow(tweet)

if __name__ == "__main__":
    usernames = [
        "WatcherGuru", "VitalikButerin", "rovercrc", "_RichardTeng", "justinsuntron", "BitcoinMagazine",
        "Cointelegraph", "CryptoCapo_", "TheCryptoLark", "binance", "zerohedge", "saylor", "lookonchain",
        "ElonMuskAOC", "greg16676935420", "MrBeast", "BillyM2k", "tier10k", "coinmarketcap", "100trillionUSD",
        "MMCrypto", "BTC_Archive", "cz_binance"
    ]
    asyncio.run(main(usernames))
