let score = 0;
let question_num = 0;

const questions = [
    "Who is the creator of Valorant?",
    "Which agent can heal?",
    "What color is Phoenix's signature move?",
    "Which agent is known for her healing abilities?",
    "Which Valorant map features a teleporter?"
];

const options = [
    ["Riot Games", "Valve", "Epic Games"],
    ["Reyna", "Sage", "Brimstone"],
    ["Blue", "Green", "Red"],
    ["Jett", "Phoenix", "Sage"],
    ["Bind", "Haven", "Split"]
];

const real_answers = ["a", "b", "c", "c", "a"];

function setQuestion(num) {
    if (num < questions.length) {
        document.getElementById("no").innerHTML = num + 1;
        document.getElementById("question").innerHTML = questions[num];
        document.getElementById("showA").innerHTML = options[num][0];
        document.getElementById("showB").innerHTML = options[num][1];
        document.getElementById("showC").innerHTML = options[num][2];
    }
}

setQuestion(question_num);

function validateChecked() {
    if (document.getElementById("option1").checked) return "a";
    if (document.getElementById("option2").checked) return "b";
    if (document.getElementById("option3").checked) return "c";
}

function check() {
    if (question_num < questions.length) {
        const answer = validateChecked();
        if (answer === real_answers[question_num]) score++;
        question_num++;
        setQuestion(question_num);
    }

    if (question_num >= questions.length) {
        document.getElementById("score").innerHTML = "Your score: " + score;
        document.getElementById("btnAnswer").disabled = true;
    }

    document.getElementById("option1").checked = false;
    document.getElementById("option2").checked = false;
    document.getElementById("option3").checked = false;
}
