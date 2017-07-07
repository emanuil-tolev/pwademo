from flask import Flask, send_file, send_from_directory, abort
pwademo = Flask(__name__)

@pwademo.route("/")
@pwademo.route("/index.html")
def home():
    return send_file('index.html')

@pwademo.route("/service-worker.js")
def service_worker():
    return send_file('service-worker.js')

@pwademo.route("/manifest.json")
def manifest():
    return send_file('manifest.json')

@pwademo.route('/<static_dir>/<path:path>')
def send_scripts(static_dir, path):
    if static_dir not in ['images', 'scripts', 'styles']:
        abort(403)
    return send_from_directory(static_dir, path)

if __name__ == "__main__":
    pwademo.run()
