
$(document).ready(function(){

			$.getJSON('/get_algorithm_elaboration',  {}
			, function(dataObject) {

            var parsedDataObject = JSON.parse(JSON.stringify(dataObject));

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


				});

});
