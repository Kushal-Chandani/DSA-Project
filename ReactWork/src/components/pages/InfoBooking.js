import React from 'react';
import '../../App.css';
import AddressDetails from '../AddressDetails';
import '../BookingInfo.css';
import Footer from '../Footer';
import HeroSectionCI from '../HeroSectionCI';
import ScrollToTop from '../ScrollToTop';
import BookingForm from '../BookingForm';

export default function BookingInfo() {
    return(
        <div className="bookinginfo">
            <BookingForm />
            <HeroSectionCI />
            <AddressDetails />
            <Footer />
            <ScrollToTop />  
        </div>
    )
}