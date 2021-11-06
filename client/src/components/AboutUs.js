import React from 'react';
import SimpleImageSlider from "react-simple-image-slider";


const images = [
    { url: 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA4MjJfNDUg%2FMDAxNjI5NjI5NTc2MTgy.PUx9JoPQUVJt-0ok23vJvu6_jkkxQoOlDVTnlUoHkwsg.qu_88Zdj4rXzxsEqyb-nFQ9NCtv8gy5fOIf2dRo-PZgg.JPEG.jyjbono8685%2FKakaoTalk_20210822_195137167_04.jpg&type=a340' },
  ];

function AboutUs() {

    return (
        <div style = {{backgroundColor : '#000'}}>
            <SimpleImageSlider
            width={'45%'}
            height={'80%'}
            images={images}
            showBullets={true}
            showNavs={true}
            />
        </div>

    )
}

export default AboutUs
