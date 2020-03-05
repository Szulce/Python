var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
type: 'bar',
data: {
labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
datasets: [{
label: '# of Votes',
data: [12, 19, 3, 5, 2, 3],
backgroundColor: [
'rgba(255, 99, 132, 0.2)',
'rgba(54, 162, 235, 0.2)',
'rgba(255, 206, 86, 0.2)',
'rgba(75, 192, 192, 0.2)',
'rgba(153, 102, 255, 0.2)',
'rgba(255, 159, 64, 0.2)'
],
borderColor: [
'rgba(255,99,132,1)',
'rgba(54, 162, 235, 1)',
'rgba(255, 206, 86, 1)',
'rgba(75, 192, 192, 1)',
'rgba(153, 102, 255, 1)',
'rgba(255, 159, 64, 1)'
],
borderWidth: 1
}]
},
options: {
scales: {
yAxes: [{
ticks: {
beginAtZero: true
}
}]
}
}
});



//$(document).ready(function() {
//
//(function($){
//	$('#form').on('submit', function(event) {
//            event.preventDefault();
//        var formData = JSON.stringify($("#form").serializeArray());
//		$.ajax({
//		data: formData,
////			json_data: {
////                    id : 1,//todo
////                    age : $('#inputAge').val(),
////                    sex : $('#inputSex').val(),
////                    painloc : $('#gridPainLoc').val(),
////                    painexer : $('#gridPainEx').val(),
////                    relrest : $('#gridPainRelRest').val(),
//////                    pncaden : computePNCADEN([$('#gridPainLoc').val()+$('#gridPainEx').val()+$('#gridPainRelRest').val()]),
////                    pncaden:0,
////                    cp : $('#inputChestPain').val(),
////                    trestbps : $('#inputBloodPressure').val(),
////                    htn : $('#inputFluo').val(),
////                    chol : $('#inputBloodChol').val(),
////                    smoke : $('#inputSmoke').val(),
////                    cigs : $('#inputCigs').val(),
////                    years : $('#inputCigsYears').val(),
//////                    fbs : $('#gridRadiosSugar').val().get('gridRadiosSugar'),
////                    fbs:15,
////                    dm : $('#gridDiab').val(),
////                    famhist : $('#gridFamDiab').val(),
//////                    restecg : $('#gridRadiosRestEcg').val().get('gridRadiosRestEcg'),
////                    restecg : 15,
////                    dig : $('#gridDig').val(),
////                    prop : $('#gridProp').val(),
////                    nitr : $('#gridNitr').val(),
////                    pro : $('#gridPro').val(),
////                    diuretic : $('#gridDiuretic').val(),
////                    proto : $('#inputProto').val(),
////                    thaldur : $('#inputThaldur').val(),
////                    thaltime : $('#inputThalTime').val(),
////                    met : $('#inputMets').val(),
////                    thalach : $('#inputHeartRate').val(),
////                    thalrest : $('#inputThalRest').val(),
////                    tpeakbps : $('#inputTpeakBps').val(),
////                    tpeakbpd : $('#inputTpeakBpd').val(),
////                    trestbpd : $('#inputTrestBpd').val(),
////                    exang : $('#gridCheckInducedAngina').val(),
////                    xhypo : $('#gridXhypo').val(),
////                    oldpeak : $('#gridCheckOldpeek').val(),
////                    slope : $('#gridSlope').val(),
////                    rldv5 : $('#inputRldv5').val(),
////                    rldv5e : $('#inputRldv5e').val(),
////                    ca : $('#inputChestPain').val(),
////                    restef : $('#inputRestef').val(),
////                    restwm : $('#inputRestwm').val(),
////                    exeref : $('#inputExeref').val(),
////                    exerwm : $('#inputExerwm').val(),
////                    thal : $('#inputThall').val()
////			},
//			type : 'POST',
//			dataType : "json",
//			url : "/submit_action"
//
//		})
//		.done(function(data) {
//		//todo
//
//		});
//		    })(jQuery);

//        prevents basic submit action


//	});
//
//});

//function computePNCADEN(gridValuesArray){
//    var sum = 0;
//    gridValuesArray.forEach(element => {
//     if(element!=null %% element!=-1){
//         sum+=element;
//         }
//    });
//    return sum;
//};
//
//function getRadioButtonSingleAnswer(radioButtonImmutableDictionary,Name){
//    return radioButtonImmutableDictionary.get(Name);
//};


//$('#submitButton').click(function(event){
//    // Prevent redirection with AJAX for contact form
//    var form = $('#form');
//    var url = form.prop('action');
//    var type = form.prop('method');
//    var formData = document.getElementById(form);
//
//    // submit form via AJAX
//     $.ajax({
//        url: url,
//        type: type,
//        data: {"a": 1, "b":"foo","c":null},
//        processData: false,
//        contentType: false
//        dataType:'multipart/form-data'
//    });
//};
//});

//
// $(document).ready(function() {
//        $('form').submit(function (e) {
//            var url = "{{ url_for('submitActionForm') }}"; // send the form data here.
//            $.ajax({
//                type: "POST",
//                url: url,
//                data: $('form').serialize(), // serializes the form's elements.
//                success: function (data) {
//                    console.log(data)  // display the returned data in the console.
//                },
//                error:{
//                  console.log(data)
//                  }
//            });
//            e.preventDefault(); // block the traditional submission of the form.
//        });
//
//    });

//  function submitForm(){
//
//        $('form').submit(function (e) {
//            var url = "{{ url_for('submitActionForm') }}"; // send the form data here.
//            $.ajax({
//                type: "POST",
//                url: url,
//                data: $('form').serialize(), // serializes the form's elements.
//                success: function (data) {
//                    console.log(data)  // display the returned data in the console.
//                },
//                error:{
//                  console.log(data)
//                  }
//            });
//            e.preventDefault(); // block the traditional submission of the form.
//        });
//    }