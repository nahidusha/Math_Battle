document.addEventListener('DOMContentLoaded', (event) => {
    const expressionElement = document.getElementById('expression');
    const answerInput = document.getElementById('answer');
    const submitButton = document.getElementById('submit-btn');
    const resultMessage = document.getElementById('result-message');
    const scoreElement = document.getElementById('score');
    const playAgainButton = document.getElementById('play-again-btn');
    const gameDiv = document.getElementById('game');
    const timerElement = document.getElementById('timer');
    const welcomeMessage = document.getElementById('welcome-message');
    const instruction = document.getElementById('instruction');

    let score = 0;
    let wrongAnswers = 0;
    let correctAnswer;
    let timer;
    let countdown;

    function generateExpression() {
        const num1 = Math.floor(Math.random() * 20) + 1;
        const num2 = Math.floor(Math.random() * 20) + 1;
        const operators = ['+', '-', '*'];
        const operator = operators[Math.floor(Math.random() * operators.length)];
        return `${num1} ${operator} ${num2}`;
    }

    function startGame() {
        score = 0;
        wrongAnswers = 0;
        gameDiv.style.display = 'block';
        playAgainButton.style.display = 'none';
        nextExpression();
    }

    function nextExpression() {
        const exp = generateExpression();
        expressionElement.textContent = `Solve: ${exp}`;
        correctAnswer = eval(exp);
        answerInput.value = '';
        answerInput.focus();
        startTimer();
    }

    function startTimer() {
        clearInterval(countdown);
        let timeLeft = 5;
        timerElement.textContent = `Time left: ${timeLeft}s`;

        countdown = setInterval(() => {
            timeLeft--;
            timerElement.textContent = `Time left: ${timeLeft}s`;

            if (timeLeft <= 0) {
                clearInterval(countdown);
                resultMessage.textContent = "Time's up!";
                endGame();
            }
        }, 1000);
    }

    function endGame() {
        clearInterval(countdown);
        resultMessage.textContent += " Game over.";
        scoreElement.textContent = `Your final score is: ${score}`;
        gameDiv.style.display = 'none';
        playAgainButton.style.display = 'block';
    }

    function handleSubmit() {
        const userAnswer = parseInt(answerInput.value);
        if (userAnswer === correctAnswer) {
            resultMessage.textContent = "Correct!";
            score++;
        } else {
            resultMessage.textContent = "Incorrect!";
            wrongAnswers++;
            if (wrongAnswers === 2) {
                endGame();
                return;
            }
        }
        nextExpression();
    }

    submitButton.addEventListener('click', handleSubmit);

    answerInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            handleSubmit();
        }
    });

    playAgainButton.addEventListener('click', startGame);

    welcomeMessage.style.display = 'block';
    instruction.style.display = 'block';
    playAgainButton.style.display = 'block';
});
