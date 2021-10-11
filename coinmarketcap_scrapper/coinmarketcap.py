from requests_html import HTMLSession
from bs4 import BeautifulSoup as BS
 
class Scrapper:
	def __init__(self):
		self.__url = "https://coinmarketcap.com/currencies/{cryptocurrency_name}/news/"

	def get_news_of_cryptocurrency(self, cryptocurrency_name, count_of_news):
		session = HTMLSession()
		resp = session.get(self.__url.format(cryptocurrency_name = cryptocurrency_name))
		resp.html.render()

		soup = BS(resp.html.html, "html.parser")
		 
		news = []
		for i, j in enumerate(soup.select(".svowul-5.czQlor")):
			title = j.select("h3")[0].get_text()
			source = j.select(".sc-1eb5slv-0.svowul-7.gYmsIK")[0].get_text()
			published_time = j.select(".sc-1eb5slv-0.hykWbK")[0].get_text()
			cryptocurrency = j.select(".sc-1eb5slv-0.hQRknF")[0].get_text()
			url = j.select("a")[0]['href']
			news.append({"title": title, "source": source, "published_time": published_time, "cryptocurrency": cryptocurrency, "url": url})
		return news
