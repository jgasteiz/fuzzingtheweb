/*global $, jQuery, document, console*/

/*
 * Fuzzopress javascript code
 *
 * @author Javi Manzano Oller <javi.manzano.oller@gmail.com> || @jgasteiz
 */

(function($,sr){

  // debouncing function from John Hann
  // http://unscriptable.com/index.php/2009/03/20/debouncing-javascript-methods/
  var debounce = function (func, threshold, execAsap) {
      var timeout;

      return function debounced () {
          var obj = this, args = arguments;
          function delayed () {
              if (!execAsap)
                  func.apply(obj, args);
              timeout = null;
          };

          if (timeout)
              clearTimeout(timeout);
          else if (execAsap)
              func.apply(obj, args);

          timeout = setTimeout(delayed, threshold || 100);
      };
  }
  // smartresize
  jQuery.fn[sr] = function(fn){  return fn ? this.bind('resize', debounce(fn)) : this.trigger(sr); };

})(jQuery,'smartresize');

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

});