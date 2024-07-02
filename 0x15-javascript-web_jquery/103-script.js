const $ = window.$;
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('INPUT#btn_translate').click(function () {
    print();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      print();
    }
  });

  function print () {
    const lang = $('INPUT#language_code').val();
    $.get(url + lang, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  }
});
