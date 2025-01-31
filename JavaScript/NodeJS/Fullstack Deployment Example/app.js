const express = require('express')
const app = express()
const mongoose = require('mongoose')
const session = require('express-session')
const User = require('./models/User')
const Post = require('./models/Post')

const mongoURI = "mongodb+srv://admin:admin@blog.r7pcv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

app.use(session({secret: "secret"}));

// ADD THIS TO ENABLE SESSION
app.use(express.urlencoded({
    extended: false
}))

mongoose.connect(mongoURI)
    .then(() => console.log('MongoDB Connected'))

app.set('view engine', 'ejs')

// VALIDATION FUNCTION TO CHECK IF THERE ARE A LOGGED IN USER OR NOT
app.get('/', async (req, res) => {
    const posts = await Post.find().sort({createdAt : 'desc'})

    if (typeof req.session.email != 'undefined') {
        res.render('home', { user : req.session.name, posts : posts })
    } else {
        res.render('login')
    }
})

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

app.post('/login', async (req, res) => {
    const email = req.body.email
    const password = req.body.password
    
    const user = await User.find({email : email});

    if (typeof user[0] == 'undefined') {
        res.render('login', {msg : 'User not found'})
    }
    
    else if (user[0].password == password) {
        req.session.email = email
        req.session.name = user[0].name
        res.redirect('/');
    }
    
    else {
        res.render('login', {msg : 'Wrong Password'})
    }

})

app.get('/logout', (req, res) => {
    req.session.destroy(function(err) {
        res.render('login', {msg : 'You have logged out'})
    })
})

app.get('/new', (req, res) => {
    res.render('new')
})

app.post('/save', (req, res) => {
    const post = new Post({
        title: req.body.title,
        description: req.body.description,
        // The author is the user that are currently logged in
        author: req.session.name
    });

    Post.create(post, () => {
        res.redirect('/');
    });
})

app.get('/delete/:id', async (req, res) => {
    await  Post.deleteOne({ _id : req.params.id }, () => {
        res.redirect('/');
    });
})

app.listen(5001)
console.log('Listening on port 5001')