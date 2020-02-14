from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        filledForm = request.form #to chce wysaś do serwera
        return redirect(url_for('index'))

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
