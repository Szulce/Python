
$(document).ready(function(){
				$.getJSON('/get_data_elaboration',  {}
			, function(dataObject) {

            var parsedDataObject = JSON.parse(JSON.stringify(dataObject));
             $('#card_data').removeClass('hidden_div')
             $("#loader").remove();

			$('#exhibit-heart-disease').html(dataObject.exhibit_heart_disease);
			$('#gender-heart-disease').html(dataObject.gender_heart_disease);
			$('#distribution-heart-disease').html(dataObject.distribution_heart_disease);
			$('#coleration-heart-disease').html(dataObject.coleration_heart_disease);
            $('#gender-health-state').html(dataObject.gender_health_state);
            $('#age-health-state').html(dataObject.age_health_state);
            $('#health-state-plot1').html(dataObject.health_state_plot1);
            $('#health-state-plot2').html(dataObject.health_state_plot2);
            $('#health-state-plot3').html(dataObject.health_state_plot3);
            $('#health-state-plot4').html(dataObject.health_state_plot4);
            $('#health-state-plot5').html(dataObject.health_state_plot5);
            $('#health-state-plot6').html(dataObject.health_state_plot6);
            $('#health-state-plot7').html(dataObject.health_state_plot7);
            $('#health-state-plot8').html(dataObject.health_state_plot8);
            $('#health-state-plot9').html(dataObject.health_state_plot9);
            $('#health-state-plot10').html(dataObject.health_state_plot10);
            $('#health-state-plot11').html(dataObject.health_state_plot11);
				});
    }
);
