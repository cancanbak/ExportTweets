import twint

usernames = [
    "WatcherGuru", "VitalikButerin", "rovercrc", "_RichardTeng", "justinsuntron", "BitcoinMagazine",
    "Cointelegraph", "CryptoCapo_", "TheCryptoLark", "binance", "zerohedge", "saylor", "lookonchain",
    "ElonMuskAOC", "greg16676935420", "MrBeast", "BillyM2k", "tier10k", "coinmarketcap", "100trillionUSD",
    "MMCrypto", "BTC_Archive", "cz_binance"
]

for username in usernames:
    try:
        c = twint.Config()
        c.Username = username
        c.Limit = 100
        c.Store_csv = True
        c.Output = "tweets.csv"
        c.Custom["tweet"] = ["date", "tweet", "username", "id", "link", "retweets", "likes", "replies", "hashtags"]
        c.Resume = "tweets.csv"
        
        print(f"Fetching tweets for {username}")
        twint.run.Search(c)
        
    except Exception as e:
        print(f"Error fetching tweets for {username}: {e}")
