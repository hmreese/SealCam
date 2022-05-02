import React from 'react'
import './Title.css';
import logo from './seal.png'

//https://makeschool.org/mediabook/oa/tutorials/react-fundamentals-vm0/build-a-header-component/
//https://projects.animaapp.com/

function Title() {
  return (
    <div classname="Title">
        <div className="overlap-group">
            <div className="seal-container">
                <img className="seal-1" src={logo} />
                <div className="seal-cam valign-text-middle hammersmithone-normal-white-24px">
                    <span>
                        <span className="hammersmithone-normal-white-24px">Seal Cam</span>
                    </span>
                </div>
            </div>
            <h1 classname="title valign-text-middle hammersmithone-normal-white-45px">
                <span>
                    <span className="hammersmithone-normal-white-45px">NOAA Data Download</span>
                </span>
            </h1>
        </div>
    </div>
  );
}

export default Title