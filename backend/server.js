const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();

app.use(cors());
app.use(bodyParser.json());

app.post('/post', async (req, res) => {
    try {
        console.log(req.body);
        const data = req.body;
        res.send(data.password);
    } catch (error) {
        console.log(error)
    }
})

app.listen(5000, () => console.log(`Server đang chạy trên cổng 5000`));