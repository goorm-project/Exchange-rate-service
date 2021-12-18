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

app.get('/api/today/:currencyCode', (req, res) => {  
    const query = `SELECT * 
                    FROM (SELECT  * , '${req.params.currencyCode}' as country
                        FROM  ${req.params.currencyCode}
                        WHERE date = ( SELECT MAX(date)
                                        FROM  ${req.params.currencyCode})) as temp, country as c 
                    WHERE temp.country = lower(c.code);`

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
    
    const query = `SELECT * FROM ${req.params.currencyCode}`;
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
