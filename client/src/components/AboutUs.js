import React from 'react';
import SimpleImageSlider from "react-simple-image-slider";


const images = [
    { url: 'https://github.com/LEEDOWON96/goorm-proj/blob/main/client/src/data/images/pr_1.jpg?raw=true' },
    { url: 'https://github.com/LEEDOWON96/goorm-proj/blob/main/client/src/data/images/pr_2.jpg?raw=true' },
    { url: 'https://github.com/LEEDOWON96/goorm-proj/blob/main/client/src/data/images/pr_3.jpg?raw=true' },
    { url: 'https://github.com/LEEDOWON96/goorm-proj/blob/main/client/src/data/images/pr_4.jpg?raw=true' },
    { url: 'https://github.com/LEEDOWON96/goorm-proj/blob/main/client/src/data/images/pr_5.jpg?raw=true' },
    { url: 'https://github.com/LEEDOWON96/goorm-proj/blob/main/client/src/data/images/pr_6.jpg?raw=true' },
];

function AboutUs() {

    return (
        <div id = 'wrapper' style = {{backgroundColor : '#000'}}>

            <div id = 'aboutUs' style = {{marginLeft: '25%'}}>
                <SimpleImageSlider
                width={'50%'}
                height={'80%'}
                images={images}
                showBullets={true}
                showNavs={true}
                />
            </div>

        </div>

    )
}

export default AboutUs
