
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

             $('#another_1_knn_param').html(dataObject.another_1_knn_param);
             $('#another_1_knn_time').html(dataObject.another_1_knn_time);
             $('#another_1_svm_param').html(dataObject.another_1_svm_param);
             $('#another_1_svm_time').html(dataObject.another_1_knn_time);
             $('#another_1_rf_time').html(dataObject.another_1_rf_param);
             $('#another_1_rf_time').html(dataObject.another_1_rf_time);

             $('#another_1_6').html(dataObject.another_1_6);
             $('#another_1_7').html(dataObject.another_1_7);
             $('#another_1_8').html(dataObject.another_1_8);
             $('#another_1_9').html(dataObject.another_1_9);
             $('#another_1_10').html(dataObject.another_1_10);
             $('#another_1_11').html(dataObject.another_1_11);
             $('#another_1_12').html(dataObject.another_1_12);
             $('#another_1_13').html(dataObject.another_1_13);
             $('#another_1_14').html(dataObject.another_1_14);
             $('#another_1_15').html(dataObject.another_1_15);
             $('#another_1_16').html(dataObject.another_1_16);
             $('#another_1_17').html(dataObject.another_1_17);
             $('#another_1_18').html(dataObject.another_1_18);
             $('#another_1_19').html(dataObject.another_1_19);
             $('#another_1_20').html(dataObject.another_1_20);
             $('#another_1_21').html(dataObject.another_1_21);
             $('#another_1_22').html(dataObject.another_1_22);
             $('#another_1_23').html(dataObject.another_1_23);
             $('#another_1_24').html(dataObject.another_1_24);
             $('#another_1_25').html(dataObject.another_1_25);
             $('#another_1_26').html(dataObject.another_1_26);
             $('#another_1_27').html(dataObject.another_1_27);
             $('#another_1_28').html(dataObject.another_1_28);
             $('#another_1_29').html(dataObject.another_1_29);
             $('#another_1_30').html(dataObject.another_1_30);
             $('#another_1_31').html(dataObject.another_1_31);
             $('#another_1_32').html(dataObject.another_1_32);
             $('#another_1_33').html(dataObject.another_1_33);
             $('#another_1_34').html(dataObject.another_1_34);
             $('#another_1_35').html(dataObject.another_1_35);
             $('#another_1_36').html(dataObject.another_1_36);
             $('#another_1_37').html(dataObject.another_1_37);
             $('#another_1_38').html(dataObject.another_1_38);
             $('#another_1_39').html(dataObject.another_1_39);
             $('#another_1_40').html(dataObject.another_1_40);
             $('#another_1_41').html(dataObject.another_1_41);
             $('#another_1_42').html(dataObject.another_1_42);
             $('#another_1_43').html(dataObject.another_1_43);
             $('#another_1_44').html(dataObject.another_1_44);
             $('#another_1_45').html(dataObject.another_1_45);
             $('#another_1_46').html(dataObject.another_1_46);
             $('#another_1_47').html(dataObject.another_1_47);
             $('#another_1_48').html(dataObject.another_1_48);
             $('#another_1_49').html(dataObject.another_1_49);
             $('#another_1_50').html(dataObject.another_1_50);
             $('#another_1_51').html(dataObject.another_1_51);
             $('#another_1_52').html(dataObject.another_1_52);
             $('#another_1_53').html(dataObject.another_1_53);
             $('#another_1_54').html(dataObject.another_1_54);
             $('#another_1_55').html(dataObject.another_1_55);
             $('#another_1_56').html(dataObject.another_1_56);
             $('#another_1_57').html(dataObject.another_1_57);
             $('#another_1_58').html(dataObject.another_1_58);
             $('#another_1_59').html(dataObject.another_1_59);
             $('#another_1_60').html(dataObject.another_1_60);
             $('#another_1_61').html(dataObject.another_1_61);
             $('#another_1_62').html(dataObject.another_1_62);
             $('#another_1_63').html(dataObject.another_1_63);
             $('#another_1_64').html(dataObject.another_1_64);
             $('#another_1_65').html(dataObject.another_1_65);
             $('#another_1_66').html(dataObject.another_1_66);
             $('#another_1_67').html(dataObject.another_1_67);
             $('#another_1_68').html(dataObject.another_1_68);
             $('#another_1_69').html(dataObject.another_1_69);
             $('#another_1_70').html(dataObject.another_1_70);
             $('#another_1_71').html(dataObject.another_1_71);
             $('#another_1_72').html(dataObject.another_1_72);
             $('#another_1_73').html(dataObject.another_1_73);
             $('#another_1_74').html(dataObject.another_1_74);
             $('#another_1_75').html(dataObject.another_1_75);
             $('#another_1_76').html(dataObject.another_1_76);
             $('#another_1_77').html(dataObject.another_1_77);
             $('#another_1_78').html(dataObject.another_1_78);
             $('#another_1_79').html(dataObject.another_1_79);
             $('#another_1_80').html(dataObject.another_1_80);
             $('#another_1_81').html(dataObject.another_1_81);
             $('#another_1_82').html(dataObject.another_1_82);
             $('#another_1_83').html(dataObject.another_1_83);
             $('#another_1_84').html(dataObject.another_1_84);
             $('#another_1_85').html(dataObject.another_1_85);
             $('#another_1_86').html(dataObject.another_1_86);
             $('#another_1_87').html(dataObject.another_1_87);
             $('#another_1_88').html(dataObject.another_1_88);
             $('#another_1_89').html(dataObject.another_1_89);
             $('#another_1_90').html(dataObject.another_1_90);
             $('#another_1_91').html(dataObject.another_1_91);
             $('#another_1_92').html(dataObject.another_1_92);
             $('#another_1_93').html(dataObject.another_1_93);
             $('#another_1_94').html(dataObject.another_1_94);
             $('#another_1_95').html(dataObject.another_1_95);
             $('#another_1_96').html(dataObject.another_1_96);
             $('#another_1_97').html(dataObject.another_1_97);
             $('#another_1_98').html(dataObject.another_1_98);
             $('#another_1_99').html(dataObject.another_1_99);
             $('#another_1_100').html(dataObject.another_1_100);
             $('#another_1_101').html(dataObject.another_1_101);
             $('#another_1_102').html(dataObject.another_1_102);
             $('#another_1_103').html(dataObject.another_1_103);
             $('#another_1_104').html(dataObject.another_1_104);
             $('#another_1_105').html(dataObject.another_1_105);
             $('#another_1_106').html(dataObject.another_1_106);
             $('#another_1_107').html(dataObject.another_1_107);
             $('#another_1_108').html(dataObject.another_1_108);
             $('#another_1_109').html(dataObject.another_1_109);
             $('#another_1_110').html(dataObject.another_1_110);
             $('#another_1_111').html(dataObject.another_1_111);
             $('#another_1_112').html(dataObject.another_1_112);
             $('#another_1_113').html(dataObject.another_1_113);
             $('#another_1_114').html(dataObject.another_1_114);
             $('#another_1_115').html(dataObject.another_1_115);
             $('#another_1_116').html(dataObject.another_1_116);
             $('#another_1_117').html(dataObject.another_1_117);
             $('#another_1_118').html(dataObject.another_1_118);
             $('#another_1_119').html(dataObject.another_1_119);
             $('#another_1_120').html(dataObject.another_1_120);
             $('#another_1_121').html(dataObject.another_1_121);
             $('#another_1_122').html(dataObject.another_1_122);
             $('#another_1_123').html(dataObject.another_1_123);
             $('#another_1_124').html(dataObject.another_1_124);
             $('#another_1_125').html(dataObject.another_1_125);


				});

});
