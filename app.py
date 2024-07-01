from flask import Flask, render_template, request, redirect, url_for
import vlc

app = Flask(__name__)

radio_stations = [{"name": "Radio 1", "url": "http://stream.url1"},
                  {"name": "Radio 2", "url": "http://stream.url2"}]

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

if __name__ == '__main__':
    app.run(debug=True)