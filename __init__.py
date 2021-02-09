from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

from DataManagement.dto.BaseData import BaseData
from DataManagement.dto.FullData import FullData
import Main

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('/error.html', error='Page Not Found 404'), 404


@app.errorhandler(400)
def page_not_found(error):
    return render_template('/error.html', error='Bad Request 400'), 400


@app.route("/", methods=['POST', 'GET'])
def main():
    # return render_template("/form.html")
    return render_template("/index.html")


@app.route("/form", methods=['POST', 'GET'])
def fill_in():
    return render_template("/form.html")


@app.route("/algorithm", methods=['POST', 'GET'])
def algorithm():
    return render_template("/algorithm.html", model='ALL')


@app.route("/algorithmKNN", methods=['POST', 'GET'])
def algorithm():
    return render_template("/algorithm.html", model='KNN')


@app.route("/algorithmSVM", methods=['POST', 'GET'])
def algorithm():
    return render_template("/algorithm.html", model='SVM')


@app.route("/algorithmRF", methods=['POST', 'GET'])
def algorithm():
    return render_template("/algorithm.html", model='RF')


@app.route("/statistic", methods=['POST', 'GET'])
def statistic():
    return render_template("/statistic.html")


@app.route('/submit_action', methods=['GET'])
def submitAction():
    filled_form = request.args
    print(filled_form)
    base_json = BaseData(filled_form)
    full_json = FullData(filled_form)
    result = Main.predictBasedOnUserInput(base_json, full_json)
    # return render_template("/answerPage.html", answer=filledForm)
    # render_template("/answerPage.html", answer=filledForm)
    print(result)
    return "55"


@app.route('/jsonDataSend', methods=['POST'])
def jsonDataSend():
    data = request.get_json()
    name = data['name']
    return jsonify({'name': name})
    # return jsonify({'error': name})


if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True, host="0.0.0.0", port=80)
