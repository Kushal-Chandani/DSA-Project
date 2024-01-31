import '../../App.css';
import Cards from '../Cards';
import HeroSection from '../HeroSection';
import Footer from '../Footer';
import Intro from '../Intro';
import ScrollToTop from '../ScrollToTop';

function Home() {
    return(
        <>
        <HeroSection />
        <Intro />
        <Cards />
        <Footer />
        <ScrollToTop />
        </>
    )
}

export default Home;