import {React, useState, useEffect} from 'react';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
} from 'recharts';
import axios from 'axios';
import ComboBox from './ComboBoxForChart';


function LineGraph() {

    const [targetCountry, setTargetCountry] = useState('aed')
    
    const getTargetCountry = (country) => {
        setTargetCountry(country);
    }
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://k8s-eksweb-backendi-e94dfcbac2-406838544.ap-northeast-2.elb.amazonaws.com/api/alltime/ '+targetCountry.toLowerCase())
        .then(res => {
            const temp = res.data
            temp.map((day) => {
                return day.date = day.date.slice(0,10)
            })
            setData(temp)
        })
    },[targetCountry])



    return (

        <div style = {{display : 'flex',justifyContent : 'center',tableLayout : 'fixed'}}>
        <div style = {{width : '210px'}}>
        <ComboBox 
            getTargetCountry = {getTargetCountry}>
        </ComboBox>
        </div>

        <LineChart
            style = {{color : '#000'}}

            width={900}
            height={550}
            data={data}
            margin={{
            top: 5, right: 30, left: 20, bottom: 5,
            }}
        >
            <CartesianGrid strokeDasharray="" />
            <XAxis dataKey="date" />
            <YAxis domain={['dataMin' , 'dataMax']} padding={{ top: 10, bottom : 10}} />
            <Tooltip />
            <Legend align = "left" iconSize = {28} height = {1}/>
            <Line type="monotone" dataKey="ttb" stroke="#8884d8" strokeWidth={3}/>
            <Line type="monotone" dataKey="tts" stroke="#82ca9d" strokeWidth={3}/>
        </LineChart>
        </div>
    )
}

export default LineGraph
