import React from 'react'
import { Link as Scroll } from 'react-scroll';


function StickySideBar() {

    const linkStyle ={
        top:0,
        fontSize: '1.3rem',
        position: 'fixed',
        zIndex: '1',
        marginBottom : '0.3rem',
        cursor : 'pointer',
    }

    return (

        <div style={{...linkStyle, backgroundColor : '#000', color:'white', paddingBottom : '0.3rem ='}}>
            <Scroll
                to="globe"
                smooth={true}
                duration={600}
            >
                Globe
            </Scroll>
            <br></br>
    
            <Scroll
                to="graph"
                smooth={true}
                duration={600}
            >
                Chart
            </Scroll>
            <br></br>
            <Scroll
                to="chatBotManual"
                smooth={true}
                duration={600}
            >
               Chat Bot Manual
            </Scroll>
            <br></br>
            <Scroll
                to="converter"
                smooth={true}
                duration={600}
            >
               Currency Converter
            </Scroll>
        </div>
    )
}

export default StickySideBar


