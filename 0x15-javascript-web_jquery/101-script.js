$(document).ready(function() {
    // Function to add a new item to the list
    function addItem() {
        $('.my_list').append('<li>Item</li>');
    }

    // Function to remove the last item from the list
    function removeItem() {
        $('.my_list li:last').remove();
    }

    // Function to clear all items from the list
    function clearList() {
        $('.my_list').empty();
    }

    // Event listeners for the click events
    $('#add_item').click(addItem);
    $('#remove_item').click(removeItem);
    $('#clear_list').click(clearList);
});
