const express = require('express') //express를 설치했기 때문에 가져올 수 있다.
const app = express();
const { Client } = require("pg");
const Query = require('pg').Query
const cors = require('cors');
const Auth = 'database-2.cunn3lppmlk9.ap-northeast-2.rds.amazonaws.com'
const PORT = 3100;
const HOST = 'localhost';

app.use(cors('localhost://3000'));

//connect with db
var client = new Client({ 
    user : 'postgres',
    host : Auth,
    database : "ExchangeRate",
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

    today = getToday()      
    const query = new Query("SELECT * FROM (SELECT * , '" +req.params.currencyCode+ "' as cnt FROM "+ req.params.currencyCode +" ORDER BY date DESC LIMIT 1) as temp, country as c" + " WHERE temp.cnt = lower(c.code)");
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


//그래프 출력 위한 alltime API
app.get('/api/alltime/:currencyCode', function(req, res, next) {
    
    const query = new Query("SELECT DISTINCT * FROM " +req.params.currencyCode+ " ORDER BY date");
    client.query(query)
    
    var rows = [];
    query.on("row",row=>{
          rows.push(row);
     });

    query.on('end', () => 
     {        
       console.log(rows);
       console.log('query done')
       res.send(rows);
       res.status(200).end();

    });

    query.on('error', err => {
         console.error(err.stack)
    });

});


app.get('/api/countrydata', function(req, res, next) {
    
    const query = new Query("SELECT * FROM country ");
    client.query(query)
    
    var rows = [];
    query.on("row",row=>{
          rows.push(row);
     });

    query.on('end', () => 
     {        
       console.log(rows);
       console.log('query done')
       res.send(rows);
       res.status(200).end();

    });

    query.on('error', err => {
         console.error(err.stack)
    });

});

app.listen(PORT, HOST,() => {
    console.log(`Running on http://${HOST}:${PORT}`);
});
