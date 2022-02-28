import base64
from io import BytesIO

import numpy
import pandas
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import roc_curve, precision_score, recall_score, explained_variance_score

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


def plot_true_values(y_test, y_predict):
    a = plt.axes(aspect='equal')
    plt.scatter(y_test, y_predict.flatten())
    plt.xlabel('Wartości rzeczywiste ')
    plt.ylabel('Prognozy ')
    lims = [0, 920]
    plt.xlim(lims)
    plt.ylim(lims)
    plot_values = plt.plot(lims, lims)
    return convert_plot_to_html(plot_values[0].figure)


def create_figure_two_models(results_0, results_1, name_1, name_2):
    sum_result = [results_0[3], results_1[3]]
    names = [name_1, name_2]
    fig = plt.figure()
    fig.suptitle('Porównanie Algorytmów')
    ax = fig.add_subplot(111)
    plt.boxplot(numpy.array(sum_result).astype(numpy.float))
    # ax.set_xticklabels(names)
    return convert_plot_to_html(fig)


def plot_error_measures(y_test, y_predict):
    error = y_predict.flatten() - y_test
    plt.hist(error, bins=125)
    plt.xlabel("Błąd prognozy")
    plot_error = plt.ylabel("Zlicz")
    return convert_plot_to_html(plot_error.figure)


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


def create_measure_table(score, y_predict, y_test, y_train):
    measures_table = []
    r2_score = metrics.r2_score(y_test, y_predict)
    mae = metrics.r2_score(y_test, y_predict)
    mse = metrics.mean_squared_error(y_test, y_predict)
    text1 = str('Precyzja : ') + str(score) + str('       Współczynnik determinacji (r2):') \
            + str(r2_score) + str('      Średnia utrata regresji błędu bezwzględneg: ') + \
            str(mae) + str('     Utrata regresji błędu średniokwadratowego') + \
            str(mse)
    measures_table.append(text1)
    measures_table.append(plot_true_values(y_test, y_predict))
    measures_table.append(plot_error_measures(y_test, y_predict))
    measures_table.append(str(score))
    measures_table.append(str(r2_score))
    measures_table.append(str(explained_variance_score(y_test, y_predict)))
    measures_table.append(str(mae))
    measures_table.append(str(mse))
    return measures_table


def create_figure_two_models_text(param, param1, MODEL_TYPE_1, MODEL_TYPE_2):
    return None


def create_comparison_plots(results):
    columns = []
    compare = pandas.DataFrame(columns=columns)
    grids = [results[0], results[1], results[2]]
    row_index = 0
    for model in Rs.MODELS:
        # fp, tp, th = roc_curve(y_test, predicted)
        compare.loc[row_index, 'Algorytmy'] = model
        compare.loc[row_index, 'Precyzja'] = numpy.array(grids[row_index][3]).astype(numpy.float)
        compare.loc[row_index, 'Współczynnik determinacji'] = numpy.array(grids[row_index][4]).astype(numpy.float)
        compare.loc[row_index, 'Funkcja wyniku regresji wariancji'] = numpy.array(grids[row_index][5]).astype(numpy.float)
        compare.loc[row_index, 'Średnia utrata regresji błędu bezwzględnego'] = numpy.array(grids[row_index][6]).astype(numpy.float)
        compare.loc[row_index, 'Utrata regresji błędu średniokwadratowego'] = numpy.array(grids[row_index][7]).astype(numpy.float)

        # compare.loc[row_index, 'Dokładność na danych testowych'] = model.score
        # compare.loc[row_index, 'Precyzja'] = precision_score(y_test, predicted)
        # compare.loc[row_index, 'Błąd'] = recall_score(y_test, predicted)
        # MLA_compare.loc[row_index, 'AUC'] = auc(fp, tp)
        row_index += 1

    organised_data = compare.sort_values(by=['Precyzja'], ascending=False, inplace=True)

    plt.subplots(figsize=(13, 5))
    sns.barplot(x="Algorytmy", y="Precyzja", data=compare, palette='hot',
                edgecolor=sns.color_palette('dark', 7))
    plt.xticks(rotation=90)
    plt.title('Porównanie precyzji algorytmów')
    plot_1 = convert_plot_to_html(plt.figure())

    plt.subplots(figsize=(13, 5))
    sns.barplot(x="Algorytmy", y="Współczynnik determinacji", data=compare, palette='hot',
                edgecolor=sns.color_palette('dark', 7))
    plt.xticks(rotation=90)
    plot_2 = convert_plot_to_html(plt.figure())

    plt.subplots(figsize=(13, 5))
    sns.barplot(x="Algorytmy", y="Funkcja wyniku regresji wariancji", data=compare, palette='hot', edgecolor=sns.color_palette('dark', 7))
    plt.xticks(rotation=90)
    plot_3 = convert_plot_to_html(plt.figure())

    plt.subplots(figsize=(13, 5))
    sns.barplot(x="Algorytmy", y="Średnia utrata regresji błędu bezwzględnego", data=compare, palette='hot',
                edgecolor=sns.color_palette('dark', 7))
    plt.xticks(rotation=90)
    plot_4 = convert_plot_to_html(plt.figure())

    plt.subplots(figsize=(13, 5))
    sns.barplot(x="Algorytmy", y="Utrata regresji błędu średniokwadratowego", data=compare, palette='hot', edgecolor=sns.color_palette('dark', 7))
    plt.xticks(rotation=90)
    plot_5 = convert_plot_to_html(plt.figure())

    return plot_1, plot_2, plot_3, plot_4, plot_5, organised_data
