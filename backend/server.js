const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { exec } = require('child_process');

const app = express();

app.use(cors());
app.use(bodyParser.json());

app.post('/post', async (req, res) => {
    try {
        const data = req.body;
        exec(`python predict_password/predict_password_crack_time.py ${data.password}`, { encoding: "utf-8" }, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error: ${error.message}`);
                return res.send('loi');
            }
            if (stderr) {
                console.error(`Stderr: ${stderr}`);
                return res.send('pending');
            }

            const prediction = stdout.trim();
            res.send("cần " + prediction + " để phá khóa mật khẩu");
        })
    } catch (error) {
        console.log(error)
    }
})

app.listen(5000, () => console.log(`Server đang chạy trên cổng 5000`));