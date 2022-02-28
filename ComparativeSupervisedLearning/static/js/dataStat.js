
$(document).ready(function(){

				$.getJSON('/get_data_elaboration',  {}
			, function(dataObject) {

            var parsedDataObject = JSON.parse(JSON.stringify(dataObject));

			$('#exhibit-heart-disease').html(dataObject.exhibit_heart_disease);
			$('#gender-heart-disease').html(dataObject.gender_heart_disease);
			$('#distribution-heart-disease').html(dataObject.distribution_heart_disease);
			$('#coleration-heart-disease').html(dataObject.coleration_heart_disease);
            $('#gender-healt-state').html(dataObject.gender_healt_state);
            $('#age-healt-state').html(dataObject.age_healt_state);
            $('#healt-state-plot1').html(dataObject.healt_state_plot1);
            $('#healt-state-plot2').html(dataObject.healt_state_plot2);
            $('#healt-state-plot3').html(dataObject.healt_state_plot3);
            $('#healt-state-plot4').html(dataObject.healt_state_plot4);
            $('#healt-state-plot5').html(dataObject.healt_state_plot5);
            $('#healt-state-plot6').html(dataObject.healt_state_plot6);
            $('#healt-state-plot7').html(dataObject.healt_state_plot7);
            $('#healt-state-plot8').html(dataObject.healt_state_plot8);
            $('#healt-state-plot9').html(dataObject.healt_state_plot9);
            $('#healt-state-plot10').html(dataObject.healt_state_plot10);
            $('#healt-state-plot11').html(dataObject.healt_state_plot11);
				});

});
