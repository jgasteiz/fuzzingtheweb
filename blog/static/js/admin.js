/*global $, jQuery, document, console*/

/*
 * Fuzzopress javascript code
 *
 * @author Javi Manzano Oller <javi.manzano.oller@gmail.com> || @jgasteiz
 */
var fuzzopress = fuzzopress || {};
$(document).ready(function () {
	$('.markitup-editor').markItUp(fuzzopress.mySettings);
});