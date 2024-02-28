$(document).ready(function() {
    // Function to fetch and display the translation
    function fetchTranslation() {
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
    }

    // Event listener for the button click
    $('#btn_translate').click(fetchTranslation);

    // Event listener for pressing ENTER in the input field
    $('#language_code').keypress(function(event) {
        if (event.which === 13) { // 13 is the key code for ENTER
            fetchTranslation();
        }
    });
});
