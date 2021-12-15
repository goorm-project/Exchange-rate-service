import {React,useEffect,useState} from 'react'
import axios from 'axios';
import ComboBox from './ComboBox';

function CurrencyConverter() {

    const [fromCountry, setFromCountry] = useState('___')
    const [toCountry, setToCountry] = useState('___')
    const [fromRate, setFromRate] = useState('')
    const [toRate, setToRate] = useState('')
    const [userInput, setUserInput] = useState(0)
    

    const getFromCountry = (country) => {
        setFromCountry(country);        
    }

    const getToCountry = (country) => {
        setToCountry(country);
    }

    useEffect(() => {
        axios.get('http://localhost:3100/api/today/'+fromCountry.toLowerCase())
            .then(res => {
                if(fromCountry==='JPY_100'){
                    let temp = (res.data[1].deal_bas_r)/100
                    setFromRate(temp)
                }else{
                setFromRate(res.data[1].deal_bas_r)
                }
            })
    },[fromCountry])

    useEffect(() => {
        axios.get('http://localhost:3100/api/today/'+toCountry.toLowerCase())
            .then(res => {
                if(toCountry==='JPY_100'){
                    let temp = (res.data[1].deal_bas_r)/100
                    setToRate(temp)
                }else{
                setToRate(res.data[1].deal_bas_r)
                }
            })
    },[toCountry])

    function calculator (from, to, userInput) {
        let result = '___';

        if(from !== ''){
            result = parseFloat((to/from) * userInput).toFixed(3);
        }
        return result
    }

    function isJPY (country){
        if(country === 'JPY_100'){
            return 'JPY'
        }else{
            return country
        }
    }


    return (
        <div id = 'converter' style = {{textAlign : 'center', paddingBottom : '15%'}}>
            <h1 >환전 금액 계산기
            </h1>
            <p style = {{paddingTop : '2rem',paddingBottom : '3rem'}}>
                매매기준율을 기준으로 환전 예상 금액을 알려드립니다. 수수료를 포함하지 않은 금액입니다.
            </p>

            <div id = 'to_combobox' style = {{color:'#000', display : 'flex', justifyContent : 'center',  paddingBottom : '2rem'}}>
                <span style = {{color:'white', paddingRight : '4rem'}}>1. <span style = {{fontSize : '1.4rem'}}>환전</span>하실 화폐의 사용국가를 선택하세요!</span>
                <div style = {{width : '210px'}}>
                <ComboBox
                    getTargetCountry = {getToCountry}>
                </ComboBox>
                </div>
            </div>

            <div id = 'from_combobox' style = {{color:'#000', display : 'inline-flex', justifyContent : 'space-between', paddingBottom : '2rem'}}>
                <span style = {{color:'white' ,paddingRight : '4rem'}}>2. <span style = {{fontSize : '1.4rem'}}>보유</span>하신 화폐의 사용국가를 선택하세요!</span>
                <div style = {{width : '210px'}}>
                <ComboBox
  
                    getTargetCountry = {getFromCountry}>
                </ComboBox>
                </div>
            </div>

            <div>
                <p>
                    환전하실 화폐는 <span style = {{fontSize : '1.7rem'}}>{isJPY(toCountry)}</span> 이며,
                    보유하신 화폐는 <span style = {{fontSize : '1.7rem'}}>{isJPY(fromCountry)}</span> 입니다. 
                </p>
                <p>
                    <input
                        style = {{textAlign : 'center'}}
                        placeholder = '환전 금액을 입력하세요'
                        onChange={e => setUserInput(e.target.value)}
                    > 
                    </input> {isJPY(toCountry)} 는 {calculator(fromRate,toRate,userInput)} {isJPY(fromCountry)}입니다.
                </p>

            </div>

        </div>
    )
}


export default CurrencyConverter
