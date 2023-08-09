import React from "react";
import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";

function App() {
	const [count, setCount] = useState(0);
	const [data, setData] = useState(null);

	useEffect(() => {
		fetch(`http://localhost:8000`)
			.then((response) => {
				return response.json()
			})
			.then((actualData) => {
				console.log({ data: actualData })
				setData(actualData);
			})
	}, []);

	return (
		<div className="App">
			<h1>Bird or Forest?</h1>

			<form>
				<p>Upload a picture of a bird or a forest</p>
				<p>Our very advanced Machine Learning model will tell you if it is a bird or a forest</p>
				<div>
					<label for="file">Choose file to upload</label>
					<input type="file" id="file" name="file" accept="image/png, image/jpeg" />
				</div>
			</form>

			<div class="departures">
				<p><em style={{ fontWeight: "bold" }}>Probability that it is a bird: </em>{data && data.probability}</p>
				<p><em style={{ fontWeight: "bold" }}>It is a </em>{data && data.answer} !</p>
			</div>

		</div>
	);
}

export default App;
