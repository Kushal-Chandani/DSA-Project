import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './components/pages/Home';
// import SignUp from './components/pages/Signup';
import BookingInfo from './components/pages/InfoBooking';
import TrainDetails from './components/TrainDetails';

function App() {
  return (
  <Router>
      <Navbar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/bookinginfo" component={BookingInfo} />
        {/* <Route path="/sign-up" component={SignUp} /> */}
        <Route path="/trainsavailable" component={TrainDetails} />
      </Switch>
      </Router>
  );
}

export default App;
