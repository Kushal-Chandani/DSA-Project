import React from 'react';
import './Intro.css';

function IntroModal({ open, children, onClose }) {
    if (!open) return null

    return (
        <>
        <div className="overlay-styles"  />
        <div className="modal-styles" >
            <i className="fas fa-window-close" onClick={onClose} ></i>
            {children}
        </div>
        </>
    )
}

export default IntroModal;