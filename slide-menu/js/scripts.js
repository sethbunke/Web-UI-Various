//https://www.youtube.com/watch?v=TfCHsps4WIc
$(document).ready(function() {
	console.log('doc ready');
	$('a#click-a').click(function(){
		console.log('click');
		$('.nav').toggleClass('nav-view');
	});
});