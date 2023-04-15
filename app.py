from flask import Flask, render_template

from feed import get_links_from_feed
from preview import preview_link

app = Flask(__name__)


@app.route('/')
def preview():
    rss_feed_name = "Responsible AI"
    rss_url = "https://www.google.com/alerts/feeds/14189963098849591986/9255876189418000805"

    header = render_template("header.html", **{"rss_feed_name": rss_feed_name})
    html_segments = [header]

    links = get_links_from_feed(rss_url)
    for link in links:
        preview_html = preview_link(link)
        html_segments.append(preview_html)
    return "".join(html_segments)

if __name__ == '__main__':
    app.run(debug=True)