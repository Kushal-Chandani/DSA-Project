import React, { useState, useEffect } from 'react'
import '../App.css';
import { useWindowScroll } from 'react-use';

function ScrollToTop() {

    const { y: pageYOffset } = useWindowScroll();
    const [visisble, setVisibility] = useState(false)

    useEffect(() => {
        if(pageYOffset > 400) {
            setVisibility(true)
        }else {
            setVisibility(false)
        }
    }, [pageYOffset])

    if(!visisble) {
        return false;
    }

    const scrollToTop = () => window.scrollTo({ top: 0, behavior: "smooth" })

    return (
        <div className="scroll-to-top cursor-pointer text-center" onClick={ scrollToTop  } >
            <i className="icon fas fa-chevron-up"></i>
        </div>
    )
}

export default ScrollToTop
