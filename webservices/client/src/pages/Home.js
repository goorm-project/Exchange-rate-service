import {React} from 'react';
import CustomGlobe from '../components/globe';
import SideBar from '../components/SideBar';
import Graph from '../components/Graph'
import ChatBotManual from '../components/ChatBotManual';
import CurrencyConverter from '../components/CurrencyConverter';





function Home() {
    return (
        <div className = 'wrapper' style = {{backgroundColor : "#000", color : 'white'}}>
            <CustomGlobe 
                color = {'white'}
                size = {1}            ></CustomGlobe>
            <Graph></Graph>
            <ChatBotManual></ChatBotManual>
            <CurrencyConverter></CurrencyConverter>
            <SideBar></SideBar>


        </div>
    )
};

export default Home
