String.prototype.format = function(){
	let s = this;
	let i = arguments.length;
	while(i--){
		let re = new RegExp("\\{" + i + "\\}" , "gm");
		s = s.replace(re , arguments[i]);
	}
	return s;
};

$(document).ready(function(){
	
	//spinner 
	var opts = {
		  lines: 13 // The number of lines to draw
		, length: 28 // The length of each line
		, width: 14 // The line thickness
		, radius: 42 // The radius of the inner circle
		, scale: 1 // Scales overall size of the spinner
		, corners: 1 // Corner roundness (0..1)
		, color: '#000' // #rgb or #rrggbb or array of colors
		, opacity: 0.25 // Opacity of the lines
		, rotate: 0 // The rotation offset
		, direction: 1 // 1: clockwise, -1: counterclockwise
		, speed: 1 // Rounds per second
		, trail: 60 // Afterglow percentage
		, fps: 20 // Frames per second when using setTimeout() as a fallback for CSS
		, zIndex: 2e9 // The z-index (defaults to 2000000000)
		, className: 'spinner' // The CSS class to assign to the spinner
		, top: '50%' // Top position relative to parent
		, left: '50%' // Left position relative to parent
		, shadow: false // Whether to render a shadow
		, hwaccel: false // Whether to use hardware acceleration
		, position: 'absolute' // Element positioning
	};
	//spinner target
	var spinner = new Spinner(opts);
	var target = $("body").get(0);
	
	
	$("#post_f").change(function(){
		let FileName = $(this).val()
		
		let re = RegExp(".*\.torrent$");
		let result = re.test(FileName);
		if(!result)
			alert("It's not a valid torrent file!");
		else{
			
			var fd = new FormData($(".form_file_class")[0]);    
			
			
			$.ajax({
				type : "POST",
				data : fd,
				url : "/file_process",
				processData: false,
				contentType: false,
				beforeSend : function () {
						spinner.spin(target);                    
				},
				success: function(data) {
					spinner.spin();
					$("#magnet_result").html(data.link);
				},
			});
			
		};
	});
	
	$("#magnet_text").change(function(){
		let LINK = $(this).val();
		let re = new RegExp("^(magnet\:\\?xt\=urn\:btih\:).+");
		let result = re.test(LINK);
		if(!result)
			alert("It's not a valid magnet link!");
		else{
			
				let form_data = $("#magnet_form");
				
				$.ajax({
					type : "POST",
					data : form_data.serialize(),
					url : "/magnet_process",
					
					beforeSend : function () {
						spinner.spin(target);                    
					},
					
					success: function(data){
						if(data == "0"){
							spinner.spin();
							$("#torrent_result").html("No file found");
						}
						else{
							let file = new Blob([data] , {type : "application/octet-stream"});
							downloadURL = window.URL.createObjectURL(file);
							html_element = "<a href ='{0}' download = 'YourTorrent.torrent'>Your File is Ready</a>".format(downloadURL);
							spinner.spin();
							$("#torrent_result").html(html_element);
						}
					},
			
				});
				
				/*("#magnet_form").submit();*/
			
		};
	});
	
	
	$("#file_box").click(function (){
			$("#magnet_form").hide("slow");
			$("#file_form").show("slow");
	})
	
	$("#magnet_input").click(function (){
			$("#file_form").hide("slow");
			$("#magnet_form").show("slow");
	})
	
})