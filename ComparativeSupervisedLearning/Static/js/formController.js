
	$(function() {
			  $('a#process_form').bind('click', function() {

                jQuery.validator.setDefaults({
                  highlight: function(element) {
                jQuery(element).closest('.form-control').addClass('is-invalid');
                },
                  unhighlight: function(element) {
                jQuery(element).closest('.form-control').removeClass('is-invalid');
                },
                errorElement: 'span',
                errorClass: 'invalid-feedback lang',
                 errorPlacement: function(error, element) {
                 }

                    });

                var validator = $( "#form" ).validate();
                var isValid=validator.form();
                if(isValid){
                $("#loader").removeClass('hidden_div')
				$.getJSON('/submit_action',  {
                    applyExtended : $('#applyExtended').val(),
                    age : $('#inputAge').val(),
                    sex : $('#inputSex').val(),
                    painloc : $('#gridPainLoc').val(),
                    painexer : $('#gridPainEx').val(),
                    relrest : $('#gridPainRelRest').val(),
                    pncaden : computePNCADEN([$('#gridPainLoc').val(),$('#gridPainEx').val(),$('#gridPainRelRest').val()]),
                    pncaden:0,
                    cp : $('#inputChestPain').val(),
                    trestbps : $('#inputBloodPressure').val(),
                    htn : $('#inputFluo').val(),
                    chol : $('#inputBloodChol').val(),
                    smoke : $('#inputSmoke').val(),
                    cigs : $('#inputCigs').val(),
                    years : $('#inputCigsYears').val(),
                    fbs : $('input[name=gridRadiosSugar]:checked').val(),
                    dm : $('#gridDiab').val(),
                    famhist : $('#gridFamDiab').val(),
                    restecg : $('input[name=gridRadiosRestEcg]:checked').val(),
                    dig : $('#gridDig').val(),
                    prop : $('#gridProp').val(),
                    nitr : $('#gridNitr').val(),
                    pro : $('#gridPro').val(),
                    diuretic : $('#gridDiuretic').val(),
                    proto : $('#inputProto').val(),
                    thaldur : $('#inputThaldur').val(),
                    thaltime : $('#inputThalTime').val(),
                    met : $('#inputMets').val(),
                    thalach : $('#inputHeartRate').val(),
                    thalrest : $('#inputThalRest').val(),
                    tpeakbps : $('#inputTpeakBps').val(),
                    tpeakbpd : $('#inputTpeakBpd').val(),
                    trestbpd : $('#inputTrestBpd').val(),
                    exang : $('input[name=gridCheckInducedAngina]:checked').val(),
                    xhypo : $('#gridXhypo').val(),
                    oldpeak : $('input[name=gridCheckOldpeek]:checked').val(),
                    slope : $('#gridSlope').val(),
                    rldv5 : $('#inputRldv5').val(),
                    rldv5e : $('#inputRldv5e').val(),
                    ca : $('#inputChestPain').val(),
                    restef : $('#inputRestef').val(),
                    restwm : $('#inputRestwm').val(),
                    exeref : $('#inputExeref').val(),
                    exerwm : $('#inputExerwm').val(),
                    thal : $('#inputThall').val()
			}
			, function(dataObject) {

            var parsedDataObject = JSON.parse(JSON.stringify(dataObject));
               console.error(parsedDataObject);
			$('#fill-in-form').hide();


    		$('#accuracy-positive-plot-knn').html(dataObject.results_base_knn_plot).show();
    		$('#accuracy-positive-plot-svm').html(dataObject.results_base_svm_plot).show();
    		$('#accuracy-positive-plot-rf').html(dataObject.results_base_rf_plot).show();

    		$('#user_data_plot1').html(dataObject.user_data_plot1).show();
    		$('#user_data_plot2').html(dataObject.user_data_plot2).show();
    		$('#user_data_plot3').html(dataObject.user_data_plot3).show();
    		$('#user_data_plot4').html(dataObject.user_data_plot4).show();
    		$('#user_data_plot9').html(dataObject.user_data_plot5).show();
    		$('#user_data_plot10').html(dataObject.user_data_plot6).show();
    		$('#user_data_plot5').html(dataObject.user_data_plot1).show();
    		$('#user_data_plot6').html(dataObject.user_data_plot2).show();
    		$('#user_data_plot7').html(dataObject.user_data_plot3).show();
    		$('#user_data_plot8').html(dataObject.user_data_plot4).show();
    		$('#user_data_plot11').html(dataObject.user_data_plot5).show();
    		$('#user_data_plot12').html(dataObject.user_data_plot6).show();


    		$('#accuracy-positive-imputed_mean_svm').html(dataObject.accuracy_imputed_mean_svm).show();
    		$('#accuracy-positive-imputed_median_svm').html(dataObject.accuracy_imputed_median_svm).show();
    		$('#accuracy-postive-imputed_most_constant_svm').html(dataObject.accuracy_imputed_most_constant_svm).show();
    		$('#accuracy-positive-imputed_most_frequent_svm').html(dataObject.accuracy_imputed_most_frequent_svm).show();
    		$('#accuracy-negative-imputed_mean_svm').html(dataObject.accuracy_imputed_mean_svm).show();
    		$('#accuracy-negative-imputed_median_svm').html(dataObject.accuracy_imputed_median_svm).show();
    		$('#accuracy-negaive-imputed_most_constant_svm').html(dataObject.accuracy_imputed_most_constant_svm).show();
    		$('#accuracy-negative-imputed_most_frequent_svm').html(dataObject.accuracy_imputed_most_frequent_svm).show();

    		$('#accuracy-positive-imputed_mean_rf').html(dataObject.accuracy_imputed_mean_rf).show();
    		$('#accuracy-positive-imputed_median_rf').html(dataObject.accuracy_imputed_median_rf).show();
    		$('#accuracy-postive-imputed_most_constant_rf').html(dataObject.accuracy_imputed_most_constant_rf).show();
    		$('#accuracy-positive-imputed_most_frequent_rf').html(dataObject.accuracy_imputed_most_frequent_rf).show();
    		$('#accuracy-negative-imputed_mean_rf').html(dataObject.accuracy_imputed_mean_rf).show();
    		$('#accuracy-negative-imputed_median_rf').html(dataObject.accuracy_imputed_median_rf).show();
    		$('#accuracy-negaive-imputed_most_constant_rf').html(dataObject.accuracy_imputed_most_constant_rf).show();
    		$('#accuracy-negative-imputed_most_frequent_rf').html(dataObject.accuracy_imputed_most_frequent_rf).show();

            $('#progress_bar_knn_positive').width(dataObject.results_base_accuracy_text_knn)
            $('#progress_bar_svn_positive').width(dataObject.results_base_accuracy_text_svm)
            $('#progress_bar_rf_positive').width(dataObject.results_base_accuracy_text_rf)
            $('#progress_bar_knn_negative').width(dataObject.results_base_accuracy_text_knn)
            $('#progress_bar_svn_negative').width(dataObject.results_base_accuracy_text_svm)
            $('#progress_bar_rf_negative').width(dataObject.results_base_accuracy_text_rf)

            $('#result_knn_positive').width(dataObject.results_base_accuracy_text_knn)
            $('#result_svn_positive').width(dataObject.results_base_accuracy_text_svm)
            $('#result_rf_positive').width(dataObject.results_base_accuracy_text_rf)
            $('#result_knn_negative').width(dataObject.results_base_accuracy_text_knn)
            $('#result_svn_negative').width(dataObject.results_base_accuracy_text_svm)
            $('#result_rf_negative').width(dataObject.results_base_accuracy_text_rf)

            $('#progress_bar_knn_positive_sp').width(dataObject.results_base_knn_result)
            $('#progress_bar_svn_positive_sp').width(dataObject.results_base_svm_result)
            $('#progress_bar_rf_positive_sp').width(dataObject.results_base_rf_result)
            $('#progress_bar_knn_negative_sp').width(dataObject.results_base_knn_result)
            $('#progress_bar_svn_negative_sp').width(dataObject.results_base_svm_result)
            $('#progress_bar_rf_negative_sp').width(dataObject.results_base_rf_result)


            $('#progress_bar_knn_positive_1').text(dataObject.results_base_accuracy_text_knn)
            $('#progress_bar_svn_positive_1').text(dataObject.results_base_accuracy_text_svm)
            $('#progress_bar_rf_positive_1').text(dataObject.results_base_accuracy_text_rf)
            $('#progress_bar_knn_negative_1').text(dataObject.results_base_accuracy_text_knn)
            $('#progress_bar_svn_negative_1').text(dataObject.results_base_accuracy_text_svm)
            $('#progress_bar_rf_negative_1').text(dataObject.results_base_accuracy_text_rf)

            $('#result_knn_positive_1').text(dataObject.results_base_accuracy_text_knn)
            $('#result_svn_positive_1').text(dataObject.results_base_accuracy_text_svm)
            $('#result_rf_positive_1').text(dataObject.results_base_accuracy_text_rf)
            $('#result_knn_negative_1').text(dataObject.results_base_accuracy_text_knn)
            $('#result_svn_negative_1').text(dataObject.results_base_accuracy_text_svm)
            $('#result_rf_negative_1').text(dataObject.results_base_accuracy_text_rf)

            $('#progress_bar_knn_positive_1_sp').text(dataObject.results_base_knn_result)
            $('#progress_bar_svn_positive_1_sp').text(dataObject.results_base_svm_result)
            $('#progress_bar_rf_positive_1_sp').text(dataObject.results_base_rf_result)
            $('#progress_bar_knn_negative_1_sp').text(dataObject.results_base_knn_result)
            $('#progress_bar_svn_negative_1_sp').text(dataObject.results_base_svm_result)
            $('#progress_bar_rf_negative_1_sp').text(dataObject.results_base_rf_result)

            $("#loader").remove();

			if (dataObject.results_base_positive_negative){
				$('#positive-result').show();
			}
			else {
				$('#negative-result').show();
			}
				});
			$("html").animate({ scrollTop: 0 }, "slow");
				return false;
				}
			  });

			});


function computePNCADEN(gridValuesArray){
    var sum = 0;
    gridValuesArray.forEach(element => {
     if(element!=null && element!=-1){
         sum+=element;
         }
    });
    return sum;
};