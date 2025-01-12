const express = require('express')
const mongoose = require('mongoose')
const cors = require("cors")

require ('dotenv').config()

const app = express()
const PORT = process.env.port || 5000

app.use(express.json())
app.use(cors())

//app.listen(PORT, () => console.log(`listening on ${PORT}`))

mongoose.connect(process.env.MONGODB_URL)
  .then(() => {
    console.log("Connected to database!");
    app.listen(PORT, () => console.log(`listening on ${PORT}`));
  })
  .catch(() => {
    console.log("Connection failed");
  });