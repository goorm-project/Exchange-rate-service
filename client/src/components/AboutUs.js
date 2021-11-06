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
        <div id = 'wrapper' style = {{backgroundColor : '#000' , color : 'yellow', textAlign : 'center', paddingBottom : '20%'}}>

            <h1 id = 'aboutUs'>
                About Us
            </h1>
            <p>
                저희는 텔레그램 챗봇 서비스 역시 제공하고 있습니다. 아래에 텔레그램 챗봇 이용 방법이 정의되어있습니다.
            </p>

            <div style = {{display : 'flex',justifyContent : 'center'}}>
                <SimpleImageSlider
                width={'550px'}
                height={'450px'}
                images={images}
                showBullets={true}
                showNavs={true}
                navSize='100'
                />
            </div>

        </div>

    )
}

export default AboutUs
