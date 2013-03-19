/*global $, jQuery, document, console*/

/*
 * Fuzzopress javascript code
 *
 * @author Javi Manzano Oller <javi.manzano.oller@gmail.com> || @jgasteiz
 */
$(document).ready(function () {
    'use strict';

    /*
     * When the light switcher is clicked, toggles between normal and night-mode.
     */
    $('.light-switch').click(function (e) {
        e.preventDefault();
        $('body').toggleClass('night-mode').toggleClass('normal');
        var url = $(this).attr('data-href') + $('body').attr('class');
        $.get(url, {}, function(data) {
            return false;
        });
    });

    /*
     * When enter-key is pressed when writing some search, it searches it.
     */
    $('.fuzz-finder').keypress(function (e) {
        if (e.charCode === 13) {
            findPosts();
        }
    });

    /*
     * When the go-button is pressed when writing some search, it searches it.
     */
    $('.fuzz-finder-go').click(function () { findPosts(); });

    /*
     * Retrieves the text from the input box and starts the search.
     */
    var findPosts = function() {
        var inputText = $('.fuzz-finder').val().replace(/ /g, '+');
        if (inputText !== '') {
            window.location.href = '/search/' + inputText + '/';
        }
    };

    /*
     * Ajax logic for archive viewing.
     */
    $('.archive').find('.date').bind('click', function(e) {
        e.preventDefault();
        var url = $(this).attr('href'),
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
});

