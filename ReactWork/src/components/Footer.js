import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';
import { Button } from './Button';

function Footer() {
    return (
        <div className="footer-container">
            <section className="footer-subscription">
                <p className="footer-subscription-heading">Tabdeeli Passage</p>
                <p className="footer-subscription-text">Unsubscribe</p>
                <div className="input-areas">
                    <form>
                        <input type="email" name="email" 
                        placeholder="Your Email" 
                        className="footer-input" />
                        <Button buttonStyle="btn-outline">Subscribe</Button>
                    </form>
                </div>
            </section>
            <div className="footer-links">
                <div className="footer-link-wrapper">
                    <div className="footer-link-items">
                        <h2>Contact Us</h2>
                        <Link to="">How it works</Link>
                        <Link to="/services">Testimonials</Link>
                        <Link to="/gallery">Terms of Service</Link>
                    </div>
                    <div className="footer-link-items">
                        <h2>Social Media</h2>
                        <Link to="/sign-up">Facebook</Link>
                        <Link to="/services">Instagram</Link>
                        <Link to="/gallery">Twitter</Link>
                    </div>
                </div>
            </div>
            <section className="social-media">
                <div className="social-media-wrap">
                    <div className="footer-logo">
                        <Link to="/" className="social-logo">
                            Tabdeeli Passage
                        </Link>
                    </div>
                    <small className="website-rights">Tabdeeli Passage © 2020</small>
                    <div className='social-icons'>
                        <Link className="social-icon-link facebook" 
                        to="/"
                        target="_blank"
                        aria-label="Facebook"
                        >
                            <i className="fab fa-facebook" />
                        </Link>
                        <Link className="social-icon-link instagram" 
                        to="/"
                        target="_blank"
                        aria-label="Instagram"
                        >
                            <i className="fab fa-instagram" />
                        </Link>
                        <Link className="social-icon-link twitter" 
                        to="/"
                        target="_blank"
                        aria-label="Twitter"
                        >
                            <i className="fab fa-twitter" />
                        </Link>
                    </div>
                </div>
            </section>
        </div>
    )
}

export default Footer