const $ = window.$;
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('INPUT#btn_translate').click(function () {
    const value = $('INPUT#language_code').val();
    $.get(url + value, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  });
});
