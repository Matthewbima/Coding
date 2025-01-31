const express = require('express')
const app = express()
const mongoose = require('mongoose')
const session = require('express-session')
const User = require('./models/User')

const mongoURI = "mongodb+srv://admin:admin@cluster0.8uh3h.mongodb.net/Cluster0"

app.use(express.urlencoded({
    extended: false,
}))

// useNewUrlParser have to be true because there has been some updates to mongoose
mongoose.connect(mongoURI , { useNewUrlParser: true }).then(() => console.log('MongoDB Connected')).catch(err => console.log(err));

app.set('view engine', 'ejs')

app.get('/', (req, res) => res.render('home'))

app.get('/register', (req, res) => res.render('register'))

app.get('/login', (req, res) => res.render('login'))

app.post('/register', (req, res) => {
    const name = req.body.name
    const email = req.body.email
    const password = req.body.password

    let msg = ""

    if (!name || !email || !password) {
        msg = "Please fill in all the fields!"
        res.render('register', {msg})
    } else {
        User.findOne({email: email})
        .then(user => {
            if(user) {
                msg = "Email already used!"
                res.render('register', {msg})
            } else {
                const newuser = new User({
                    name: name,
                    email: email,
                    password: password,
                })

                User.create(newuser, (err, data) => {
                    msg = "Account created! Please login"
                    res.render('login', {msg})
                })
            }
        })
    }
})

app.listen(5001)
console.log('Listening on port 5001')