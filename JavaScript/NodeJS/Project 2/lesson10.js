// pokemon-info.js
const http = require('http');
const create = require('./pokemon-display');

const server = http.createServer((req, res) => {
    if (req.url == '/') {
        res.write(create.createHeader('Welcome to the Pokemon Trainer Hub!'));
        res.write(create.createParagraph('Your ultimate resource for all things Pokemon!'));
        res.end();
    }
    
    else if (req.url == '/about') {
        res.write(create.createHeader('About the Trainer'));
        res.write(create.createParagraph('Trainer Name: Ash Ketchum'));
        res.write(create.createParagraph('Favorite Pokemon: Pikachu'));
        res.write(create.createParagraph('Number of Badges: 8'));
        res.end();
    }

    else if (req.url == '/pokedex') {
        res.write(create.createHeader('Pokedex'));
        res.write(create.createParagraph('Some Pokemon in your collection:'));
        res.write(create.createList(['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle']));
        res.end();
    }

    else {
        res.write(create.createHeader('Error 404'));
        res.write(create.createParagraph('Page not found. Perhaps you wandered into tall grass?'));
        res.end();
    }
});

server.listen(5000);

console.log('Listening on port 5000');
