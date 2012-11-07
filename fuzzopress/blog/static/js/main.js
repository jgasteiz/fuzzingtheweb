/*global $, jQuery, document, location*/

/** 
 * Fuzzopress javascript code
 *
 * @author Javi Manzano Oller <javi.manzano.oller@gmail.com> || @jgasteiz
 */
$(document).ready(function () {
    'use strict';

    /**
     * When the light switcher is clicked, toggles between normal and night-mode
     */
    $('.light-switch').click(function () {
        $('body, nav, .main-container, .secondary-menu, footer')
            .toggleClass('night-mode');
    });

    /**
     * When enter-key is pressed when writing some search, it searches it
     */
    $('.fuzz-finder').keypress(function (e) {
        if (e.charCode === 13) {
            var inputText = $(this).val().replace(/ /g, '+');
            location.href = '/search/' + inputText + '/';
        }
    });

    /**
     * When the go-button is pressed when writing some search, it searches it
     */
    $('.fuzz-finder-go').click(function () {
        var inputText = $('.fuzz-finder').val().replace(/ /g, '+');
        if (inputText !== '') {
            location.href = '/search/' + inputText + '/';
        }
    });
});