from sklearn.model_selection import GridSearchCV
# training a Decision Tree model
from sklearn.tree import DecisionTreeRegressor

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms


def create_train_save_model(x_train, x_test, y_train, y_test):
    param_grid = {'max_depth': Rs.RF_MAX_DEPTH, 'random_state': Rs.RF_RANDOM_STATE}
    grid = GridSearchCV(DecisionTreeRegressor(), param_grid, refit=True, verbose=2)
    grid.fit(x_train, y_train)
    grid.score(x_test, y_test)
    Ms.save_grid_scores(grid, Rs.MODEL_TYPE_RF)

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
