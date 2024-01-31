import React, { useState } from "react";
import img from "../images/trainmaps.jpeg";
import "./Intro.css";
import IntroModal from "./IntroModal";

function Intro() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <div className="intro">
        <h1 className="intro_heading"><i class="fas fa-info-circle"></i> About Us </h1>{" "}
        <div className="intro_container">
          <div>
            <li className="intro_feature"> Introduction </li>{" "}
            <p>
            Pakistan Railways is a public-sector organization, earlier known as the Pakistan Western Railway (1947 to 1974). From 1948, usage of railways increased and the network became profitable. From the year 1950 to 1955, it improved its operations by connecting West and East Pakistan (now Bangladesh).
            </p>{" "}
            <br />
            <hr />
            <br />
            <br />
            <div>
              <li className="intro_feature">Objectives</li>{" "}
              <p className="last-p">
              The core operational activities of Pakistan Railways are to: Provide comfortable and safe travelling facilities to the general public. Cater to the cargo transport needs of general public, Pakistan Army and other government departments at economical tariff rates and within shortest possible time.
              </p>{" "}
              <br />
            <hr />
            </div>{" "}
          </div>{" "}
          <div className="image-div">
            <img
              src={img}
              alt="Intro"
              className="intro_img"
              onClick={() => setIsOpen(true)}
            />{" "}
          </div>{" "}
        </div>{" "}
        <IntroModal open={isOpen} onClose={() => setIsOpen(false)}>
          <img src={img} alt="trainmap" onClick={() => setIsOpen(false)} />{" "}
        </IntroModal>{" "}
      </div>{" "}
    </>
  );
}

export default Intro;
