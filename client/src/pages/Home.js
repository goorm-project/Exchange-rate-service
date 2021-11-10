import {React, useState, useEffect} from 'react';
import CustomGlobe from '../components/globe';
import SideBar from '../components/SideBar';
import Graph from '../components/Graph'
import ChatBotManual from '../components/ChatBotManual';
import axios from 'axios';




function Home() {
    const [date,setDate] = useState('');

    const [eurTtb, setEurTtb] = useState('');
    const [eurTts, setEurTts] = useState('');

    const [cadTtb, setCadTtb] = useState('');
    const [cadTts, setCadTts] = useState('');

    const [audTtb, setAudTtb] = useState('');
    const [audTts, setAudTts] = useState('');

    const [krwTtb, setKrwTtb] = useState('');
    const [krwTts, setKrwTts] = useState('');

    const [jpyTtb, setJpyTtb] = useState('');
    const [jpyTts, setJpyTts] = useState('');

    const [cnyTtb, setCnyTtb] = useState('');
    const [cnyTts, setCnyTts] = useState('');

    const [gbpTtb, setGbpTtb] = useState('');
    const [gbpTts, setGbpTts] = useState('');

    const [usdTtb, setUsdTtb] = useState('');
    const [usdTts, setUsdTts] = useState('');

    const [hkdTtb, setHkdTtb] = useState('');
    const [hkdTts, setHkdTts] = useState('');

    const [aedTtb, setAedTtb] = useState('');
    const [aedTts, setAedTts] = useState('');

    useEffect(() => {
        axios.get('http://localhost:3100/api/today/eur')
            .then(res => setDate(res.data[0].updateDate))
    },[])

    useEffect(() => {
        axios.get('http://localhost:3100/api/today/eur')
            .then(res => {
                setEurTtb(res.data[1].ttb)
                setEurTts(res.data[1].tts)
            })
    },[])

    useEffect(() => {
        axios.get('http://localhost:3100/api/today/cad')
            .then(res => {
                setCadTtb(res.data[1].ttb)
                setCadTts(res.data[1].tts)
            })
    },[])

    useEffect(() => {
        axios.get('http://localhost:3100/api/today/aud')
            .then(res => {
                setAudTtb(res.data[1].ttb)
                setAudTts(res.data[1].tts)
            })
    },[])


    useEffect(() => {
        axios.get('http://localhost:3100/api/today/cny')
            .then(res => {
                setCnyTtb(res.data[1].ttb)
                setCnyTts(res.data[1].tts)
            })
    },[])


    useEffect(() => {
        axios.get('http://localhost:3100/api/today/krw')
            .then(res => {
                setKrwTtb(res.data[1].ttb)
                setKrwTts(res.data[1].tts)
            })
    },[])


    useEffect(() => {
        axios.get('http://localhost:3100/api/today/jpy_100')
            .then(res => {
                setJpyTtb(res.data[1].ttb)
                setJpyTts(res.data[1].tts)
            })
    },[])


    useEffect(() => {
        axios.get('http://localhost:3100/api/today/usd')
            .then(res => {
                setUsdTtb(res.data[1].ttb)
                setUsdTts(res.data[1].tts)
            })
    },[])


    useEffect(() => {
        axios.get('http://localhost:3100/api/today/gbp')
            .then(res => {
                setGbpTtb(res.data[1].ttb)
                setGbpTts(res.data[1].tts)
            })
    },[])


    useEffect(() => {
        axios.get('http://localhost:3100/api/today/aed')
            .then(res => {
                setAedTtb(res.data[1].ttb)
                setAedTts(res.data[1].tts)
            })
    },[])


    useEffect(() => {
        axios.get('http://localhost:3100/api/today/hkd')
            .then(res => {
                setHkdTtb(res.data[1].ttb)
                setHkdTts(res.data[1].tts)
            })
    },[])


    return (
        <div className = 'wrapper' style = {{backgroundColor : "#000"}}>
            <CustomGlobe 
                date = {date} 
                eurTtb = {eurTtb}
                eurTts = {eurTts}
                gbpTtb = {gbpTtb}
                gbpTts = {gbpTts}
                aedTts = {aedTts} 
                aedTtb = {aedTtb} 
                cnyTts = {cnyTts} 
                cnyTtb = {cnyTtb} 
                hkdTts = {hkdTts} 
                hkdTtb = {hkdTtb} 
                krwTts = {krwTts} 
                krwTtb = {krwTtb} 
                jpyTts = {jpyTts} 
                jpyTtb = {jpyTtb} 
                cadTts = {cadTts} 
                cadTtb = {cadTtb} 
                usdTts = {usdTts} 
                usdTtb = {usdTtb} 
                audTtb = {audTtb} 
                audTts = {audTts} 
             ></CustomGlobe>
            <Graph></Graph>
            <ChatBotManual></ChatBotManual>
            <SideBar></SideBar>


        </div>
    )
};

export default Home
