function submitLog() {
	now = Date.now();
	logData = $("#log-input").val();

	console.log(logData);
	console.log(now);

	data = {
		ts: now,
		note: logData	
	};

	$.post("/note", data, function(data, status){
		console.log(`Status: ${status}`)
	});

	$("#log-input").val("");
	$("#log-input").attr("placeholder", "Log something else...")
}
