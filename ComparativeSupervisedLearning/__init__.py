from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import Main
from ComparativeSupervisedLearning.Data.Dto.In.BaseData import BaseData
from ComparativeSupervisedLearning.Data.Dto.In.FullData import FullData
from Config.LogConfig import mainLogger as Log

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('/error.html', error='Page Not Found 404'), 404


@app.errorhandler(400)
def page_not_found(error):
    return render_template('/error.html', error='Bad Request 400'), 400


@app.route("/", methods=['POST', 'GET'])
def main():
    return render_template("/index.html")


@app.route("/form", methods=['POST', 'GET'])
def fill_in():
    return render_template("/form.html")


@app.route("/algorithm", methods=['POST', 'GET'])
def algorithm():
    return render_template("/algorithm.html", model='ALL')


@app.route("/algorithmKNN", methods=['POST', 'GET'])
def algorithm_knn():
    return render_template("/algorithm.html", model='KNN')


@app.route("/algorithmSVM", methods=['POST', 'GET'])
def algorithm_svm():
    return render_template("/algorithm.html", model='SVM')


@app.route("/algorithmRF", methods=['POST', 'GET'])
def algorithm_rf():
    return render_template("/algorithm.html", model='RF')


@app.route("/statistic", methods=['POST', 'GET'])
def statistic():
    return render_template("/statistic.html")


@app.route('/submit_action', methods=['GET'])
def submit_action():
    filled_form = request.args
    Log.debug(filled_form)
    Log.debug("Processing ...")
    result = Main.predict_based_on_user_input(BaseData(filled_form), FullData(filled_form))
    Log.info(result)
    return result


@app.route('/get_data_elaboration', methods=['GET'])
def get_data_elaboration():
    result = Main.render_data_info()
    Log.info(result)
    return result


@app.route('/jsonDataSend', methods=['POST'])
def json_data_send():
    data = request.get_json()
    name = data['name']
    return jsonify({'name': name})


if __name__ == '__main__':
    Bootstrap(app)
    Log.info("Start Flask application")
    app.run(debug=True, host="0.0.0.0", port=80)
