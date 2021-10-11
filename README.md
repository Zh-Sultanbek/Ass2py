Title: Scrapping news about difference cryptocurrency from coinmarketcap.com

Usage/Example:
from coinmarketcap_scrapper import coinmarketcap

scrapper = coinmarketcap.Scrapper()
news = scrapper.get_news_of_cryptocurrency(cryptocurrency_name="bitcoin", count_of_news=20)

for i, new in enumerate(news, start=1):
	print(f"{i}. {new['title']}.\nSource: {new['source']}. Published: {new['published_time']}. Cryptocurrency: {new['cryptocurrency']}.\nReference: {new['url']}\n\n")	

OUTPUT:
1. BTC price hits $57K five-month high — 5 things to watch in BTC this week.
Source: Cointelegraph.com News. Published: 2 hours ago. Cryptocurrency: Bitcoin.
Reference: https://cointelegraph.com/news/btc-price-hits-57k-five-month-high-5-things-to-watch-in-btc-this-week


2. Bitcoin ($BTC) To $60K? Whales Accumulation Continues Amid New 5-Month High.
Source: Coingape. Published: 4 hours ago. Cryptocurrency: Bitcoin.
Reference: /headlines/news/bitcoin-btc-to-60k-whales-accumulation-continues-amid-new-5-month-high/


3. Bitcoin Price Prediction: BTC Continues Explosion To $60,000 Amid A Whale Buying Spree.
Source: Coingape. Published: 5 hours ago. Cryptocurrency: Bitcoin.
Reference: /headlines/news/Bitcoin-Price-Prediction:-BTC-Continues-Explosion-To-$60,000-Amid-A-Whale-Buying-Spree/


4. Does Bitcoin mining ‘just literally force us’ to be energy efficient.
Source: AMBCrypto. Published: 12 hours ago. Cryptocurrency: Bitcoin.
Reference: https://ambcrypto.com/does-bitcoin-mining-just-literally-force-us-to-be-energy-efficient/


5. Bitcoin Long Term Holder Supply Shock Hits New High, Signaling New Trajectory For BTC Bulls.
Source: ZyCrypto. Published: 14 hours ago. Cryptocurrency: Bitcoin.
Reference: https://zycrypto.com/bitcoin-long-term-holder-supply-shock-hits-new-high-signaling-new-trajectory-for-btc-bulls/
