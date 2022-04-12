import React from 'react'
//import TextField from '@mui/material/TextField';

function MyApp() {
   return (
	<div>
        <h1>Seal Cam Data</h1>
	<p> Submit dates for NOAA data </p>
	<label> Start Date </label>
        <input type="date" id="start"/>
	<label> End Date </label>
        <input type="date" id="end"/>
        <input type="submit" value="Submit"/>
	</div>
    );
}

export default MyApp;
