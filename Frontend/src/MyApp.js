import React, {useState} from 'react';
import "./MyApp.css";
import Title from "./Title"

//import axios from 'axios';

//import TextField from '@mui/material/TextField';

//  backend url = https://sealcamdata.herokuapp.com/

function MyApp() {
    const [start, setStart] = useState("");
    const [end, setEnd] = useState("");
    const [email, setEmail] = useState("")
    const [message, setMessage] = useState("");

    const state = {button: 1};

    let handleSubmit = async (e) => {
        e.preventDefault();
        if (state.button === 1)
        {
            try {
            setMessage("Gathering Data...");
            const res = await fetch("https://sealcamdata.herokuapp.com/home", {
                method: "POST",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    start: start,
                    end: end
                })
            });
            const resJson = await res.json();
            if (res.status === 200) {
                setMessage("Success!");
            } else {
                setMessage("Uh oh");
            }
            } catch (err) {
            console.log(err);
            }
        }
        else if (state.button === 2)
        {
            try {
                setMessage("Emailing...");
                const res = await fetch("https://sealcamdata.herokuapp.com/email", {
                    method: "POST",
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        email: email,
                        start: start,
                        end: end
                    })
                });
                const resJson = await res.json();
                if (res.status === 200) {
                    setMessage("Sent!");
                    setStart("");
                    setEnd("");
                } else {
                    setMessage("Uh oh");
                }
                } catch (err) {
                console.log(err);
                }
        }
      };

      return (
        <div className="MyApp">
            <Title />
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
                style={{width: "370px"}}
                />
        
                <button 
                    onClick={() => (state.button = 1)}
                    type="submit"
                    name="Submit"
                    style={{width: "370px"}}
                >Submit
                </button>

                <div className="message">{message ? <p>{message}</p> : null}</div>

                <input
                type="text"
                value={email}
                placeholder="Email"
                onChange={(e) => setEmail(e.target.value)}
                style={{width: "370px"}}
                />
                <button 
                    onClick={() => (state.button = 2)}
                    type="submit"
                    name="Email"
                    style={{width: "370px"}}
                >Email Me!
                </button>
            </form>
            <div className="hyperlink">
            <a href="https://sealcamdata.herokuapp.com/download" rel="noreferrer">
                Download
                </a>
            </div>
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
