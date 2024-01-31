import { Button } from './Button';
import React from 'react';
import "./HeroSection.css";
import '../App.css';
// import video from "../videos/video-1.mp4";
import {Link} from 'react-router-dom';

function HeroSection() {
    return(
         <div className='hero-container'>
             {/* <video src={video} autoPlay loop muted /> */}
             {/* <h1 className="heading-tabdeeli">Tabdeeli Passage</h1> */}
             <div className='hero-btns'>
             <Link to="/contactinfo" className="btn-mobile">
                 <Button className='btns check' buttonStyle='btn-outline' buttonSize='btn-large'>
                     Login and Signup
                     </Button>
                     </Link>
                     <Link to="/bookingform" className="btn-mobile">
                     <Button className='btns' buttonStyle='btn-primary' buttonSize='btn-large'>
                      VIEW TRAIN SCHEDULES <i className='far fa-play-circle' /> 
                     </Button>
                     </Link>

             </div>
         </div>
    )
}   

export default HeroSection;