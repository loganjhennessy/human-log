function submitLog() {
	now = Date.now();
	logData = document.getElementById('log-input').value;

	console.log(logData);
	console.log(now)

	data = {
		ts: now,
		note: logData	
	};

	$.post("/note", data, function(data, status){
		console.log(`Status: ${status}`)
	})
}
