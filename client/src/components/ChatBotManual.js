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

function ChatBotManual() {

    return (
        <div id = 'wrapper' style = {{backgroundColor : '#000' , color : 'yellow', textAlign : 'center', paddingBottom : '15%'}}>

            <h1 id = 'chatBotManual'>
                Chat Bot 사용 설명서
            </h1>
            <p style = {{paddingBottom : '3%'}}> 
                저희는 텔레그램 챗봇 서비스 역시 제공하고 있습니다.<br></br>
                주기적인 알림, 원터치 환율 알림 등 다양한 서비스를 사용해보세요!

            </p>

            <div style = {{display : 'flex',justifyContent : 'center',objectFit:'cover'}}>
                <SimpleImageSlider
                width={'590px'}
                height={'450px'}
                images={images}
                showBullets={true}
                showNavs={true}
                navSize='50'
                />
            </div>

        </div>

    )
}

export default ChatBotManual
