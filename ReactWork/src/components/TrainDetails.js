import React from 'react';

const TrainDetails = () => {
  var city1 = "Karachi"
  var city2 = "Islamabad"
  return (
    <div>
      <div>
      <p>Source: </p><p>Karachi</p>
      </div>
      <br/>
      <div>
      <p>Destination: </p><p>Islamabad</p>
      </div>
      <br/>
      <input type="button" value="Book?"/>
    </div>
  )
}

export default TrainDetails