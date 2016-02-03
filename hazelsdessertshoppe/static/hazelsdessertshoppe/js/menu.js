$(document).ready(function() {
    $('#list-view').click(function(event){
    	event.preventDefault();
    	$('#categories-list .item').addClass('list-group-item');
    });
    
    $('#grid-view').click(function(event){
    	event.preventDefault();
    	$('#categories-list .item').removeClass('list-group-item');
    	$('#categories-list .item').addClass('grid-group-item');
    });
});