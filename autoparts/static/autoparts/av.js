document.addEventListener('DOMContentLoaded', function() {
	
	const myform = document.querySelector("#av");
	myform.addEventListener("submit", (event) => {
		event.preventDefault();
	const name = document.querySelector('#av_type').value;
	const price = document.querySelector('#av_price').value;
	fetch ('/newav', {
		method:'POST',
		body:JSON.stringify({
			"av_name": name,
			"av_price": price,
})
})
.then(response => response.json())
.then(result => {
alert("New AV!");

})
})
})


