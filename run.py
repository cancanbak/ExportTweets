import twint

# Kullanıcı adlarını liste olarak tanımla
usernames = [
    "WatcherGuru", "VitalikButerin", "rovercrc", "_RichardTeng", "justinsuntron", "BitcoinMagazine",
    "Cointelegraph", "CryptoCapo_", "TheCryptoLark", "binance", "zerohedge", "saylor", "lookonchain",
    "ElonMuskAOC", "greg16676935420", "MrBeast", "BillyM2k", "tier10k", "coinmarketcap", "100trillionUSD",
    "MMCrypto", "BTC_Archive", "cz_binance"
]

# Her bir kullanıcı için Twint konfigürasyonunu çalıştır
for username in usernames:
    c = twint.Config()
    c.Username = username
    c.Limit = 100  # İstediğin tweet sayısını buraya yaz
    c.Store_csv = True
    c.Output = "tweets.csv"  # Çıktı dosyasının adı, aynı dosyaya eklemek için aynı adı kullan
    c.Custom["tweet"] = ["date", "tweet", "username", "id", "link", "retweets", "likes", "replies", "hashtags"]
    c.Resume = "tweets.csv"  # Kaldığı yerden devam etmesi için aynı dosya adı

    twint.run.Search(c)
