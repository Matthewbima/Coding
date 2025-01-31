// pokemon-display.js
const createHeader = (text) => {
    return `<h1>${text}</h1>`;
};

const createParagraph = (text) => {
    return `<p>${text}</p>`;
};

const createList = (items) => {
    const listItems = items.map(item => `<li>${item}</li>`).join('');
    return `<ul>${listItems}</ul>`;
};

exports.createHeader = createHeader;
exports.createParagraph = createParagraph;
exports.createList = createList;
