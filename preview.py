import newspaper
from flask import render_template
from typing import Dict

def get_newspaper_article(link: str) -> newspaper.article.Article:
    article = newspaper.Article(url="%s" % (link), language='en')
    try:
        article.download()
        article.parse()
        return article 
    except Exception as e:
        raise e

def get_metadata(article: newspaper.article.Article) -> Dict:
    if not article.is_parsed:
        raise TypeError("Article must be parsed.")
    
    title = article.title
    image = article.top_img
    url = article.url
    try:
        description = article.meta_data['description']
    except KeyError:
       description = ""

    return {"title": title, "description": description, "image": image, "url":url}

def preview_link(link: str) -> str:
    try:
        article = get_newspaper_article(link)
        link_metadata = get_metadata(article)
        html = render_template('preview.html', **link_metadata)
        return html 
    except:
       return ""