import React from "react";
import "./HeroSectionCI.css";
import train from "../images/train-icon.svg";

function HeroSectionCI() {
  
  
  function scrollWindow() {
    window.scrollBy({top: 600, behavior: "smooth"})
  }

  return (
    <div className="hs-container">
      <div>
        <h1 className="hs-heading">
          Our Services
          <br />
          and info of
          <br />
          Trains.
        </h1>
        <p className="hs-p">
          Need to know more about the services
          <br /> and features we offer. Just give us a
          <br /> call and we will be ready to help you.
        </p>
        <div className="hs-buttons">
          <button onClick={scrollWindow}> Take a Look! </button>
        </div>
      </div>
      <div className="hs-img-container">
        <img src={train} alt="train" className="hs-image" />
      </div>
    </div>
  );
}

export default HeroSectionCI;
