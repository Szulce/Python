import base64
from io import BytesIO

import numpy
import seaborn as sns
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
# Generate the figure **without using pyplot**.
from matplotlib import pyplot as plt
from matplotlib.figure import Figure


# def plotx():
#     fig = Figure()
#     ax = fig.subplots()
#     ax.plot([1, 2])
#     return convert_plot_to_html(fig)


#
# def ploty(prediction_model):
#     # plot 30 examples of dependency between cv fold and AUC scores
#     fig, ax = plt.subplots()
#     sns.lineplot(
#         data=prediction_model.transpose().iloc[:30],
#         dashes=False,
#         palette="Set1",
#         marker="o",
#         alpha=0.5,
#         ax=ax,
#     )
#     ax.set_xlabel("CV test fold", size=12, labelpad=10)
#     ax.set_ylabel("Model AUC", size=12)
#     ax.tick_params(bottom=True, labelbottom=False)
#     plt.show()


def set_name_based_on_model_type(model_type):
    if model_type == Rs.MODEL_TYPE_KNN:
        return 'K najbliższych sąsiadów'
    elif model_type == Rs.MODEL_TYPE_SVM:
        return 'Maszyna wektorów nośnych'
    elif model_type == Rs.MODEL_TYPE_RF:
        return 'Lasy losowe'


def plot(model_type, prediction_model):
    estimators = prediction_model.cv_results_
    plot = sns.FacetGrid(estimators, row="score_achived", col="param", margin_titles=True)
    plot.map(plt.hist, "tip_pct", bins=numpy.linspace(0, 0.5, 1))
    plt.title(set_name_based_on_model_type(model_type))
    return convert_plot_to_html(plot)


def plot_knn(model_type, prediction_model, result):
    print("Training K-Nearest Neighbors")
    print(prediction_model.cv_results_)
    # plt.plot([i for i in range(1, )], knn)
    # for i in range(1, 21):
    #     plt.text(i, knn[i - 1], (i, round(knn[i - 1] * 100, 2)))
    # plt.xticks([i for i in range(1, 21)])
    # plt.xlabel('K')
    # plt.ylabel('Wynik')
    # plt.title(set_name_based_on_model_type(model_type))


# def plotSvm():
# svc = []
# activators = ['poly', 'sigmoid', 'linear', 'rbf']
# for i in range(len(activators)):
#     SVclassifier = SVC(kernel=activators[i])
#     SVclassifier.fit(X_train, Y_train)
#     svc.append(SVclassifier.score(X_test, Y_test))
# C:\Users\Raghav\Anaconda3\lib\site - packages\sklearn\svm\base.py: 196: FutureWarning: The
# default
# value
# of
# gamma
# will
# change
# from
# 'auto'
# to
# 'scale' in version
# 0.22
# to
# account
# better
# for unscaled features.Set gamma explicitly to 'auto' or 'scale' to avoid this warning.
# "avoid this warning.", FutureWarning)
# C:\Users\Raghav\Anaconda3\lib\site - packages\sklearn\svm\base.py: 196: FutureWarning: The
# default
# value
# of
# gamma
# will
# change
# from
# 'auto'
# to
# 'scale' in version
# 0.22
# to
# account
# better
# for unscaled features.Set gamma explicitly to 'auto' or 'scale' to avoid this warning.
# "avoid this warning.", FutureWarning)
# C:\
#     Users\Raghav\Anaconda3\lib\site - packages\sklearn\svm\base.py: 196: FutureWarning: The
# default
# value
# of
# gamma
# will
# change
# from
# 'auto'
# to
# 'scale' in version
# 0.22
# to
# account
# better
# for unscaled features.Set gamma explicitly to 'auto' or 'scale' to avoid this warning.
# "avoid this warning.", FutureWarning)
# plt.bar(activators, svc)
# for i in range(len(activators)):
#     plt.text(i, round(svc[i], 2), round(svc[i] * 100, 2))
# plt.xlabel('Activators')
# plt.ylabel('Score')
# plt.title('Support Vector Classifier')

# def plotDf():
#     dt = []
#     for i in range(1, len(X.columns) + 1):
#         dtc = DecisionTreeClassifier(max_features=i)
#         dtc.fit(X_train, Y_train)
#         dt.append(dtc.score(X_test, Y_test))
#     plt.plot([i for i in range(1, len(X.columns) + 1)], dt, color='red')
#     for i in range(1, len(X.columns) + 1):
#         plt.text(i, dt[i - 1], (i, round(dt[i - 1] * 100, 2)))
#     plt.xticks([i for i in range(1, len(X.columns) + 1)])
#     plt.xlabel('Features')
#     plt.ylabel('Scores')


def convert_plot_to_html(figure):
    buf = BytesIO()
    figure.savefig(buf, format="png", dpi=40)
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


def plo2t(model):
    X_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # test_preds = model.predict(X_test)
    # cmap = sns.cubehelix_palette(as_cmap=True)
    # f, ax = plt.subplots()
    # points = ax.scatter(X_test[:, 0], X_test[:, 1], c=test_preds, s=50, cmap=cmap)
    # f.colorbar(points)
    # plt.show()


def convert_counts_to_html(counts):
    return str(counts).replace("plec stan_zdrowia", "").replace("Name: stan_zdrowia, dtype: int64", "") \
        .replace("Name: plec_tekst, dtype: int64", "").replace("Name: plec, dtype: int64", "") \
        .replace("0.0", "Kobiety").replace("1.0", "Mężczyźni")


def get_coleration(data):
    f, ax = plt.subplots(figsize=(15, 10))
    return convert_plot_to_html(sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=.5).figure)


def get_description(data_set):
    data = data_set.copy()
    plt.rcParams["figure.figsize"] = (15, 15)
    age_plot = convert_plot_to_html(sns.distplot(data['wiek']).figure)
    plt.rcParams["figure.figsize"] = (8, 5)
    thal_plot = convert_plot_to_html(sns.distplot(data['thalach']).figure)
    chol = convert_plot_to_html(sns.distplot(data['cholesterol']).figure)
    pressure_plot = convert_plot_to_html(sns.distplot(data['cisnienie_krwi']).figure)
    exchang_plot = convert_plot_to_html(sns.countplot(data=data, x='exang', hue='stan_zdrowia').figure)
    plt.rcParams["figure.figsize"] = (4, 4)
    old_peak_plot = convert_plot_to_html(sns.countplot(data=data, x='oldpeak', hue='stan_zdrowia').figure)
    slope_plot = convert_plot_to_html(sns.countplot(data=data, x='slope', hue='stan_zdrowia').figure)
    plt.rcParams["figure.figsize"] = (5, 10)
    plot_list = [convert_plot_to_html(
        sns.countplot(data=data, x='bol_w_klatce_piersiowej', hue='stan_zdrowia').figure),
        age_plot, pressure_plot, chol,
        convert_plot_to_html(
            sns.countplot(data=data, x='cukier', hue='stan_zdrowia').figure),
        convert_plot_to_html(
            sns.countplot(data=data, x='restecg', hue='stan_zdrowia').figure),
        thal_plot, exchang_plot,
        old_peak_plot, slope_plot,
        convert_plot_to_html(
            sns.countplot(data=data, x='ca', hue='stan_zdrowia').figure),
        convert_plot_to_html(
            sns.countplot(data=data, x='thal', hue='stan_zdrowia').figure),
        convert_plot_to_html(
            sns.pairplot(data, vars=['wiek', 'cholesterol', 'thal', 'oldpeak'], hue='stan_zdrowia').figure)
    ]
    return plot_list
