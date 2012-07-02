

$(document).ready(function() {
	var SIDEBAR_SHOWN = true;
	$(".toggle-sidebar").click(function() {
		if (SIDEBAR_SHOWN == true) {
			SIDEBAR_SHOWN = false;
			$(".articles").css("width", "92%");
			$(".toggle-sidebar span").html("<<");
			$(".sidebar").removeClass("open");
			$(".sidebar").addClass("close");
			$(".sidebar-content").hide();
		}
		else {
			SIDEBAR_SHOWN = true;
			$(".articles").css("width", "70%");
			$(".toggle-sidebar span").html(">>");
			$(".sidebar").removeClass("close");
			$(".sidebar").addClass("open");
			$(".sidebar-content").show();
		}
	});
});