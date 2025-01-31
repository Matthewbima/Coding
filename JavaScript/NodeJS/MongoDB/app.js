const express = require('express');
const app = express();
const mongoose = require('mongoose');
const Student = require('./models/students');

const mongoURI = 'mongodb://bima:admin123@kodingnext-shard-00-00.dea8z.mongodb.net:27017,kodingnext-shard-00-01.dea8z.mongodb.net:27017,kodingnext-shard-00-02.dea8z.mongodb.net:27017/?ssl=true&replicaSet=atlas-5vduiq-shard-0&authSource=admin&retryWrites=true&w=majority&appName=KodingNext';

app.use(express.json());

mongoose.connect(mongoURI)
  .then(() => console.log('MongoDB Connected!'))
  .catch(err => console.error('MongoDB connection error:', err));

app.get('/', async (req, res) => {
    try {
        const students = await Student.find();
        res.send(students);
    } catch (err) {
        res.status(500).send({ message: 'Error fetching students', error: err });
    }
});

app.post('/insert', (req, res) => {
    const student = new Student({
        name: req.body.name,
        phone: req.body.phone
    });

    Student.create(student)
      .then(() => {
          res.send({ message: 'Data created successfully' });
      })
      .catch((err) => {
          res.status(500).send({ message: 'Error creating data', error: err });
      });
});

app.listen(5001, () => console.log('Listening on port 5001'));
