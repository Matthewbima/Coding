const express = require('express')
const app = express()

app.use(express.json())

// Array as the database
const posts = [{
        id: 1,
        title: 'Post 1',
        description: 'Post Description 1'
    },
    {
        id: 2,
        title: 'Post 2',
        description: 'Post Description 2'
    },
    {
        id: 3,
        title: 'Post 3',
        description: 'Post Description 3'
    },
]

app.get('/', (req, res) => {
    res.send('<h1>Hello World!</h1>')
})

app.get('/posts', (req, res) => {
    res.send(posts)
})

app.post('/posts', (req, res) => {
    const post = {
        id: posts.length + 1,
        title: req.body.title,
        description: req.body.description,
    }

    posts.push(post)
    res.send(posts)
})

// Listener
const port = 5000
app.listen(port, () => console.log(`Listening on port ${port}`))