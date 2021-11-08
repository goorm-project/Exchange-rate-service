import React from "react";
import { useEffect, useState, useRef, useCallback } from "react";
import { COUNTRIES_DATA } from "../data/countries_data";
import HEX_DATA from "../data/countries_hex_data.json";
import Globe from "react-globe.gl";

export default function CustomGlobe( props ) {


const labelsData = [

  { name: "EUROPE",
    lat: 46.227638,
    lng: 2.213749, 
    size: 1, 
    color: "yellow",
    code: "EUR",
    updateDate : props.date,
    ttb : props.eurTtb,
    tts : props.eurTts,
  },
  {
    name: "Canada",
    lat: 56.130366,
    lng: -106.34677099999999,
    size: 1,
    color: "white",
    code: "CAD",
    updateDate : props.date,
    ttb : props.cadTtb,
    tts : props.cadTts,

  },
  {
      name: "Australia",
      lat: -25.274398,
      lng: 133.775136,
      size: 1,
      color: "white",
      code: "AUD",
      updateDate : props.date,
      ttb : props.audTtb,
      tts : props.audTts,

  },
  {
      name: "South Korea",
      lat: 35.907757000000004,
      lng: 127.766922,
      size: 1,
      color: "white",
      code: "WON",
      updateDate : props.date,
      ttb : props.krwTtb,
      tts : props.krwTts,
  },
  {
    name: "Japan",
    lat: 36.204824,
    lng: 138.252924,
    size: 1,
    color: "white",
    code: "JPY(100)",
    updateDate : props.date,
    ttb : props.jpyTtb,
    tts : props.jpyTts,
 },
  {
      name: "China",
      lat: 35.86166,
      lng: 104.195397,
      size: 1,
      color: "white",
      code: "CNY",
      updateDate : props.date,
      ttb : props.cnyTtb,
      tts : props.cnyTts,

  },
  {
      name: "United Kingdom",
      lat: 55.378051,
      lng: -3.435973,
      size: 1,
      color: "white",
      code: "GBP",
      updateDate : props.date,
      ttb : props.gbpTtb,
      tts : props.gbpTts,

  },
  {
      name: "Hong Kong",
      lat: 22.396428,
      lng: 114.109497,
      size: 1,
      color: "white",
      code: "HKD",
      updateDate : props.date,
      ttb : props.hkdTtb,
      tts : props.hkdTts,

  },
  {
      name: "United States",
      lat: 42.813297,
      lng: -106.34677099999999,
      size: 1,
      color: "white",
      code: "USD",
      updateDate : props.date,
      ttb : props.usdTtb,
      tts : props.usdTts,

  },
  {
      name: "United Arab Emirates",
      lat: 23.424076,
      lng: 53.847818,
      size : 1,
      color: "white",
      code: "AED",
      updateDate : props.date,
      ttb : props.aedTtb,
      tts : props.aedTts,

    },
];


  const globeEl = useRef();
  //console.log(COUNTRIES_DATA.findIndex((e) => e.name === "South Korea" )) 39
  const [hex, setHex] = useState({ features: [] });
  useEffect(() => {
    setHex(HEX_DATA);
  }, []);

  useEffect(() => {
    // globeEl.current.controls().autoRotate = true;
    // globeEl.current.controls().autoRotateSpeed = 0.2;
    const kr = COUNTRIES_DATA[39];
    const MAP_CENTER = { lat: kr.latitude, lng: kr.longitude, altitude: 1.5 };
    globeEl.current.pointOfView(MAP_CENTER, 0);
  }, [globeEl]);

  return (
    <div class = 'wrapper' style = {{marginBottom : '20%'}}>
        <div id = 'globe' >
            <Globe 
            ref={globeEl}
            backgroundColor="#000"
            labelsData= {labelsData}
            labelLat={(d) => d.lat}
            labelLng={(d) => d.lng}
            labelText={(d) => d.name}
            labelSize={(d) => 0.5 + d.size}
            labelLabel={(d) => `
            <div>
            <br></br>
            <b>통화 코드 : ${d.code}</b></div>
            <li><b>받으실 때 : ${d.ttb}</b></li>
            <li><b>보내실 때 : ${d.tts}</b></li>
            <li><b>업데이트 날짜 : ${d.updateDate}</b></li>
            <i>자세한 정보를 보시려면 클릭하세요</i>
            `}
            
            labelColor={useCallback(() => "yellow", [])}
            onLabelClick={() => window.open('https://www.koreaexim.go.kr/site/program/financial/exchange?menuid=001001004002001')}
            labelDotRadius={0.4}
            labelAltitude={0.05}
            hexPolygonsData={hex.features}
            hexPolygonResolution={3} //values higher than 3 makes it buggy
            hexPolygonMargin={0.62}
            hexPolygonColor={useCallback(() => "#1b66b1", [])}
            />
        </div>
        
    </div>
  );
}
