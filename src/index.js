const express = require('express');
const app = express();
const { spawn } = require('child_process');
const scrap = spawn('python', [__dirname + '\\scrapper.py'])

app.set('port', 3000);
app.set('view engine', 'ejs');
//scrapper
scrap.stdout.on('data', (data) => {
    dataString = data.toString();
    dataJson = JSON.parse(dataString);
});

//Routes
app.get('/', (req, res) => {
    res.render(__dirname + '\\views\\index.ejs', { Time: dataJson['Hour'], Price: dataJson['Price'] })
});

//Listen
app.listen(app.get('port'), () => {
    console.log('server on port', app.get('port'))
})