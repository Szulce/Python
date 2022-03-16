
$(document).ready(function(){

			$.getJSON('/get_algorithm_elaboration',  {}
			, function(dataObject) {

            var parsedDataObject = JSON.parse(JSON.stringify(dataObject));

            $('#time_knn_1').html(dataObject.time_knn);
            $('#time_svm_1').html(dataObject.time_svm);
            $('#time_rf_1').html(dataObject.time_rf);
            $('#time_knn_2').html(dataObject.time_knn);
            $('#time_svm_2').html(dataObject.time_svm);
            $('#time_rf_2').html(dataObject.time_rf);
            $('#time_knn_3').html(dataObject.time_knn);
            $('#time_svm_3').html(dataObject.time_svm);
            $('#time_rf_3').html(dataObject.time_rf);

            $('#best_estimator_plot_1_knn').html(dataObject.best_estimator_plot_1_knn).show();
    		$('#best_estimator_plot_2_knn').html(dataObject.best_estimator_plot_2_knn).show();
    		$('#best_estimator_plot_1_svm').html(dataObject.best_estimator_plot_1_svm).show();
    		$('#best_estimator_plot_2_svm').html(dataObject.best_estimator_plot_2_svm).show();
    		$('#best_estimator_plot_1_rf').html(dataObject.best_estimator_plot_1_rf).show();
    		$('#best_estimator_plot_2_rf').html(dataObject.best_estimator_plot_2_rf).show();

    		$('#best_estimator_plot_4').html(dataObject.best_estimator_plot_2).show();


			$('#card_text_knn_1').html(dataObject.card_text_knn_1);
			$('#card_text_knn_1_1').html(dataObject.card_text_knn_1_1);
			$('#card_text_knn_1_2').html(dataObject.card_text_knn_1_2);
			$('#card_text_knn_2').html(dataObject.card_text_knn_svm_text);
			$('#card_text_knn_3').html(dataObject.card_text_knn_rf_text);
			$('#card_text_knn_4').html(dataObject.card_text_knn_svm_plot);
			$('#card_text_knn_5').html(dataObject.card_text_knn_rf_plot);

			$('#card_text_svm_1').html(dataObject.card_text_svm_1);
			$('#card_text_svm_1_1').html(dataObject.card_text_svm_1_1);
			$('#card_text_svm_1_2').html(dataObject.card_text_svm_1_2);
			$('#card_text_svm_2').html(dataObject.card_text_knn_svm_text);
			$('#card_text_svm_3').html(dataObject.card_text_knn_svm_plot);
			$('#card_text_svm_4').html(dataObject.card_text_svm_rf_text);
			$('#card_text_svm_5').html(dataObject.card_text_svm_rf_plot);

			$('#card_text_rf_1').html(dataObject.card_text_rf_1);
			$('#card_text_rf_1_1').html(dataObject.card_text_rf_1_1);
			$('#card_text_rf_1_2').html(dataObject.card_text_rf_1_2);
			$('#card_text_rf_2').html(dataObject.card_text_knn_rf_text);
			$('#card_text_rf_3').html(dataObject.card_text_knn_rf_plot);
			$('#card_text_rf_4').html(dataObject.card_text_svm_rf_text);
			$('#card_text_rf_5').html(dataObject.card_text_svm_rf_plot);

			$('#card_plot_all_1').html(dataObject.card_plot_all_1);
			$('#card_plot_all_2').html(dataObject.card_plot_all_2);
			$('#card_plot_all_3').html(dataObject.card_plot_all_3);
			$('#card_plot_all_4').html(dataObject.card_plot_all_4);
			$('#card_plot_all_5').html(dataObject.card_plot_all_5);
			$('#card_plot_all_6').html(dataObject.card_plot_all_6);
			$('#card_plot_all_7').html(dataObject.card_plot_all_7);


			$('#accuracy-positive-imputed_mean_knn').html(dataObject.accuracy_imputed_mean_knn).show();
    		$('#accuracy-positive-imputed_median_knn').html(dataObject.accuracy_imputed_median_knn).show();
    		$('#accuracy-postive-imputed_most_constant_knn').html(dataObject.accuracy_imputed_most_constant_knn).show();
    		$('#accuracy-positive-imputed_most_frequent_knn').html(dataObject.accuracy_imputed_most_frequent_knn).show();
    		$('#accuracy-negative-imputed_mean_knn').html(dataObject.accuracy_imputed_mean_knn).show();
    		$('#accuracy-negative-imputed_median_knn').html(dataObject.accuracy_imputed_median_knn).show();
    		$('#accuracy-negaive-imputed_most_constant_knn').html(dataObject.accuracy_imputed_most_constant_knn).show();
    		$('#accuracy-negative-imputed_most_frequent_knn').html(dataObject.accuracy_imputed_most_frequent_knn).show();


            $('#result-positive-value-knn').html(dataObject.results_base_information_text_knn).show();
			$('#result-negative-value-knn').html(dataObject.results_base_information_text_knn).show();
    		$('#accuracy-negative-value-knn').html(dataObject.results_base_accuracy_text_knn).show();
    		$('#accuracy-positive-value-knn').html(dataObject.results_base_accuracy_text_knn).show();
    		$('#result-positive-value-svm').html(dataObject.results_base_information_text_svm).show();
			$('#result-negative-value-svm').html(dataObject.results_base_information_text_svm).show();
    		$('#accuracy-negative-value-svm').html(dataObject.results_base_accuracy_text_svm).show();
    		$('#accuracy-positive-value-svm').html(dataObject.results_base_accuracy_text_svm).show();
    		$('#result-positive-value-rf').html(dataObject.results_base_information_text_rf).show();
			$('#result-negative-value-rf').html(dataObject.results_base_information_text_rf).show();
    		$('#accuracy-negative-value-rf').html(dataObject.results_base_accuracy_text_rf).show();
    		$('#accuracy-positive-value-rf').html(dataObject.results_base_accuracy_text_rf).show();

				});

});
