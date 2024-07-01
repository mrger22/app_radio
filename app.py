# https://github.com/mrger22/app_radio

from flask import Flask, render_template, request, redirect, url_for
import vlc

app = Flask(__name__)

radio_stations = [{"name": "Radio 1", "url": "https://ep128.hostingradio.ru:8030/ep128"},
                  {"name": "Radio 2", "url": "https://pub0301.101.ru:8443/stream/air/mp3/256/200"}]

@app.route('/')
def index():
    return render_template('index.html', radio_stations=radio_stations)

@app.route('/add_radio', methods=['GET', 'POST'])
def add_radio():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        radio_stations.append({"name": name, "url": url})
        return redirect(url_for('index'))
    return render_template('add_radio.html')

@app.route('/radio2')
def radio2():
    return render_template('radio2.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
