/*global $, jQuery, document, console*/

/*
 * Fuzzopress javascript code
 *
 * @author Javi Manzano Oller <javi.manzano.oller@gmail.com> || @jgasteiz
 */
var fuzzopress = fuzzopress || {};
$(document).ready(function () {
    'use strict';

    /*
     * When the light switcher is clicked, toggles between normal and night-mode.
     */
    $('#light_switch').click(function (e) {
        e.preventDefault();
        $('body').toggleClass('night-mode').toggleClass('normal');
        var url = $(this).attr('data-href') + $('body').attr('class');
        $.get(url, {}, function(data) {
            return false;
        });
    });

    /*
     * When the go-button is pressed when writing some search, it searches it.
     */
    $('#menu_opener').click(function () {
        $('#menu').slideToggle();
    });

    /*
     * Ajax logic for archive viewing.
     */
    $('.archive').find('.date').bind('click', function(e) {
        e.preventDefault();
        var url = $(this).attr('data-href'),
            parent = $(this).parent();

        $.get(url, {}, function(data) {
            var posts = JSON.parse(data),
                $ul = $('<ul>');
            for (var i in posts) {
                $($ul).append($('<li>').append(
                    $('<a>').attr('href', posts[i].url)
                            .attr('target', '_blank')
                            .html(posts[i].title)
                ));
            }
            $(parent).append($ul);
        });
    });

	$('.markitup-editor').markItUp(fuzzopress.mySettings);

});