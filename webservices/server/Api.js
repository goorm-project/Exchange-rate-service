const express = require('express')
const app = express();
const { Client } = require("pg");
const cors = require('cors');

const EndPoint = 'database-2.cunn3lppmlk9.ap-northeast-2.rds.amazonaws.com'
const PORT = 3100;
const HOST = 'localhost';
const OriginURL = 'localhost://3000'

app.use(cors(OriginURL));

//connect with db
var client = new Client({ 
    user : 'postgres',
    host : EndPoint,
    database : "ExchangeRate",
    password : "12341234",
    port : 5432, })

client.connect(err => { 
    if (err) { console.error('connection error', err.stack) }
    else { console.log('success!') }
});

//get what date is it today
function getToday(){
    var date = new Date();
    var year = date.getFullYear();
    var month = ("0" + (1 + date.getMonth())).slice(-2);
    var day = ("0" + date.getDate()).slice(-2);
    return `${year}-${month}-${day}`;
}

app.get('/api/today/:currencyCode', (req, res) => {
    today = getToday()      
    const query = `SELECT * FROM (SELECT * , '${req.params.currencyCode}' as cnt FROM ${req.params.currencyCode} ORDER BY date DESC LIMIT 1) as temp, country as c WHERE temp.cnt = lower(c.code);`

    client.query(query, (err,result) => {
        if(err) {
            console.log(err.stack);
        } else {
            let row = result.rows[0];
            res.send(row)
            res.status(200).end();
        }
    })
});


//그래프 출력 위한 alltime API
app.get('/api/alltime/:currencyCode', (req, res) => {
    
    const query = `SELECT DISTINCT * FROM ${req.params.currencyCode} ORDER BY date`;
    client.query(query, (err,result) => {
        if(err) {
            console.log(err.stack);
        } else {
            let row = result.rows;
            res.send(row)
            res.status(200).end();
        }
    })

});

app.listen(PORT, HOST,() => {
    console.log(`Running on http://${HOST}:${PORT}`);
});
