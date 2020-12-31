document.addEventListener('DOMContentLoaded', function() {
	
	const myform = document.querySelector("#body");
	myform.addEventListener("submit", (event) => {
		event.preventDefault();
	const name = document.querySelector('#b_type').value;
	const price = document.querySelector('#b_price').value;
	fetch ('/newbody', {
		method:'POST',
		body:JSON.stringify({
			"body_name": name,
			"body_price": price,
})
})
.then(response => response.json())
.then(result => {
alert("New Body!");

})
})
})


