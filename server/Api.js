const express = require('express') //express를 설치했기 때문에 가져올 수 있다.
const app = express();
const { Client } = require("pg");
const Query = require('pg').Query
const cors = require('cors');
const Auth = require('./Auth')

const port = 3100;


app.use(cors());

//connect with db
var client = new Client({ 
    user : 'postgres',
    host : Auth,
    database : 'ExchangeRate',
    password : "12341234",
    port : 5432, })

client.connect(err => { 
    if (err) { console.error('connection error', err.stack) }
    else { console.log('success!') }
});


function getToday(){
    var date = new Date();
    var year = date.getFullYear();
    var month = ("0" + (1 + date.getMonth())).slice(-2);
    var day = ("0" + date.getDate()).slice(-2);

    return year + "-" + month + "-" + day;
}


app.get('/api/today/:currencyCode', function(req, res, next) {
    today = '2021-11-04'
    console.log(today)
    console.log(req.params.currencyCode)
    console.log("SELECT * FROM " +req.params.currencyCode+  " WHERE date = '"+today+"'")
    

    const query = new Query("SELECT * FROM " +req.params.currencyCode+  " WHERE date = '"+today+"'");
    client.query(query)
        
    var rows = [];
     rows.push({updateDate : today })
     query.on("row",row=>{
          rows.push(row);
     });
     
     query.on('end', () => 
     { console.log(rows);
       console.log('query done')
       res.send(rows);
       res.status(200).end();
    });
    query.on('error', err => {
         console.error(err.stack)
    });
});


app.listen(port, () => {
    console.log(`listening on port : ${port}`);
});
