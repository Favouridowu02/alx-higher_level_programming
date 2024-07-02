const $ = window.$;
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fri';
  $.get(url, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
});
