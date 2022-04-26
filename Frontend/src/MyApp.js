//import React from 'react';
import React, {useState, useEffect, useReducer} from 'react';
//import CORS from 'flask_cors';
//import CORS from 'flask-cors';
import axios from 'axios';
//import TextField from '@mui/material/TextField';

const formReducer = (state, event) => {
        return {
          ...state,
          [event.name]: event.value
        }
       }



async function makePostCall(date){
        try {
           const response = await axios.post('http://localhost:5000/home', date);
           return response;
        }
        catch (error) {
           console.log(error);
           return false;
        }
}
   
/*
function updateList(date) { 
        makePostCall(date).then( result => {
        if (result)
           setData([date]);
        });
     }
*/   
function MyApp() {
   
   //const [data, setData] = useState([{}])
   const [formData, setFormData] = useReducer(formReducer, {});
   const [submitting, setSubmitting] = useState(false);
   
   useEffect(() => {
        fetch("/home").then(
                res => res.json()
        ).then(
                data => {
                        formData(data)
                        console.log(data)
                }
        )
   }, [])

   const handleSubmit = event => {
           event.preventDefault();
           setSubmitting(true);
           setTimeout(() => { setSubmitting(false);}, 3000)
           //alert('You have submitted the dates.')
   }

   const handleChange = event => {
        setFormData({
          name: event.target.name,
          value: event.target.value,
        });
      }

   return (
	<div>
        <h1>Seal Cam Data</h1>
        {submitting &&
            <div>
                You are submitting the following:
                <ul>
                   {Object.entries(formData).map(([name, value]) => (
                      <li key={name}><strong>{name}</strong> {value}</li>,
                      <li key={name}><strong>{name}</strong> {value}</li>
                      ))}
                </ul>
            </div>}
	<p> Submit dates for NOAA data </p>
	<form onSubmit={handleSubmit}>
           <fieldset>
              <label> Start Date </label>
              <input type="date" name="start" onChange={handleChange}/>
	      <label> End Date </label>
              <input type="date" name="end" onChange={handleChange}/>
           </fieldset>
           <button type="submit">Submit</button>
        </form>
	</div>
    );
    /*
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
    */
}

export default MyApp;
