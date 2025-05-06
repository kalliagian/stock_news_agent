from transformers import pipeline # plus torch
import pandas as pd
import json

class NewsSummarizationAgent:
    def __init__(self, model_name="Kallia/t5-small-finetuned-stock-news", dataset_path="news_dataset/2020_processed.json"):
        self.summarizer = pipeline("summarization", model=model_name)
        with open(dataset_path, "r", encoding="utf-8") as f:
            self.dataset = json.load(f)  # Simulated "news API"
        self.indexed_articles = {}
        for article in self.dataset:
            for company in article.get("mentioned_companies", []):
                if company in self.indexed_articles:
                    self.indexed_articles[company].append(article)
                else:
                    self.indexed_articles[company] = [article]
        

    def fetch_articles(self, portfolio):
        if type(portfolio) != list:
            portfolio = [portfolio]
        articles = []
        for company in portfolio:
            articles += self.indexed_articles[company][:5]
        return articles

    def summarize_articles(self, articles, text_key="maintext"):
        results = {"Assets": [], "News Summaries": [], 'Articles': []}
        for article in articles:
            text = article.get(text_key, "")
            if text:
                summary = self.summarizer(text[:1000], max_length=100, min_length=30, do_sample=False, truncation=True)[0]['summary_text']
                companies = ", ".join(article.get("mentioned_companies", []))
                results['Assets'].append(companies)
                results['News Summaries'].append(summary)
                results['Articles'].append(text)
        return pd.DataFrame(results)
    
