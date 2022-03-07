from sklearn.model_selection import GridSearchCV
# training a Decision Tree model
from sklearn.tree import DecisionTreeRegressor

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import ComparativeSupervisedLearning.Data.DataConversion as Dc
import ComparativeSupervisedLearning.Management.Elaboration.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms


def create_train_save_model(x_train, x_test, y_train, y_test):
    param_grid = {'max_depth': Rs.RF_MAX_DEPTH, 'random_state': Rs.RF_RANDOM_STATE, 'max_features': Rs.RF_MAX_FEATURES,
                  'criterion': Rs.RF_CRITERION, 'splitter': Rs.RF_SPLITTER, 'min_samples_split': Rs.RF_MIN_SAMPLES,
                  'min_samples_leaf': Rs.RF_MIN_SAMPLES_LEAF,
                  'min_weight_fraction_leaf': Rs.RF_MIN_WEIGHT_FRACTION_LEAF, 'max_leaf_nodes': Rs.RF_MAX_LEAF_NODES,
                  'min_impurity_decrease': Rs.RF_MIN_IMPURITY_DECREASE, 'ccp_alpha': Rs.RF_CPP}
    grid = GridSearchCV(DecisionTreeRegressor(), param_grid, refit=True, verbose=2)
    grid.fit(x_train, y_train)
    grid.score(x_test, y_test)
    Ms.save_grid_scores(grid, Rs.MODEL_TYPE_RF)
    y_predict = grid.predict(x_test)
    Dc.save_prediction_to_json(Plot.create_measure_table(grid.score(x_test, y_test), y_predict, y_test, y_train),
                               Rs.MODEL_TYPE_RF)

#     print(rand_clf.score(x_test, y_test))
#     0.9867256637168141
#     y_preds = rand_clf.predict(x_test)
#     print(classification_report(y_test, y_preds))
#     precision
#     recall
#     f1 - score
#     support
#
#
# 0
# 0.98
# 0.99
# 0.99
# 100
# 1
# 0.99
# 0.98
# 0.99
# 126
#
# accuracy
# 0.99
# 226
# macro
# avg
# 0.99
# 0.99
# 0.99
# 226
# weighted
# avg
# 0.99
# 0.99
# 0.99
# 226
#
# # confusion matrix
# plot_confusion_matrix(rand_clf, x_test, y_test,
#                       cmap=plt.cm.Reds);

# plot_roc_curve(rand_clf, x_test, y_test)
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver Operating Characteristic Curve');
