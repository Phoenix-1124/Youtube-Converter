import os
import shutil
from flask import Flask, render_template, request
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/result', methods=['POST'])
def convert():
    if request.method == 'POST':
        video_url = request.form['video_link']
        video_info = YoutubeDL().extract_info(url=video_url, download=False)
        filename = f"{video_info['title']}​.mp3"
        option = {'format' : 'bestaudio/best', 'keepvideo' : False, 'outtmpl' : filename}
        with YoutubeDL(option) as ytaudio:
            ytaudio.download([video_info['webpage_url']])
    
    path = '/storage/emulated/0/youtube_converter_downloads'
    if os.path.isdir(path) == False:
        os.makedirs(path)
        
    dest = f"{path}/{filename}"
    shutil.move(filename, dest)
        
    
    return render_template('result.html', file_name = filename)
    
if __name__ == '__main__':
    app.run(debug=True)