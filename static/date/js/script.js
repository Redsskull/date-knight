$(document).ready(function() {
    $('#date-form').on('submit', function(event) {
        event.preventDefault();

        $.ajax({
            url: '/',
            type: 'POST',
            data: $(this).serialize(),
            dataType: 'json',
            success: function(data) {

                // Get the date ideas container
                const container = $('#date-ideas-list');

                // Clear any existing date ideas
                container.empty();

                // Add a CSS class to the container that makes the date ideas display in a grid
                container.addClass('grid grid-cols-3 gap-4');

                // Add each new date idea to the container
                data.date_ideas.forEach(function(idea) {
                    container.append(
                        '<div class="bg-rose-50 p-5">' +
                            '<h2 class="font-bold text-gray-700 text-lg mb-4">&#128161; ' + idea.name + '</h2>' +
                            '<p class="text-gray-600 px-3">' + idea.description + '</p>' +
                        '</div>'
                    );
                });
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('AJAX error: ' + textStatus + ' : ' + errorThrown);
            }
        });
    });
});