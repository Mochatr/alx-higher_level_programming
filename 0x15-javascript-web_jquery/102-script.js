$(document).ready(function() {
    $('#btn_translate').click(function() {
        var languageCode = $('#language_code').val();
        if (languageCode) {
            $.ajax({
                url: 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode,
                method: 'GET',
                success: function(data) {
                    $('#hello').text(data);
                },
                error: function(error) {
                    console.error('Error fetching translation:', error);
                }
            });
        } else {
            alert('Please enter a language code.');
        }
    });
});
