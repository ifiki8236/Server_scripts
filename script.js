// const url = 'http://127.0.0.1:8080'; // Replace with your server URL
// const url_2 = 'http://127.0.0.1:8080/applicants';
// const requestData = {
//   method: 'POST', // HTTP method (GET, POST, PUT, DELETE, etc.)
//   headers: {
//     'Content-Type': 'application/json', // Set the content type of the request body
//   },
//   body: JSON.stringify({name: 'john jones', number: '123456', address: '999 west street park' }), // Convert data to JSON string
// };

// console.log('Script running...')

// function fetchData() {
//     fetch(url)
//     .then(response => {
//         if (!response.ok) {
//         throw new Error('Request failed'); // Handle non-OK responses
//         }
//         return response.json(); // Parse response body as JSON
//     })
//     .then(data => {
//         console.log('Response data:', data); // Handle the parsed response data
//     })
//     .catch(error => {
//         console.error('Error:', error); // Handle errors during the request
//     });
// }

// function postData() {
//     fetch(url_2, requestData)
//     .then(response => {
//         if (!response.ok) {
//         throw new Error('Request failed'); // Handle non-OK responses
//         }
//         return response.json(); // Parse response body as JSON
//     })
//     .then(data => {
//         console.log('Response data:', data); // Handle the parsed response data
//     })
//     .catch(error => {
//         console.error('Error:', error); // Handle errors during the request
//     });
// }
// setInterval(postData, 10000);
// setInterval(fetchData, 20000); // Adjust the interval as needed
