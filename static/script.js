function shortenUrl() {
    var longUrl = $('#input_url').val();

    $.ajax({
        url: '/get/' + longUrl,
        type: 'GET',
        success: function(response) {
            console.log(response);
            console.log(response.shortned_url);
            $('#shortUrl').text(response.shortned_url);
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
}