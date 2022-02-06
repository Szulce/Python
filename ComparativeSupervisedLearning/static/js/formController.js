
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
//                if(element.parent('.input-group').length) {
//                    error.insertAfter(element.parent());
//                } else {
//                    error.insertAfter(element);
//                }
                 }

                    });



                var validator = $( "#form" ).validate();
                var isValid=validator.form();

                if(isValid){

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
            console.info(parsedDataObject);
			$('#fill-in-form').hide();
			$('#result-positive-value').text(dataObject.results_base_information_text).show();
			$('#result-negative-value').text(dataObject.results_base_information_text).show();
			$('#accuracy-value').text(dataObject.results_base_accuracy_text).show();
			if(parsedDataObject.applyExtended){
			if(parsedDataObject.results_full.percentageKNN
			|| parsedDataObject.results_full.percentageSVM
			|| parsedDataObject.results_full.percentageRF
			) {
			$('#positive-result').show();
			}
			else {
				$('#negative-result').show();
			}
			}else{
			if (parsedDataObject.results_base.percentageKNN
			&& parsedDataObject.results_base.percentageSVM
			&& parsedDataObject.results_base.percentageRF){
				$('#positive-result').show();
			}
			else {
				$('#negative-result').show();
			}
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

function applyExtended(){
//todo dlaczego zwraca pusta wartosc
console.error(document.getElementById("applyExtended").value);
document.getElementById("applyExtended").value = ! document.getElementById("applyExtended").value;
}


function createChart(){
      new Chart(document.getElementById("myCanvas"), {
          type: 'bar',
          data: {
            labels: algorithm,
            datasets: [
              {
                label: "Percentage od accuracy",
                backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f"],
                data: value
              }
            ]
          },
          options: {
            legend: { display: false },
            title: {
              display: true,
              text: 'Accuracy'
            }
          }
      });
      }