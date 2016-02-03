$(document).ready(function(e) {

	try {
		$("select").msDropDown();
	} catch (e) {
		alert(e.message);
	}

	$('select').change(function() {
		if ($(this).children('option:first-child').is(':selected')) {
			$(this).addClass('select-placeholder');
		} else {
			$(this).removeClass('select-placeholder');
		}
	});

	$('form').each(function() {
		$(this).submit(function(e) {

			showSpinner();

		});
	});
});
