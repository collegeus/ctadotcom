import os
from flask import Flask, render_template, send_from_directory

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/workflow")
def workflow():
    return render_template('workflow.html')

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return render_template('post.html', id=post_id)

@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

