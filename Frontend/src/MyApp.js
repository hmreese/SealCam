import React, {useState} from 'react';
import "./MyApp.css";
import Title from "./Title"

//import axios from 'axios';

//import TextField from '@mui/material/TextField';

//  backend url = https://sealcamdata.herokuapp.com/

function MyApp() {
    const [start, setStart] = useState("");
    const [end, setEnd] = useState("");
    const [message, setMessage] = useState("");


    let handleSubmit = async (e) => {
        e.preventDefault();
        try {
          const res = await fetch("https://sealcamdata.herokuapp.com/", {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                start: start,
                end: end
            })
          });
          const resJson = await res.json();
          if (res.status === 200) {
            setStart("");
            setEnd("");
            setMessage("Success!");
          } else {
            setMessage("Uh oh");
          }
        } catch (err) {
          console.log(err);
        }
      };

      return (
        <div className="MyApp">
            <div className="Title">
                <h1>SEAL CAM</h1>
                <div className="Title-Subtitle">NOAA Data</div>
            </div>
            <form onSubmit={handleSubmit}>
                <input
                type="date"
                value={start}
                placeholder="Start"
                onChange={(e) => setStart(e.target.value)}
                style={{width: "370px"}}
                />
                <input
                type="date"
                value={end}
                placeholder="End"
                onChange={(e) => setEnd(e.target.value)}
                style={{width: "370px", display: "flex",
                justifyContent: "center",
                alignItems: "center"}}
                />
        
                <button type="submit">Submit</button>
        
                <div className="message">{message ? <p>{message}</p> : null}</div>
            </form>
        </div>
      );

    // return (
    //     <div>
    //         <h1>Seal Cam Data</h1>
    //     <p> Submit dates for NOAA data </p>
    //     <label> Start Date </label>
    //         <input type="date" id="start"/>
    //     <label> End Date </label>
    //         <input type="date" id="end"/>
    //         <input type="submit" value="Submit"/>
    //     </div>
    //     );
    }

export default MyApp;
