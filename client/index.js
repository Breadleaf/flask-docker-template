document.addEventListener("DOMContentLoaded", function() {
	var form = document.getElementById("nameForm");
	form.onsubmit = function(event) {
		event.preventDefault();
		var name = form.elements["name"].value;
		fetch("/submit", {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify({name: name}),
		})
		.then(response => response.text())
		.then(msg => {
			document.getElementById("response").innerText = msg;
		})
		.catch(error => {
			console.error("Error:", error);
		});
	};
});
