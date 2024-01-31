/* eslint-disable jsx-a11y/anchor-has-content */
import React from "react";
import "./BookingInfo.css";

function AddressDetails() {

  return (
    <>
      <div className="address-container">
        {/* MAP INTEGRATION */}
          <div className="gmap_canvas">
            <iframe
              title="sdechs-map"
              id="gmap_canvas"
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3620.584509551682!2d67.03905131482233!3d24.8438787520408!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3eb33dd3ea9a02d1%3A0x5130a188a432bda7!2sPakistan%20Railways%20Karachi%20Cantonment%20Station!5e0!3m2!1sen!2s!4v1651216325093!5m2!1sen!2s"
              frameBorder="0"
              scrolling="no"
              marginHeight="0"
              marginWidth="0"
            ></iframe>
            <a href="https://embedgooglemap.net/145/"></a>
          </div>

        {/* ADDRESS INFORMATION */}
        <div className="address-details">
          <h3>
            <i className="fas fa-phone-square-alt"></i> &nbsp; Phone :
          </h3>
          <p>117</p>
          
          <h3>
            <i className="fas fa-map-pin"></i> &nbsp; Address :
          </h3>
          <p>
          Cantt. Station Rd Karachi.
          </p>
          <h3>
            <i className="fas fa-envelope-square"></i> &nbsp; Email :
          </h3>
          <p>minister@railways.gov.pk.</p>
        </div>
      </div>
    </>
  );
}

export default AddressDetails;
