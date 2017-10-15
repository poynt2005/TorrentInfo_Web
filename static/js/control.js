$(document).ready(function(){
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
				success: function(data) {
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
			$("#magnet_form").submit();
		}
	})
	
	
	$("#file_box").click(function (){
			$("#magnet_form").hide("slow");
			$("#file_form").show("slow");
	})
	
	$("#magnet_input").click(function (){
			$("#file_form").hide("slow");
			$("#magnet_form").show("slow");
	})
	
})