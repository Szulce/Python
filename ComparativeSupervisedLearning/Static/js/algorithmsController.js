
$(document).ready(function(){

			$.getJSON('/get_algorithm_elaboration',  {}
			, function(dataObject) {

            var parsedDataObject = JSON.parse(JSON.stringify(dataObject));

            $('#knn_mean_desc').html(dataObject.knn_mean_desc);
            $('#knn_mean_plot1').html(dataObject.knn_mean_plot1);
            $('#knn_mean_plot2').html(dataObject.knn_mean_plot2);
            $('#knn_mean_best_params').html(dataObject.knn_mean_best_params);

            $('#svm_mean_desc').html(dataObject.svm_mean_desc);
            $('#svm_mean_plot1').html(dataObject.svm_mean_plot1);
            $('#svm_mean_plot2').html(dataObject.svm_mean_plot2);
            $('#svm_mean_best_params').html(dataObject.svm_mean_best_params);

            $('#rf_mean_desc').html(dataObject.rf_mean_desc);
            $('#rf_mean_plot1').html(dataObject.rf_mean_plot1);
            $('#rf_mean_plot2').html(dataObject.rf_mean_plot2);
            $('#rf_mean_best_params').html(dataObject.rf_mean_best_params);

            $('#knn_median_desc').html(dataObject.knn_median_desc);
            $('#knn_median_plot1').html(dataObject.knn_median_plot1);
            $('#knn_median_plot2').html(dataObject.knn_median_plot2);
            $('#knn_median_best_params').html(dataObject.knn_median_best_params);

            $('#svm_median_desc').html(dataObject.svm_median_desc);
            $('#svm_median_plot1').html(dataObject.svm_median_plot1);
            $('#svm_median_plot2').html(dataObject.svm_median_plot2);
            $('#svm_median_best_params').html(dataObject.svm_median_best_params);

            $('#rf_median_desc').html(dataObject.rf_median_desc);
            $('#rf_median_plot1').html(dataObject.rf_median_plot1);
            $('#rf_median_plot2').html(dataObject.rf_median_plot2);
            $('#rf_median_best_params').html(dataObject.rf_median_best_params);

            $('#knn_freq_desc').html(dataObject.knn_freq_desc);
            $('#knn_freq_plot1').html(dataObject.knn_freq_plot1);
            $('#knn_freq_plot2').html(dataObject.knn_freq_plot2);
            $('#knn_freq_best_params').html(dataObject.knn_freq_best_params);

            $('#svm_freq_desc').html(dataObject.svm_freq_desc);
            $('#svm_freq_plot1').html(dataObject.svm_freq_plot1);
            $('#svm_freq_plot2').html(dataObject.svm_freq_plot2);
            $('#svm_freq_best_params').html(dataObject.svm_freq_best_params);

            $('#rf_freq_desc').html(dataObject.rf_freq_desc);
            $('#rf_freq_plot1').html(dataObject.rf_freq_plot1);
            $('#rf_freq_plot2').html(dataObject.rf_freq_plot2);
            $('#rf_freq_best_params').html(dataObject.rf_freq_best_params);

            $('#knn_cont_desc').html(dataObject.knn_cont_desc);
            $('#knn_cont_plot1').html(dataObject.knn_cont_plot1);
            $('#knn_cont_plot2').html(dataObject.knn_cont_plot2);
            $('#knn_cont_best_params').html(dataObject.knn_cont_best_params);

            $('#svm_cont_desc').html(dataObject.svm_cont_desc);
            $('#svm_cont_plot1').html(dataObject.svm_cont_plot1);
            $('#svm_cont_plot2').html(dataObject.svm_cont_plot2);
            $('#svm_cont_best_params').html(dataObject.svm_cont_best_params);

            $('#rf_cont_desc').html(dataObject.rf_cont_desc);
            $('#rf_cont_plot1').html(dataObject.rf_cont_plot1);
            $('#rf_cont_plot2').html(dataObject.rf_cont_plot2);
            $('#rf_cont_best_params').html(dataObject.rf_cont_best_params);


            $('#time_knn_1').html(dataObject.time_knn_train);
            $('#time_svm_1').html(dataObject.time_svm_train);
            $('#time_rf_1').html(dataObject.time_rf_train);
            $('#time_knn_2').html(dataObject.time_knn_train);
            $('#time_svm_2').html(dataObject.time_svm_train);
            $('#time_rf_2').html(dataObject.time_rf_train);
            $('#time_knn_3').html(dataObject.time_knn_train);
            $('#time_svm_3').html(dataObject.time_svm_train);
            $('#time_rf_3').html(dataObject.time_rf_train);

            $('#time_knn_4').html(dataObject.time_knn_predict);
            $('#time_svm_4').html(dataObject.time_svm_predict);
            $('#time_rf_4').html(dataObject.time_rf_predict);
            $('#time_knn_5').html(dataObject.time_knn_predict);
            $('#time_svm_5').html(dataObject.time_svm_predict);
            $('#time_rf_5').html(dataObject.time_rf_predict);
            $('#time_knn_6').html(dataObject.time_knn_predict);
            $('#time_svm_6').html(dataObject.time_svm_predict);
            $('#time_rf_6').html(dataObject.time_rf_predict);

            $('#confusion_1').html(dataObject.confusion);
            $('#confusion_2').html(dataObject.confusion);
            $('#confusion_3').html(dataObject.confusion);

            $('#classification_report_knn_1').html(dataObject.classification_report_knn_1);
            $('#classification_report_knn_2').html(dataObject.classification_report_knn_2);
            $('#classification_report_knn_3').html(dataObject.classification_report_knn_3);
            $('#classification_report_knn_4').html(dataObject.classification_report_knn_4);

            $('#classification_report_svm_1').html(dataObject.classification_report_svm_1);
            $('#classification_report_svm_2').html(dataObject.classification_report_svm_2);
            $('#classification_report_svm_3').html(dataObject.classification_report_svm_3);
            $('#classification_report_svm_4').html(dataObject.classification_report_svm_4);

            $('#classification_report_rf_1').html(dataObject.classification_report_rf_1);
            $('#classification_report_rf_2').html(dataObject.classification_report_rf_2);
            $('#classification_report_rf_3').html(dataObject.classification_report_rf_3);
            $('#classification_report_rf_4').html(dataObject.classification_report_rf_4);

				});

});
