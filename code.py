import subprocess
#import yaml
import hashlib
#import flask


def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=file)
    subprocess.call(command, shell=True)


def load_config(filename):
    # Load a configuration file into YAML
    stream = file.open(filename, "w")
    config = yaml.load(stream)


def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


def fetch_website(urllib_version, url):
    # Import the requested version of urllib
    exec(f"import urllib{urllib_version} as urllib", globals())
    # Fetch and print the requested URL
    http = urllib.PoolManager()
    url_data = http.request('GET', url)
    return url_data.data

#@app.route("/")
#def index():
#    version = flask.request.args.get("urllib_version")
#    url = flask.request.args.get("url")
#    return fetch_website(version, url)

fetch_website(1.17, "https://www.google.com/search?q=urllib+version&rlz=1C1GCEB_enCZ994CZ997&oq=urllib+version&aqs=chrome..69i57j0i19l2j0i19i22i30l7.5560j0j4&sourceid=chrome&ie=UTF-8")
