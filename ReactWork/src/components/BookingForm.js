import React from "react";
import "./BookingForm.css";
import { Link } from 'react-router-dom';

const BookingForm = () => {

  return (
    <div className="main-booking">
      <h2 className="heading-booking">Search For Train Tickets</h2>
      <select name="source" id="source" form="bookingform">
        <option value="departure">Select Departure</option>
        <option value="karachi">Karachi</option>
        <option value="lahore">Lahore</option>
        <option value="islamabad">Islamabad</option>
      </select>
      <select name="destination" id="destination" form="destination">
        <option value="arrival">Select Arrival</option>
        <option value="karachi">Karachi</option>
        <option value="lahore">Lahore</option>
        <option value="islamabad">Islamabad</option>
      </select>
      <input className="text-fields" type="text" placeholder="Enter Your CNIC Number" />
      <input className="text-fields" type="number" placeholder="Enter Your Phone Number" />
      
      
      <Link to="/trainsavailable"><input type="button" value="Submit" className="submitbutton" /></Link>
     

    </div>
  );
};

export default BookingForm;
