var DEBUG = false;

var DEFAULT_ALERT_CLOSE_DELAY = 5000;
var DEFAULT_ALERT_TYPE = "info";

/*
 * All jQuery AJAX posts require this!
 */
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
	beforeSend : function(xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});


function showSpinner() {
	spinner.css({
		visibility : 'visible'
	});
}
function hideSpinner() {
	spinner.css({
		visibility : 'hidden'
	});
}

var spinner = $('#spinner');

$(document).ready(function() {

	if (DEBUG) { 
		$(window).resize(function() {
			showAlert($(window).width() + ' x ' + $(window).height(), 2000);
		});
	}
	
	isIOS = /iPad|iPhone|iPod/.test(navigator.platform);
	isAndroid = /(android)/i.test(navigator.userAgent);

	spinner.position({
		my : 'center top+120',
		at : 'center top+120',
		of : 'body'
	});

});

