const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const app = express()
const port = 8000

let dataToSend;

app.use(cors())
app.use(bodyParser.json())
app.route('/calculated')
    .post((req, res) => {
        dataToSend = req.body;

        fetch("http://localhost:7000/calculated", {
            method: "POST",
            mode: "cors",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(dataToSend)
        }).then(received => received.json()).then(message => {
            payload = {
                price: message,
                message: 'post request for calculated page successful'
            }
            res.send(payload)
        });
    })

  app.listen(port, () => {
    console.log(`Server listening on port ${port}`)
  })