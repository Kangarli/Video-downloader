from flask import Flask, render_template, request
from pytube import YouTube
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ytb')
def download():
    url = request.args.get('url')
    if url:
        yt = YouTube(url)
        video = {
            "info": {
                "title": yt.title,
                "author": yt.author,
                "thumbnail": yt.thumbnail_url,
                "description": yt.description,
            },
            "sources": []
        }

        videos = yt.streams.filter(progressive=True)
        for v in videos:
            video['sources'].append({
                "url": v.url,
                "resolution": v.resolution,
            })
    return video

# yt = YouTube('https://www.youtube.com/watch?v=maoWldOBDj8')

# print(yt.streams)