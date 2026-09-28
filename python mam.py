<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI VS REAL — Forensic Detective</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    background: radial-gradient(circle at top, #10252b, #020506 65%);
    color: #e8ffff;
    font-family: "Courier New", monospace;
    overflow-x: hidden;
}

header {
    padding: 22px;
    text-align: center;
    border-bottom: 1px solid #00ffc3;
    background: rgba(2,10,11,0.9);
    box-shadow: 0 0 30px #00ffc322;
}

.logo {
    font-size: 32px;
    font-weight: bold;
    color: #00ffc3;
    text-shadow: 0 0 8px #00ffc3, 0 0 20px #00ffc3;
}

.subtitle {
    color: #71908b;
    margin-top: 8px;
}

.container {
    width: 94%;
    max-width: 1250px;
    margin: 25px auto;
}

.stats {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-bottom: 20px;
}

.stat {
    background: #071011;
    border: 1px solid #17443c;
    border-radius: 10px;
    padding: 13px;
    text-align: center;
}

.stat-title {
    color: #66827d;
    font-size: 12px;
}

.stat-value {
    color: #00ffc3;
    font-size: 20px;
    margin-top: 5px;
    font-weight: bold;
}

.timer-bar {
    height: 8px;
    background: #0d1818;
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 20px;
}

#timerProgress {
    width: 100%;
    height: 100%;
    background: #00ffc3;
    transition: width 0.1s linear;
}

#timerProgress.danger {
    background: #ff4545;
}

.round-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.round-title {
    color: #00ffc3;
    font-size: 20px;
}

.difficulty {
    padding: 7px 12px;
    border: 1px solid #ffbd4a;
    color: #ffbd4a;
    border-radius: 20px;
    font-size: 12px;
}

.images {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.image-card {
    position: relative;
    background: #060c0d;
    border: 2px solid #173d38;
    border-radius: 14px;
    overflow: hidden;
    cursor: pointer;
    transition: 0.25s;
}

.image-card:hover {
    transform: translateY(-5px);
    border-color: #00ffc3;
}

.image-card.selected {
    border-color: #00ffc3;
    box-shadow: 0 0 35px #00ffc344;
}

.image-card.correct {
    border-color: #66ff88;
    box-shadow: 0 0 30px #66ff8844;
}

.image-card.wrong {
    border-color: #ff4545;
    box-shadow: 0 0 30px #ff454544;
}

.image-card img {
    display: block;
    width: 100%;
    height: 390px;
    object-fit: cover;
    background: #111;
}

.image-label {
    position: absolute;
    top: 12px;
    left: 12px;
    padding: 7px 12px;
    background: rgba(0,0,0,0.75);
    border-radius: 6px;
    font-weight: bold;
}

.choice-area {
    margin-top: 20px;
    padding: 20px;
    background: #071011;
    border: 1px solid #17443c;
    border-radius: 12px;
}

.choice-title {
    color: #8fb3ad;
    margin-bottom: 14px;
}

.choice-buttons,
.secondary-actions {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 12px;
}

.choice {
    width: 100%;
    padding: 14px;
    background: transparent;
    color: #00ffc3;
    border: 1px solid #00ffc3;
    border-radius: 8px;
    font-family: inherit;
    cursor: pointer;
}

.choice:hover:not(:disabled) {
    background: #00ffc3;
    color: #02100c;
}

.choice:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.clue-area {
    display: none;
    margin-top: 18px;
    padding: 20px;
    background: #0b1112;
    border: 1px solid #41544f;
    border-radius: 12px;
}

.clue-area h3 {
    margin-top: 0;
    color: #ffbd4a;
}

.clue-options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
}

.clue-option {
    padding: 10px;
    background: #0b1515;
    border: 1px solid #23433d;
    border-radius: 7px;
    color: #8ca7a2;
    cursor: pointer;
}

.clue-option:hover {
    border-color: #ffbd4a;
    color: #ffbd4a;
}

.hint-box {
    display: none;
    margin-top: 15px;
    padding: 15px;
    border-left: 3px solid #ffbd4a;
    background: #171208;
    color: #c9b27b;
}

.result {
    display: none;
    margin-top: 20px;
    padding: 20px;
    border-radius: 12px;
    background: #071011;
}

.result.correct {
    border: 1px solid #66ff88;
}

.result.wrong {
    border: 1px solid #ff4545;
}

.result-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}

.correct-text {
    color: #66ff88;
}

.wrong-text {
    color: #ff5555;
}

.explanation {
    color: #a8bbb7;
    line-height: 1.6;
}

.next-button {
    width: 100%;
    margin-top: 15px;
    padding: 14px;
    background: #00ffc3;
    border: none;
    color: #02100c;
    font-weight: bold;
    font-family: inherit;
    border-radius: 8px;
    cursor: pointer;
    display: none;
}

#endScreen {
    display: none;
    position: fixed;
    inset: 0;
    z-index: 100;
    align-items: center;
    justify-content: center;
    background: rgba(0,0,0,0.94);
}

.end-box {
    width: 90%;
    max-width: 650px;
    padding: 40px;
    text-align: center;
    background: #071011;
    border: 1px solid #00ffc3;
    border-radius: 16px;
}

.end-icon {
    font-size: 70px;
}

.end-box h1 {
    color: #00ffc3;
    font-size: 38px;
    margin: 10px 0;
}

.final-score {
    font-size: 28px;
    margin: 20px;
}

.rank {
    color: #ffbd4a;
    font-size: 20px;
}

@media(max-width:800px) {
    .stats {
        grid-template-columns: repeat(2,1fr);
    }

    .images {
        grid-template-columns: 1fr;
    }

    .image-card img {
        height: 300px;
    }

    .choice-buttons,
    .secondary-actions,
    .clue-options {
        grid-template-columns: 1fr;
    }

    .logo {
        font-size: 24px;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">🕵️ AI VS REAL</div>
    <div class="subtitle">DIGITAL IMAGE FORENSICS — HARD MODE</div>
</header>

<div class="container">

    <div class="stats">
        <div class="stat">
            <div class="stat-title">ROUND</div>
            <div id="round" class="stat-value">1/8</div>
        </div>

        <div class="stat">
            <div class="stat-title">SCORE</div>
            <div id="score" class="stat-value">0</div>
        </div>

        <div class="stat">
            <div class="stat-title">STREAK</div>
            <div id="streak" class="stat-value">0</div>
        </div>

        <div class="stat">
            <div class="stat-title">TIME</div>
            <div id="time" class="stat-value">12</div>
        </div>

        <div class="stat">
            <div class="stat-title">RANK</div>
            <div id="rank" class="stat-value">ROOKIE</div>
        </div>
    </div>

    <div class="timer-bar">
        <div id="timerProgress"></div>
    </div>

    <div class="round-header">
        <div class="round-title">FORENSIC ROUND</div>
        <div id="difficulty" class="difficulty">EXPERT</div>
    </div>

    <div class="images">

        <div id="cardA" class="image-card" onclick="chooseImage('A')">
            <img id="imageA" alt="Image A">
            <div class="image-label">IMAGE A</div>
        </div>

        <div id="cardB" class="image-card" onclick="chooseImage('B')">
            <img id="imageB" alt="Image B">
            <div class="image-label">IMAGE B</div>
        </div>

    </div>

    <div class="choice-area">

        <div class="choice-title">
            🔍 Which image is AI-generated?
        </div>

        <div class="choice-buttons">

            <button class="choice choice-btn"
                    onclick="submitGuess('A')">
                🤖 IMAGE A IS AI
            </button>

            <button class="choice choice-btn"
                    onclick="submitGuess('B')">
                🤖 IMAGE B IS AI
            </button>

        </div>

        <div class="secondary-actions">

            <button id="hintBtn"
                    class="choice choice-btn"
                    onclick="useHint()">
                💡 USE FORENSIC HINT (-25)
            </button>

            <button class="choice choice-btn"
                    onclick="submitGuess('REAL')">
                📸 BOTH LOOK REAL
            </button>

        </div>

        <div id="clueArea" class="clue-area">

            <h3>🔬 WHAT MADE YOU SUSPICIOUS?</h3>

            <p>Select the clue you noticed:</p>

            <div class="clue-options">

                <div class="clue-option"
                     onclick="selectClue('lighting')">
                    💡 Lighting
                </div>

                <div class="clue-option"
                     onclick="selectClue('shadow')">
                    🌑 Shadow
                </div>

                <div class="clue-option"
                     onclick="selectClue('reflection')">
                    🪞 Reflection
                </div>

                <div class="clue-option"
                     onclick="selectClue('text')">
                    🔤 Text
                </div>

                <div class="clue-option"
                     onclick="selectClue('object')">
                    🧩 Object consistency
                </div>

                <div class="clue-option"
                     onclick="selectClue('texture')">
                    🔬 Texture
                </div>

            </div>

        </div>

        <div id="hint" class="hint-box"></div>

        <div id="result" class="result">

            <div id="resultTitle" class="result-title"></div>

            <div id="resultText" class="explanation"></div>

        </div>

        <button id="nextButton"
                class="next-button"
                onclick="nextRound()">
            NEXT FORENSIC CASE →
        </button>

    </div>

</div>

<div id="endScreen">

    <div class="end-box">

        <div class="end-icon">🏆</div>

        <h1>CASE FILE CLOSED</h1>

        <p>You completed the AI image forensic investigation.</p>

        <div class="final-score">
            Score:
            <strong id="finalScore">0</strong>
        </div>

        <div class="rank">
            🕵️ <span id="finalRank">ROOKIE</span>
        </div>

        <br>

        <p id="finalMessage"></p>

        <button class="choice" onclick="restartGame()">
            🔄 INVESTIGATE AGAIN
        </button>

    </div>

</div>

<script>

const rounds = [

{
    ai: "B",
    difficulty: "EXPERT",
    imageA: "https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1000&q=85",
    imageB: "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=1000&q=85",
    clue: "The AI image contains subtle inconsistencies in fine facial and hair details.",
    hint: "Look closely at the smallest repeating textures and hair strands."
},

{
    ai: "A",
    difficulty: "FORENSIC",
    imageA: "https://images.unsplash.com/photo-1511818966892-d7d671e672a2?auto=format&fit=crop&w=1000&q=85",
    imageB: "https://images.unsplash.com/photo-1518005020951-eccb494ad742?auto=format&fit=crop&w=1000&q=85",
    clue: "The suspicious architecture has subtle perspective and structural inconsistencies.",
    hint: "Follow straight architectural lines toward the distance."
},

{
    ai: "B",
    difficulty: "PHANTOM",
    imageA: "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1000&q=85",
    imageB: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1000&q=85",
    clue: "The AI scene contains repeated visual patterns that are unusually similar.",
    hint: "Compare chairs, objects and repeated shapes."
},

{
    ai: "A",
    difficulty: "FORENSIC",
    imageA: "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=1000&q=85",
    imageB: "https://images.unsplash.com/photo-1519501025264-65ba15a82390?auto=format&fit=crop&w=1000&q=85",
    clue: "The suspicious image has subtle inconsistencies in lighting.",
    hint: "Check whether objects receive light from the same direction."
},

{
    ai: "B",
    difficulty: "PHANTOM",
    imageA: "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1000&q=85",
    imageB: "https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1000&q=85",
    clue: "The suspicious scene contains subtle texture repetition.",
    hint: "Look at the background rather than the main subject."
},

{
    ai: "A",
    difficulty: "EXPERT",
    imageA: "https://images.unsplash.com/photo-1493246507139-91e8fad9978e?auto=format&fit=crop&w=1000&q=85",
    imageB: "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=85",
    clue: "The suspicious image contains unnatural environmental detail.",
    hint: "Look at distant objects rather than the main landscape."
},

{
    ai: "B",
    difficulty: "PHANTOM",
    imageA: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1000&q=85",
    imageB: "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1000&q=85",
    clue: "The suspicious image has inconsistencies in reflections and glass.",
    hint: "Inspect windows and reflective surfaces."
},

{
    ai: "A",
    difficulty: "FINAL BOSS",
    imageA: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1000&q=85",
    imageB: "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1000&q=85",
    clue: "The final case contains inconsistencies in objects and fine details.",
    hint: "Inspect the entire scene carefully."
}

];

let currentRound = 0;
let score = 0;
let streak = 0;
let time = 12;
let timer = null;
let hintUsed = false;
let guessMade = false;

function loadRound() {

    const data = rounds[currentRound];

    document.getElementById("round").textContent =
        (currentRound + 1) + "/" + rounds.length;

    document.getElementById("difficulty").textContent =
        data.difficulty;

    document.getElementById("imageA").src = data.imageA;
    document.getElementById("imageB").src = data.imageB;

    document.getElementById("cardA").className =
        "image-card";

    document.getElementById("cardB").className =
        "image-card";

    document.getElementById("result").style.display =
        "none";

    document.getElementById("nextButton").style.display =
        "none";

    document.getElementById("clueArea").style.display =
        "none";

    document.getElementById("hint").style.display =
        "none";

    document.getElementById("hintBtn").disabled =
        false;

    hintUsed = false;
    guessMade = false;

    toggleButtons(false);

    startTimer();
}

function toggleButtons(disabled) {

    document.querySelectorAll(".choice-btn")
        .forEach(function(button) {
            button.disabled = disabled;
        });

}

function startTimer() {

    clearInterval(timer);

    time = 12;

    updateTimer();

    timer = setInterval(function() {

        time -= 0.1;

        updateTimer();

        if (time <= 0) {

            clearInterval(timer);

            timeUp();

        }

    }, 100);

}

function updateTimer() {

    document.getElementById("time").textContent =
        Math.max(0, Math.ceil(time));

    let percentage =
        Math.max(0, (time / 12) * 100);

    document.getElementById("timerProgress")
        .style.width = percentage + "%";

    if (time <= 4) {

        document.getElementById("timerProgress")
            .classList.add("danger");

    } else {

        document.getElementById("timerProgress")
            .classList.remove("danger");

    }

}

function chooseImage(letter) {

    if (guessMade) return;

    document.getElementById("cardA")
        .classList.remove("selected");

    document.getElementById("cardB")
        .classList.remove("selected");

    document.getElementById("card" + letter)
        .classList.add("selected");

}

function submitGuess(answer) {

    if (guessMade) return;

    guessMade = true;

    clearInterval(timer);

    toggleButtons(true);

    const data = rounds[currentRound];

    const correct = answer === data.ai;

    if (correct) {

        let points = 100;

        points += Math.floor(time * 5);

        if (streak >= 2) {
            points += 50;
        }

        if (hintUsed) {
            points -= 25;
        }

        score += Math.max(0, points);

        streak++;

        document.getElementById("card" + data.ai)
            .classList.add("correct");

        showResult(true, points, data.clue);

    } else {

        streak = 0;

        document.getElementById("card" + data.ai)
            .classList.add("correct");

        if (answer === "A" || answer === "B") {

            document.getElementById("card" + answer)
                .classList.add("wrong");

        }

        showResult(false, 0, data.clue);
    }

    updateStats();

    document.getElementById("clueArea")
        .style.display = "block";
}

function showResult(correct, points, explanation) {

    const result =
        document.getElementById("result");

    result.style.display = "block";

    if (correct) {

        result.className = "result correct";

        document.getElementById("resultTitle").innerHTML =
            '<span class="correct-text">✅ CORRECT — FORENSIC MATCH</span>';

        document.getElementById("resultText").innerHTML =
            "<strong>+" + points + " XP</strong><br><br>" +
            explanation;

    } else {

        result.className = "result wrong";

        document.getElementById("resultTitle").innerHTML =
            '<span class="wrong-text">❌ INCORRECT</span>';

        document.getElementById("resultText").innerHTML =
            "The AI-generated image was <strong>IMAGE " +
            rounds[currentRound].ai +
            "</strong>.<br><br>" +
            explanation;
    }

    document.getElementById("nextButton")
        .style.display = "block";
}

function selectClue(type) {

    if (!guessMade) return;

    const messages = {

        lighting:
            "You noticed the lighting. AI images can sometimes create inconsistent light direction.",

        shadow:
            "Shadows can reveal impossible light sources or incorrect object placement.",

        reflection:
            "Reflections are difficult for image generators because they must match the original scene.",

        text:
            "AI-generated text can contain subtle character, spacing or structural errors.",

        object:
            "Object consistency is an important forensic clue.",

        texture:
            "Textures such as hair, grass and fabric can contain unnatural repetition."

    };

    document.getElementById("resultText").innerHTML +=
        "<br><br>🔬 <strong>YOUR ANALYSIS:</strong> " +
        messages[type];
}

function useHint() {

    if (hintUsed || guessMade) return;

    hintUsed = true;

    const hint =
        document.getElementById("hint");

    hint.textContent =
        "💡 FORENSIC HINT: " +
        rounds[currentRound].hint;

    hint.style.display = "block";

    document.getElementById("hintBtn").disabled =
        true;
}

function timeUp() {

    if (guessMade) return;

    guessMade = true;

    streak = 0;

    toggleButtons(true);

    const data = rounds[currentRound];

    document.getElementById("card" + data.ai)
        .classList.add("correct");

    showResult(
        false,
        0,
        "Time expired! " + data.clue
    );

    updateStats();

    document.getElementById("clueArea")
        .style.display = "block";
}

function nextRound() {

    currentRound++;

    if (currentRound >= rounds.length) {

        endGame();

        return;
    }

    loadRound();
}

function updateStats() {

    document.getElementById("score")
        .textContent = score;

    document.getElementById("streak")
        .textContent = streak;

    let rank = "ROOKIE";

    if (score >= 1200) {
        rank = "PHANTOM ANALYST";
    } else if (score >= 900) {
        rank = "FORENSIC EXPERT";
    } else if (score >= 600) {
        rank = "DIGITAL DETECTIVE";
    } else if (score >= 300) {
        rank = "INVESTIGATOR";
    }

    document.getElementById("rank")
        .textContent = rank;
}

function endGame() {

    clearInterval(timer);

    document.getElementById("endScreen")
        .style.display = "flex";

    document.getElementById("finalScore")
        .textContent = score;

    let rank;
    let message;

    if (score < 300) {

        rank = "ROOKIE";

        message =
            "The images fooled you this time. Keep training your forensic eye.";

    } else if (score < 600) {

        rank = "IMAGE INVESTIGATOR";

        message =
            "Good work. You are beginning to spot subtle visual inconsistencies.";

    } else if (score < 900) {

        rank = "DIGITAL DETECTIVE";

        message =
            "Excellent analysis. Your visual forensic skills are strong.";

    } else if (score < 1200) {

        rank = "FORENSIC EXPERT";

        message =
            "Outstanding. You detected subtle AI artifacts.";

    } else {

        rank = "PHANTOM ANALYST";

        message =
            "Elite performance. You are extremely difficult to fool.";

    }

    document.getElementById("finalRank")
        .textContent = rank;

    document.getElementById("finalMessage")
        .textContent = message;
}

function restartGame() {

    clearInterval(timer);

    currentRound = 0;
    score = 0;
    streak = 0;

    document.getElementById("endScreen")
        .style.display = "none";

    updateStats();

    loadRound();
}

loadRound();
updateStats();

</script>

</body>
</html>