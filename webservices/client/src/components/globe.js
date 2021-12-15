import React from "react";
import { useEffect, useState, useRef, useCallback } from "react";
import { COUNTRIES_DATA } from "../data/countries_data";
import HEX_DATA from "../data/countries_hex_data.json";
import Globe from "react-globe.gl";
import axios from "axios";

export default function CustomGlobe( props ) {

  const [eur,setEur] = useState('');
  const [cad,setCad] = useState({});
  const [aud,setAud] = useState({});
  const [krw,setKrw] = useState({});
  const [jpy,setJpy] = useState({});
  const [cny,setCny] = useState({});
  const [gbp,setGbp] = useState({});
  const [usd,setUsd] = useState({});
  const [hkd,setHkd] = useState({});
  const [aed,setAed] = useState({});

  useEffect(() => {
      axios.get('http://localhost:3100/api/today/eur')
          .then(res => {
            setEur(res.data)
          })
      axios.get('http://localhost:3100/api/today/cad')
          .then(res => {
              setCad(res.data)
          })
      axios.get('http://localhost:3100/api/today/aud')
          .then(res => {
              setAud(res.data)
          })
      axios.get('http://localhost:3100/api/today/cny')
          .then(res => {
              setCny(res.data)
          })
      axios.get('http://localhost:3100/api/today/krw')
          .then(res => {
              setKrw(res.data)
          })
      axios.get('http://localhost:3100/api/today/jpy_100')
          .then(res => {
              setJpy(res.data)
          })
      axios.get('http://localhost:3100/api/today/usd')
          .then(res => {
              setUsd(res.data)
          })
      axios.get('http://localhost:3100/api/today/gbp')
        .then(res => {
            setGbp(res.data)
        })
      axios.get('http://localhost:3100/api/today/aed')
        .then(res => {
            setAed(res.data)
        })
      axios.get('http://localhost:3100/api/today/hkd')
        .then(res => {
            setHkd(res.data)
        })
  },[])

const labelsData = [

  { name: eur.name,
    lat: eur.lat,
    lng: eur.lng, 
    size: props.size, 
    color: props.color,
    code: eur.code,
    updateDate : String(eur.date).slice(0,10),
    ttb : eur.ttb,
    tts : eur.tts,
  },
  {
    name: cad.name,
    lat: cad.lat,
    lng: cad.lng,
    size: props.size,
    color: props.color,
    code: cad.code,
    updateDate : String(cad.date).slice(0,10),
    ttb : cad.ttb,
    tts : cad.tts,

  },
  {
      name: aud.name,
      lat: aud.lat,
      lng: aud.lng,
      size: props.size,
      color: props.color,
      code: aud.code,
      updateDate : String(aud.date).slice(0,10),
      ttb : aud.ttb,
      tts : aud.tts,

  },
  {
      name: krw.name,
      lat: krw.lat,
      lng: krw.lng,
      size: props.size,
      color: props.color,
      code: krw.code,
      updateDate : String(krw.date).slice(0,10),
      ttb : krw.ttb,
      tts : krw.tts,
  },
  {
    name: jpy.name,
    lat: jpy.lat,
    lng: jpy.lng,
    size: props.size,
    color: props.color,
    code: jpy.code,
    updateDate : String(jpy.date).slice(0,10),
    ttb : jpy.ttb,
    tts : jpy.tts,
 },
  {
      name: cny.name,
      lat: cny.lat,
      lng: cny.lng,
      size: props.size,
      color: props.color,
      code: cny.code,
      updateDate : String(cny.date).slice(0,10),
      ttb : cny.ttb,
      tts : cny.tts,

  },
  {
      name: gbp.name,
      lat: gbp.lat,
      lng: gbp.lng,
      size: props.size,
      color: props.color,
      code: gbp.code,
      updateDate : String(gbp.date).slice(0,10),
      ttb : gbp.ttb,
      tts : gbp.tts,

  },
  {
      name: hkd.name,
      lat: hkd.lat,
      lng: hkd.lng,
      size: props.size,
      color: props.color,
      code: hkd.code,
      updateDate : String(hkd.date).slice(0,10),
      ttb : hkd.ttb,
      tts : hkd.tts,

  },
  {
      name: usd.name,
      lat: usd.lat,
      lng: usd.lng,
      size: props.size,
      color: props.color,
      code: usd.code,
      updateDate : String(usd.date).slice(0,10),
      ttb : usd.ttb,
      tts : usd.tts,

  },
  {
      name: aed.name,
      lat: aed.lat,
      lng: aed.lng,
      size : props.size,
      color: props.color,
      code: aed.code,
      updateDate : String(aed.date).slice(0,10),
      ttb : aed.ttb,
      tts : aed.tts,

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
            
            labelColor={useCallback(() => "white", [])}
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
