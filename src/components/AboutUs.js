import React from 'react';
import SimpleImageSlider from "react-simple-image-slider";
import prcimg1 from '../data/images/process_1.jpg'
import prcimg2 from '../data/images/process_2.jpg'
import prcimg3 from '../data/images/process_3.jpg'
import prcimg4 from '../data/images/process_4.jpg'
import prcimg5 from '../data/images/process_5.jpg'
import prcimg6 from '../data/images/process_6.jpg'
import allProcessInOne from '../data/images/allProcessInOne.jpg'

const images = [
    { src: {prcimg1} },
    { src: {prcimg2} },
    { url: 'C:/Users/Lenovo/OneDrive/바탕 화면/ikuzo/client/src/data/images/process_1.jpg' },
    { url: '../data/images/process_4.jpg' },
    { url: "images/5.jpg" },
    { url: "images/6.jpg" },
    { url: "images/7.jpg" },
  ];

function AboutUs() {

    return (
        <div>
            <SimpleImageSlider
            width={896}
            height={504}
            images={images}
            showBullets={true}
            showNavs={true}
            />
        </div>

    )
}

export default AboutUs
