import requests
import tkinter as tk
import webbrowser

class NewsScraper:
    def __init__(self, master):
        self.api_key = "0dc26c31a2c6014df0d028227f2956d3"
        self.url = f"http://api.mediastack.com/v1/news?access_key={self.api_key}&countries=gb&limit=10"
        self.master = master

    def fetch_news(self):
        # fetch and store the news in json format
        response = requests.get(self.url)
        data = response.json()
        return data.get('data', [])

    def show_news(self):
        news = self.fetch_news()

        if news:
            # create a splash window for the news articles
            self.news_window = tk.Toplevel(self.master)
            self.news_window.geometry("640x480")
            self.news_window.protocol("WM_DELETE_WINDOW", self.close_news)

            for news_item in news:
                news_title = news_item['title']
                news_link = news_item['url']
                news_button = tk.Button(self.news_window, text=news_title,
                                        command=lambda url=news_link: self.open_link(url),
                                        width=100, anchor='w', font=("Arial", 15))
                news_button.pack()
        else:
            print("No news to display.")

    def open_link(self, url):
        # open the news in the default web-browser
        webbrowser.open(url)

    def close_news(self):
        # close the news window without harming the execution of the main program
        self.news_window.destroy()





