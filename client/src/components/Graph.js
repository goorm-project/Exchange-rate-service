import {React} from 'react'

import LineGraph from './LineGraph'


function Graph() 
{  

    return (
        <div id = 'graph' style = {{paddingBottom : '13%', paddingTop : '3%', textAlign : 'center'}}>
            <h1 style = {{color : 'yellow'}}> Chart </h1>
            <p style = {{color : 'yellow'}}>
                차트를 확인하고 싶으신 국가를 선택해 주세요
            </p>

            <div style = {{display : 'flex',justifyContent : 'center'}}> 

            <LineGraph></LineGraph>
            </div>
        </div>

    )
}

export default Graph
