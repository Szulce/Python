import base64
from io import BytesIO
import numpy
import pandas
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.metrics import explained_variance_score
import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Data.DataConversion as Dc
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms

"""" Generation plots for data and algorithms comparison"""


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


def convert_plot_to_html(figure):
    buf = BytesIO()
    figure.set_size_inches(9.8, 8.8)
    figure.savefig(buf, format="png", dpi=40)
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


def plot_true_values(y_test, y_predict):
    df = y_predict.flatten()
    plt.rcParams["figure.figsize"] = (8, 5)
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
    plt.rcParams["figure.figsize"] = (8, 5)
    plt.boxplot(numpy.array(sum_result).astype(numpy.float))
    plt.xticks(ticks=numpy.array(sum_result).astype(numpy.float), labels=names, rotation=25, fontsize=5)
    return convert_plot_to_html(plt.figure())


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
    f, ax = plt.subplots(figsize=(4, 4))
    return convert_plot_to_html(sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=.5).figure)


def get_legend_out_plot(plot_tmp):
    legend = plot_tmp.get_position()
    plot_tmp.set_position([legend.x0, legend.y0, legend.width * 0.85, legend.height])
    plot_tmp.legend(loc='center right', bbox_to_anchor=(1.88, 0.5), ncol=1)
    return plot_tmp


def get_description(data_set):
    data = data_set.copy()
    plt.rcParams["figure.figsize"] = (15, 15)
    sns.set_context(rc={"font.size": 15, "axes.titlesize": 15, "axes.labelsize": 15})
    age_plot = convert_plot_to_html(sns.distplot(data['wiek']).figure)
    plt.rcParams["figure.figsize"] = (8, 5)
    thal_plot = convert_plot_to_html(sns.distplot(data['thalach']).figure)
    chol = convert_plot_to_html(sns.distplot(data['cholesterol']).figure)
    pressure_plot = get_log_scale_displot(data, 'cisnienie_krwi')
    exchang_plot = convert_plot_to_html(sns.countplot(data=data, x='exang', hue='stan_zdrowia').figure)
    plt.rcParams["figure.figsize"] = (4, 4)
    old_peak_plot = get_log_scale_countplot(data, 'oldpeak', 'stan_zdrowia')
    slope_plot = convert_plot_to_html(sns.countplot(data=data, x='slope', hue='stan_zdrowia').figure)
    plt.rcParams["figure.figsize"] = (5, 10)
    return [convert_plot_to_html(get_legend_out_plot(
        sns.countplot(data=data, x='bol_w_klatce_piersiowej', hue='stan_zdrowia')).figure),
            age_plot, pressure_plot, chol,
            convert_plot_to_html(get_legend_out_plot(
                sns.countplot(data=data, x='cukier', hue='stan_zdrowia')).figure),
            convert_plot_to_html(get_legend_out_plot(
                sns.countplot(data=data, x='restecg', hue='stan_zdrowia')).figure),
            thal_plot, exchang_plot,
            old_peak_plot, slope_plot,
            convert_plot_to_html(get_legend_out_plot(
                sns.countplot(data=data, x='ca', hue='stan_zdrowia')).figure),
            convert_plot_to_html(get_legend_out_plot(
                sns.countplot(data=data, x='thal', hue='stan_zdrowia')).figure),
            convert_plot_to_html(
                sns.pairplot(data, vars=['wiek', 'cholesterol', 'thal', 'oldpeak'], hue='stan_zdrowia').figure)
            ]


def get_log_scale_displot(data, param):
    plot_tmp1 = sns.distplot(data[param])
    return convert_plot_to_html(plot_tmp1.figure)


def get_log_scale_countplot(data, param_1, param_2):
    with sns.plotting_context(None, font_scale=1, rc={"font.size": 8, "axes.titlesize": 8, "axes.labelsize": 5}):
        plot_tmp1 = sns.countplot(data=data, x=param_1, hue=param_2)
    return convert_plot_to_html(plot_tmp1.figure)


def create_measure_table(score, y_predict, y_test, fit_time, predict_time, classificatio_report):
    measures_table = []
    accuracy_score = metrics.accuracy_score(y_test, y_predict)
    balanced_accuracy_score = metrics.balanced_accuracy_score(y_test, y_predict)
    brier_score_loss = metrics.brier_score_loss(y_test, y_predict)
    text1 = str('Precyzja : ') + \
            str(score) + \
            str('%            |                       Wynik klasyfikacji dokładności: ') + \
            str(accuracy_score) + \
            str('             |                       Zrównoważoną dokładność: ') + \
            str(balanced_accuracy_score) + str('  |                   Utrata regresji błędu średniokwadratowego: ') + \
            str(brier_score_loss)
    measures_table.append(text1)
    measures_table.append(plot_true_values(y_test, y_predict))
    measures_table.append(plot_error_measures(y_test, y_predict))
    measures_table.append(str(score))
    measures_table.append(str(accuracy_score))
    measures_table.append(str(explained_variance_score(y_test, y_predict)))
    measures_table.append(str(balanced_accuracy_score))
    measures_table.append(str(brier_score_loss))
    measures_table.append(str(fit_time))
    measures_table.append(str(predict_time))
    measures_table.append(str(classificatio_report))
    return measures_table


def create_measure_table_regression(score, y_predict, y_test, exec_time):
    measures_table = []
    r2_score = metrics.r2_score(y_test, y_predict)
    mae = metrics.r2_score(y_test, y_predict)
    mse = metrics.mean_squared_error(y_test, y_predict)

    text1 = str('Precyzja : ') + \
            str(score) + \
            str('%  |     Współczynnik determinacji (r2): ') + \
            str(r2_score) + \
            str('   |   Średnia utrata regresji błędu bezwzględneg: ') + \
            str(mae) + str('  |   Utrata regresji błędu średniokwadratowego: ') + \
            str(mse)
    measures_table.append(text1)
    measures_table.append(plot_true_values(y_test, y_predict))
    measures_table.append(plot_error_measures(y_test, y_predict))
    measures_table.append(str(score))
    measures_table.append(str(r2_score))
    measures_table.append(str(explained_variance_score(y_test, y_predict)))
    measures_table.append(str(mae))
    measures_table.append(str(mse))
    measures_table.append(str(exec_time))
    return measures_table


def generate_user_data_plot(base_data):
    sns.set_context(rc={"font.size": 20, "axes.titlesize": 20, "axes.labelsize": 15})
    plt.clf()
    plt.cla()
    test_data = Dc.get_unprepared_data()
    base_data_frame = base_data.to_data_frame()
    concatenated = pandas.concat(
        [test_data.assign(dataset='dane testowe'), base_data_frame.assign(dataset='wprowadzone dane')])
    dots_size = 250
    plot1 = convert_plot_to_html(
        sns.scatterplot(x='age', y='chol', hue='dataset', data=concatenated, style='dataset', s=dots_size).figure)
    plot2 = convert_plot_to_html(
        sns.scatterplot(x='sex', y='restecg', hue='dataset', data=concatenated, style='dataset', s=dots_size).figure)
    plot3 = convert_plot_to_html(
        sns.scatterplot(x='cp', y='trestbps', hue='dataset', data=concatenated, style='dataset', s=dots_size).figure)
    plot4 = convert_plot_to_html(
        sns.scatterplot(x='fbs', y='exang', hue='dataset', data=concatenated, style='dataset', s=dots_size).figure)
    plot5 = convert_plot_to_html(
        sns.scatterplot(x='thalach', y='oldpeak', hue='dataset', data=concatenated, style='dataset',
                        s=dots_size).figure)
    plot6 = convert_plot_to_html(
        sns.scatterplot(x='slope', y='ca', hue='dataset', data=concatenated, style='dataset', s=dots_size).figure)
    return [plot1, plot2, plot3, plot4, plot5, plot6]


def best_estimator_compare(iterator, type_m):
    ax = []
    bp = []
    grid = Ms.load_grid_scores(type_m, iterator)
    bp.append(grid.best_params_)
    ax1 = get_algorithm_param_comp(grid, 'mean_test_score', 'std_test_score', 'rank_test_score', 'split0_test_score')
    ax.append(ax1)
    ax2 = get_algorithm_param_comp(grid, 'mean_fit_time', 'std_fit_time', 'mean_score_time', 'std_score_time')
    ax.append(ax2)
    return ax, bp


def get_algorithm_param_comp(grid, means_test_s, means_train_s, stds_test_s, stds_train_s):
    means_test = grid.cv_results_[str(means_test_s)]
    stds_test = grid.cv_results_[str(means_train_s)]
    means_train = grid.cv_results_[str(stds_test_s)]
    stds_train = grid.cv_results_[str(stds_train_s)]

    masks_names = list(grid.best_params_.keys())
    masks = mask_prepare(grid)
    params = grid.param_grid
    ax, fig = figure_prepare(params)

    for i, p in enumerate(masks_names):
        if len(masks) > 1:
            best_index = get_best_index(i, masks)
            if params[p] is not None and params[p][0] is not None:
                x = numpy.array(params[p])
                y_1 = numpy.array(means_test[best_index].astype(numpy.float64))
                e_1 = numpy.array(stds_test[best_index].astype(numpy.float64))
                y_2 = numpy.array(means_train[best_index].astype(numpy.float64))
                e_2 = numpy.array(stds_train[best_index].astype(numpy.float64))
                ax[i].errorbar(x, y_1, e_1, linestyle='--', marker='o', label='test')
                ax[i].errorbar(x, y_2, e_2, linestyle='-', marker='^', label='trening')
                ax[i].set_xlabel(p.upper())

    if len(fig.axes) > 3:
        fig.axes[2].xaxis.set_ticklabels([])
    return specialized_figure(fig)


def get_best_index(i, masks):
    m = numpy.stack(masks[:i] + masks[i + 1:])
    best_parms_mask = m.all(axis=0)
    best_index = numpy.where(best_parms_mask)[0]
    return best_index


def mask_prepare(grid):
    masks = []
    for p_k, p_v in grid.best_params_.items():
        masks.append(list(grid.cv_results_['param_' + p_k].data == p_v))
    return masks


def figure_prepare(params):
    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.rcParams.update({'font.size': 22})
    fig, ax = plt.subplots(1, len(params), sharex='none', sharey='all', figsize=(80, 20))
    fig.suptitle('Wynik dla parametru')
    fig.text(0.04, 0.5, 'Średni wynik', va='center', rotation='vertical')
    return ax, fig


def specialized_figure(fig):
    buf = BytesIO()
    fig.set_size_inches(20, 10)
    fig.savefig(buf, format="png", dpi=40)
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


def get_confusion_matrix():
    fig, axes = plt.subplots(len(Rs.SCORER_DICTIONARY), 1, figsize=(6, 2 * len(Rs.SCORER_DICTIONARY)))
    fig.tight_layout()
    for type_m in Rs.MODELS:
        scorer_m = Ms.load_scorer_models(type_m)
        for ax, i in zip(axes, Rs.SCORER_DICTIONARY.keys()):
            results = scorer_m[i]
            ax.plot(results, 'o--')
            ax.set_title(i)
    return convert_plot_to_html(fig)
