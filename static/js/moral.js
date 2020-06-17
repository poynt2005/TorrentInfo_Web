window.onload = function(){	
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
	
	/**
	 * 送出資料
	*/
	
	var spinner = new Spinner(opts)
	  , target = document.querySelector("body")
	  , isPSending = false
	  , isMSending = false;
	
	document.getElementById("post_f").onchange = async function(){
		var FileName = this.value;	
		if(isPSending) return;

		if(!/.*\.torrent$/.test(FileName))
			alert("It's not a valid torrent file!");
		else{			
			var fd = new FormData(document.querySelector(".form_file_class"));
			
			spinner.spin(target);
			isPSending = !isPSending;
			
			let r = await fetch("/file_process", {
				method: "POST",
				body: fd
			});
			
			r = await r.json();
			
			spinner.spin();
			
			document.getElementById("magnet_result").innerHTML = r.link;
			
			isPSending = !isPSending;
		};
	};
	
	document.getElementById("magnet_text").onchange = async function(){
		let LINK = this.value;
		
		if(isMSending) return;
		
		if(!/^(magnet\:\?xt\=urn\:btih\:).+/.test(LINK))
			alert("It's not a valid magnet link!");
		else{
			let magnet_text = document.getElementById("magnet_text").value;
			
			spinner.spin(target);
			isMSending = !isMSending;
			
			let r = await fetch("/magnet_process", {
				method: "POST",
				body: `magnet_link=${encodeURIComponent(magnet_text)}`
			});
			
			r = await r.text();
			
			spinner.spin();
			
			if(r == "0")
				document.getElementById("torrent_result").innerHTML = "No file found";
			else{
				let file = new Blob([r] , {type : "application/octet-stream"});
				downloadURL = window.URL.createObjectURL(file);
				html_element = `<a href ="${downloadURL}" download = 'YourTorrent.torrent'>Your File is Ready</a>`;
				document.getElementById("torrent_result").innerHTML = html_element;		
			}		
			isMSending = !isMSending;		
		};
	};

	/**
	 * 控制顯示或隱藏的按鈕
	*/
	
	var sleep = sec => new Promise(resolve => setTimeout(resolve ,sec*1000));
	
	async function hide(element, delay=0.75){
		element.classList.remove("fadeInAni");	
		element.classList.add("fadeOutAni");
		await sleep(delay);
		element.classList.remove("visable");
		element.classList.add("hidden");
	}
	async function show(element, delay=0.75){
		element.classList.remove("fadeOutAni");		
		element.classList.add("fadeInAni", "visable");
		await sleep(delay);
		element.classList.remove("hidden");
	}
	
	document.getElementById("file_box").onclick = async function(){
		if(Array.from(document.getElementById("file_form").classList).indexOf("visable") != -1) return;
		await hide(document.getElementById("magnet_form"));
		await show(document.getElementById("file_form"));
	};
	
	document.getElementById("magnet_input").onclick = async function(){	
		if(Array.from(document.getElementById("magnet_form").classList).indexOf("visable") != -1) return;
		await hide(document.getElementById("file_form"));
		await show(document.getElementById("magnet_form"));
	};
}