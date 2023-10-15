import React from "react";
import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";

function App() {
	const [file, setFile] = useState();

	const handleFileChange = (e) => {
		if (e.target.files) {
			setFile(e.target.files[0]);
		}
	};

	const handleUploadClick = () => {
		if (!file) {
			return;
		}
		let formData = new FormData();

		formData.append("file", file, file.name);
		// 👇 Uploading the file using the fetch API to the server
		fetch('http://localhost:8000/', {
			method: 'POST',
			body: formData,
			// 👇 Set headers manually for single file upload
			headers: {
				// If you pass the content type it breaks!
				// 	'content-type': "multipart/form-data",
				'content-length': `${file.size}`, // 👈 Headers need to be a string
			},
		})
			.then((res) => res.json())
			.then((data) => console.log(data))
			.catch((err) => console.error(err));
	};

	return (
		<div>
			<input type="file" onChange={handleFileChange} />

			<div>{file && `${file.name} - ${file.type}`}</div>

			<button onClick={handleUploadClick}>Upload</button>
		</div>
	);
}

export default App;
