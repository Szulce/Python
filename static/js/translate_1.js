 // Process translation
    $(function() {
      $('.translate').click(function() {
        var language = $(this).attr('id');
        $('.lang').each(function(index, item) {
          $(this).text(LanguageJson[language][$(this).attr('key')]);
        });
      });
    });


  var LanguageJson = {
      'english': {
        'contact': 'Contact',
        'contact-data':'Contact data',
        'find':'FIND ON',
        'fill-in-form':'Fill in Form',
        'age':'Age',
        'sex':'Sex',
        'no-select':'Not selected',
        'woman':'Woman',
        'man':'Man'
      },
      'polski': {
        'contact': 'Kontakt',
        'contact-data':'Dane kontaktowe',
        'find':'ZNAJDŹ NA',
        'fill-in-form':'Wypełnij formularz',
        'age':'Wiek',
        'sex':'Płeć,',
        'no-select':'Brak',
        'woman':'Kobieta',
        'man':'Mężczyzna'
      }
    };