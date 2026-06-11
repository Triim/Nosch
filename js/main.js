/**
 * KNOWLEDGE QUEST - Ultra Randomized Experience
 */

const LEVELS = [
    { 
        id: 0, title: "Binary Foundations", level: "Beginner", desc: "The heartbeat of all computing is binary.",
        x: 120, y: 880,
        pool: [
            { type: "slider", desc: "Convert binary 1011 to decimal.", answer: 11 },
            { type: "choice", desc: "What is 1 + 1 in binary?", choices: ["1", "10", "11", "100"], answer: "10" },
            { type: "click", desc: "Click exactly 3 times to simulate a 3-bit register.", answer: 3 },
            { type: "slider", desc: "Binary 111 is decimal...", answer: 7 },
            { type: "choice", desc: "Which is the smallest binary value?", choices: ["10", "01", "11", "101"], answer: "01" },
            { type: "text", desc: "Convert decimal 5 to binary.", answer: "101" },
            { type: "choice", desc: "How many bits in a byte?", choices: ["4", "8", "16", "32"], answer: "8" },
            { type: "slider", desc: "Binary 1000 is decimal...", answer: 8 },
            { type: "text", desc: "Binary for decimal 2?", answer: "10" },
            { type: "click", desc: "Click 8 times for one byte.", answer: 8 }
        ]
    },
    { 
        id: 1, title: "Pythonic Flow", level: "Beginner", desc: "Organize operations in the correct logical order.",
        x: 220, y: 780,
        pool: [
            { type: "sort", desc: "Correct order for a script:", options: ["Initialize List", "Append Data", "Sort Collection", "Output Result"], answer: ["Initialize List", "Append Data", "Sort Collection", "Output Result"] },
            { type: "choice", desc: "Which symbol is used for comments in Python?", choices: ["//", "/*", "#", "--"], answer: "#" },
            { type: "slider", desc: "len([1, 2, 3, 4, 5]) is...", answer: 5 },
            { type: "choice", desc: "Which keyword is used for functions?", choices: ["func", "define", "def", "function"], answer: "def" },
            { type: "text", desc: "What is the keyword to start a loop that repeats a fixed number of times?", answer: "for" },
            { type: "choice", desc: "Which is a valid list?", choices: ["{1,2}", "[1,2]", "(1,2)", "<1,2>"], answer: "[1,2]" },
            { type: "slider", desc: "2**3 equals...", answer: 8 },
            { type: "choice", desc: "Keyword to exit a loop?", choices: ["stop", "exit", "break", "return"], answer: "break" },
            { type: "text", desc: "Correct keyword for a conditional branch?", answer: "if" },
            { type: "sort", desc: "Print a greeting:", options: ["Define message", "Call print()", "Pass message to print", "Execute"], answer: ["Define message", "Pass message to print", "Call print()", "Execute"] }
        ]
    },
    { 
        id: 2, title: "NumPy Dimensions", level: "Intermediate", desc: "Link powerful NumPy concepts to definitions.",
        x: 320, y: 850,
        pool: [
            { type: "match", desc: "Match NumPy concepts:", pairs: { "Broadcasting": "Array shape alignment", "Axis": "Dimension index", "Slicing": "Subset selection", "Reshape": "Dimension change" } },
            { type: "choice", desc: "NumPy arrays are called...?", choices: ["Lists", "ndarrays", "Tensors", "Matrices"], answer: "ndarrays" },
            { type: "slider", desc: "A 2x3 array has how many elements?", answer: 6 },
            { type: "choice", desc: "Which method flattens an array?", choices: ["flatten()", "squeeze()", "reshape(1)", "all above"], answer: "all above" },
            { type: "match", desc: "Axis matching:", pairs: { "Axis 0": "Rows", "Axis 1": "Columns", "Axis 2": "Depth", "Axis -1": "Last" } },
            { type: "text", desc: "What function creates an array of zeros?", answer: "np.zeros" },
            { type: "slider", desc: "np.zeros((10,)) length is...", answer: 10 },
            { type: "choice", desc: "Slicing in NumPy creates a...?", choices: ["Copy", "View", "New List", "Tuple"], answer: "View" },
            { type: "text", desc: "Opposite of np.max()?", answer: "np.min" },
            { type: "choice", desc: "Standard NumPy import alias?", choices: ["num", "np", "nump", "numpy"], answer: "np" }
        ]
    },
    { 
        id: 3, title: "AI Architecture", level: "Intermediate", desc: "Outliers in the architecture of an LLM.",
        x: 420, y: 750,
        pool: [
            { type: "choice", desc: "Which is an outlier in LLM architecture?", choices: ["Attention Mechanism", "Transformer Block", "Steam Valve", "Token Embeddings"], answer: "Steam Valve" },
            { type: "slider", desc: "Typical temperature for creative text is around...", answer: 0.7 },
            { type: "choice", desc: "What does GPT stand for?", choices: ["General Pre-trained Transformer", "Generative Pre-trained Transformer", "Global Processing Tool", "Giant Python Trainer"], answer: "Generative Pre-trained Transformer" },
            { type: "match", desc: "AI terms:", pairs: { "Overfitting": "Too specific", "Underfitting": "Too simple", "Epoch": "Full pass", "Batch": "Subset" } },
            { type: "click", desc: "Simulate 2 epochs of training (click 2x).", answer: 2 },
            { type: "choice", desc: "Core component of Transformers?", choices: ["Recurrence", "Attention", "Convolution", "Sifting"], answer: "Attention" },
            { type: "text", desc: "What is the term for the input text fed into an LLM?", answer: "prompt" },
            { type: "match", desc: "Learning:", pairs: { "SGD": "Stochastic", "Adam": "Adaptive", "LR": "Step size", "Loss": "Error" } },
            { type: "choice", desc: "Which is NOT a common AI framework?", choices: ["PyTorch", "TensorFlow", "Keras", "Photoshop"], answer: "Photoshop" },
            { type: "slider", desc: "Learning rate is usually a very... (0 for small, 1 for large)", answer: 0 }
        ]
    },
    { 
        id: 4, title: "Iteration Logic", level: "Beginner", desc: "Simulate loops and execute cycles.",
        x: 520, y: 800,
        pool: [
            { type: "click", desc: "Execute exactly 5 cycles!", answer: 5 },
            { type: "choice", desc: "What happens if a loop condition is always true?", choices: ["Error", "Skip", "Infinite Loop", "Zero cycles"], answer: "Infinite Loop" },
            { type: "slider", desc: "range(0, 10, 2) produces how many values?", answer: 5 },
            { type: "sort", desc: "Loop lifecycle:", options: ["Check condition", "Execute body", "Update counter", "Repeat"], answer: ["Check condition", "Execute body", "Update counter", "Repeat"] },
            { type: "choice", desc: "Which keyword breaks a loop?", choices: ["stop", "exit", "break", "return"], answer: "break" },
            { type: "text", desc: "What is the keyword to skip the rest of the current loop iteration?", answer: "continue" },
            { type: "click", desc: "Execute 7 cycles!", answer: 7 },
            { type: "slider", desc: "while(False) runs how many times?", answer: 0 },
            { type: "choice", desc: "Which loop is typically used when the number of iterations is known?", choices: ["while", "for", "do-while", "if"], answer: "for" },
            { type: "text", desc: "What do you call a loop inside another loop?", answer: "nested" }
        ]
    },
    { 
        id: 5, title: "Geometric Constants", level: "Beginner", desc: "Calculate area and properties of shapes.",
        x: 620, y: 700,
        pool: [
            { type: "slider", desc: "Area of unit circle (r=1, Pi=3.14).", answer: 3.14 },
            { type: "choice", desc: "Sum of angles in a triangle?", choices: ["90", "180", "270", "360"], answer: "180" },
            { type: "slider", desc: "Side of a square with area 16 is...", answer: 4 },
            { type: "match", desc: "Shapes:", pairs: { "Isosceles": "2 equal sides", "Scalene": "0 equal sides", "Equilateral": "3 equal sides", "Right": "90 degree" } },
            { type: "choice", desc: "Value of cos(0)?", choices: ["0", "0.5", "1", "-1"], answer: "1" },
            { type: "text", desc: "How many degrees are in a full circle?", answer: "360" },
            { type: "slider", desc: "Area of rectangle 5x4 is...", answer: 20 },
            { type: "choice", desc: "A pentagon has how many sides?", choices: ["4", "5", "6", "8"], answer: "5" },
            { type: "text", desc: "A triangle with all sides equal is called...?", answer: "equilateral" },
            { type: "slider", desc: "Radius is 5, diameter is...?", answer: 10 }
        ]
    },
    { 
        id: 6, title: "Logic Gates", level: "Beginner", desc: "Match Boolean operations to resulting states.",
        x: 720, y: 750,
        pool: [
            { type: "match", desc: "Boolean results:", pairs: { "T AND T": "True", "T OR F": "True", "T AND F": "False", "NOT T": "False" } },
            { type: "choice", desc: "Which gate is a 'flip'?", choices: ["AND", "OR", "NOT", "XOR"], answer: "NOT" },
            { type: "slider", desc: "1 OR 0 equals (0 for False, 1 for True)...", answer: 1 },
            { type: "choice", desc: "XOR is true when inputs are...", choices: ["Both true", "Both false", "Different", "Same"], answer: "Different" },
            { type: "match", desc: "Gate logic:", pairs: { "AND": "Both must be T", "OR": "Either can be T", "NAND": "Not both T", "NOR": "Neither T" } },
            { type: "text", desc: "What is the result of NOT(False)?", answer: "True" },
            { type: "slider", desc: "NOT (0) is (0 or 1)?", answer: 1 },
            { type: "choice", desc: "AND result is True only if...?", choices: ["One is T", "Both are T", "Both are F", "None are T"], answer: "Both are T" },
            { type: "text", desc: "Gate that returns True if exactly one input is True?", answer: "XOR" },
            { type: "choice", desc: "Which is the 'Inverse' gate?", choices: ["AND", "OR", "NOT", "XOR"], answer: "NOT" }
        ]
    },
    { 
        id: 7, title: "Algorithmic Speed", level: "Advanced", desc: "Rank Big-O complexities efficiently.",
        x: 820, y: 600,
        pool: [
            { type: "sort", desc: "Rank Big-O (fastest to slowest):", options: ["O(1)", "O(log n)", "O(n)", "O(n^2)"], answer: ["O(1)", "O(log n)", "O(n)", "O(n^2)"] },
            { type: "choice", desc: "Binary search complexity?", choices: ["O(1)", "O(n)", "O(log n)", "O(n log n)"], answer: "O(log n)" },
            { type: "slider", desc: "If n=10, what is n^2?", answer: 100 },
            { type: "match", desc: "Algorithm types:", pairs: { "QuickSort": "Divide & Conquer", "Dijkstra": "Greedy", "Fibonacci": "Dynamic", "BFS": "Queue" } },
            { type: "choice", desc: "Worst case for QuickSort?", choices: ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"], answer: "O(n^2)" },
            { type: "text", desc: "Complexity of accessing an array element by index?", answer: "O(1)" },
            { type: "slider", desc: "O(n) with n=50 takes how many steps?", answer: 50 },
            { type: "choice", desc: "Which is fastest?", choices: ["O(n)", "O(log n)", "O(n^2)", "O(n!)"], answer: "O(log n)" },
            { type: "text", desc: "Complexity of a single loop from 1 to n?", answer: "O(n)" },
            { type: "choice", desc: "What does Big-O measure?", choices: ["Exact time", "Memory only", "Upper bound growth", "Average speed"], answer: "Upper bound growth" }
        ]
    },
    { 
        id: 8, title: "Data Structures", level: "Advanced", desc: "Pair structures with governing principles.",
        x: 850, y: 450,
        pool: [
            { type: "match", desc: "Governing principles:", pairs: { "Stack": "LIFO", "Queue": "FIFO", "Hash Map": "O(1) Access", "Tree": "Hierarchical" } },
            { type: "choice", desc: "Which is NOT linear?", choices: ["Array", "Linked List", "Graph", "Stack"], answer: "Graph" },
            { type: "slider", desc: "Height of a balanced tree with 7 nodes is...", answer: 3 },
            { type: "match", desc: "Structures:", pairs: { "Heap": "Priority", "Set": "Unique", "Map": "Key-Value", "Deque": "Double-ended" } },
            { type: "choice", desc: "Best structure for a undo-button?", choices: ["Queue", "Stack", "Tree", "Hash Map"], answer: "Stack" },
            { type: "text", desc: "What does LIFO stand for?", answer: "Last In First Out" },
            { type: "choice", desc: "FIFO stands for...?", choices: ["First In First Out", "Fast In Fast Out", "First In Final Out", "None"], answer: "First In First Out" },
            { type: "slider", desc: "Average search time in Hash Map is O(...)?", answer: 1 },
            { type: "text", desc: "Which structure uses a Root and Children?", answer: "Tree" },
            { type: "choice", desc: "A set differs from a list because it only contains...?", choices: ["Numbers", "Unique values", "Strings", "Tuples"], answer: "Unique values" }
        ]
    },
    { 
        id: 9, title: "Slicing Logic", level: "Intermediate", desc: "Analyze slice outputs of lists.",
        x: 700, y: 350,
        pool: [
            { type: "choice", desc: "L = [10, 20, 30, 40]. L[1:3] is...?", choices: ["[10, 20]", "[20, 30]", "[20, 30, 40]", "[10, 20, 30]"], answer: "[20, 30]" },
            { type: "slider", desc: "L = [0,1,2,3]. L[-1] is...", answer: 3 },
            { type: "choice", desc: "What does L[::-1] do?", choices: ["Copies", "Clears", "Reverses", "Sorts"], answer: "Reverses" },
            { type: "match", desc: "Slicing:", pairs: { "start": "First index", "stop": "Exclude index", "step": "Stride", "negative": "From end" } },
            { type: "choice", desc: "L[0:100] where len(L)=5 results in...?", choices: ["Error", "Empty", "All elements", "First 100"], answer: "All elements" },
            { type: "text", desc: "In L[1:4], is index 4 included?", answer: "no" },
            { type: "slider", desc: "L = [10, 20, 30]. L[0:1] length is...", answer: 1 },
            { type: "choice", desc: "Index of first element?", choices: ["0", "1", "-1", "None"], answer: "0" },
            { type: "text", desc: "Which operator is used for slicing?", answer: ":" },
            { type: "slider", desc: "L = [1,2,3,4,5]. L[1:4] has how many elements?", answer: 3 }
        ]
    },
    { 
        id: 10, title: "Functional Flow", level: "Intermediate", desc: "Order the lifecycle of a function call.",
        x: 500, y: 300,
        pool: [
            { type: "sort", desc: "Lifecycle of a call:", options: ["Definition", "Invocation", "Execution", "Return"], answer: ["Definition", "Invocation", "Execution", "Return"] },
            { type: "choice", desc: "A function that calls itself is...?", choices: ["Iterative", "Recursive", "Linear", "Static"], answer: "Recursive" },
            { type: "slider", desc: "A function returning no value returns... (0 for None, 1 for True)", answer: 0 },
            { type: "match", desc: "Params:", pairs: { "Argument": "Actual value", "Parameter": "Placeholder", "Keyword": "Named", "Default": "Fallback" } },
            { type: "choice", desc: "Lambda functions are...?", choices: ["Long", "Anonymous", "Only for math", "Recursive"], answer: "Anonymous" },
            { type: "text", desc: "The keyword used to send a result back from a function?", answer: "return" },
            { type: "choice", desc: "A function that doesn't return a value is often called...?", choices: ["Procedure", "Variable", "Loop", "Class"], answer: "Procedure" },
            { type: "slider", desc: "Max recursion depth is usually... (100, 1000, 10000)", answer: 1000 },
            { type: "text", desc: "A variable defined inside a function is called...?", answer: "local" },
            { type: "choice", desc: "Which of these is a built-in Python function?", choices: [" print()", " run()", " execute()", " start()"], answer: " print()" }
        ]
    },
    { 
        id: 11, title: "The Summit", level: "Advanced", desc: "Ultimate challenge of knowledge.",
        x: 400, y: 150,
        pool: [
            { type: "slider", desc: "Sum of first 10 natural numbers.", answer: 55 },
            { type: "choice", desc: "Complexity of finding an element in a sorted array?", choices: ["O(n)", "O(1)", "O(log n)", "O(n^2)"], answer: "O(log n)" },
            { type: "match", desc: "Advanced:", pairs: { "Turing": "Machine", "Von Neumann": "Architecture", "Boolean": "Algebra", "Shannon": "Information" } },
            { type: "slider", desc: "If a process takes O(n), and n=1000, time is proportional to...", answer: 1000 },
            { type: "choice", desc: "Which is the ultimate goal of the Quest?", choices: ["Money", "Fame", "Knowledge", "A Trophy"], answer: "Knowledge" },
            { type: "text", desc: "Who developed the first programmable computer?", answer: "Turing" },
            { type: "slider", desc: "What is 2^10?", answer: 1024 },
            { type: "choice", desc: "Which is the most efficient sort for most cases?", choices: ["Bubble", "Selection", "QuickSort", "Insertion"], answer: "QuickSort" },
            { type: "text", desc: "Base 16 is called...?", answer: "hexadecimal" },
            { type: "slider", desc: "The value of e (approx)?", answer: 2.72 }
        ]
    },
];

const STATE = {
    userName: "",
    userEmail: "",
    claimedSpots: [],
    activeLevel: null,
    activeQuestions: [],
    currentQuestionIdx: 0,
    levelCorrectCount: 0,
    currentAnswer: null,
    tutorialStep: 0,
    darkMode: false
};

class SoundManager {
    constructor() { this.audioCtx = new (window.AudioContext || window.webkitAudioContext)(); }
    async play(type) {
        const sounds = { click: 'assets/sounds/click.mp3', success: 'assets/sounds/success.mp3', error: 'assets/sounds/error.mp3', move: 'assets/sounds/move.mp3' };
        try {
            const response = await fetch(sounds[type]);
            if (response.ok) {
                const buffer = await this.audioCtx.decodeAudioData(await response.arrayBuffer());
                const src = this.audioCtx.createBufferSource();
                src.buffer = buffer; src.connect(this.audioCtx.destination); src.start(0);
                return;
            }
        } catch (e) {}
        this.playSynth(type);
    }
    playSynth(type) {
        const osc = this.audioCtx.createOscillator();
        const gain = this.audioCtx.createGain();
        osc.connect(gain); gain.connect(this.audioCtx.destination);
        if (type === 'success') {
            osc.frequency.setValueAtTime(523, this.audioCtx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(880, this.audioCtx.currentTime + 0.1);
            gain.gain.setValueAtTime(0.1, this.audioCtx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, this.audioCtx.currentTime + 0.3);
            osc.start(); osc.stop(this.audioCtx.currentTime + 0.3);
        } else if (type === 'error') {
            osc.frequency.setValueAtTime(220, this.audioCtx.currentTime);
            osc.frequency.linearRampToValueAtTime(110, this.audioCtx.currentTime + 0.2);
            gain.gain.setValueAtTime(0.1, this.audioCtx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, this.audioCtx.currentTime + 0.3);
            osc.start(); osc.stop(this.audioCtx.currentTime + 0.3);
        } else {
            osc.frequency.setValueAtTime(440, this.audioCtx.currentTime);
            gain.gain.setValueAtTime(0.05, this.audioCtx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, this.audioCtx.currentTime + 0.1);
            osc.start(); osc.stop(this.audioCtx.currentTime + 0.1);
        }
    }
}
const sound = new SoundManager();

const canvas = document.getElementById('tech-canvas');
const ctx = canvas.getContext('2d');
let particles = [];
let width, height;
function resize() { width = canvas.width = window.innerWidth; height = canvas.height = window.innerHeight; }
class Particle {
    constructor() { this.init(); }
    init() {
        this.x = Math.random() * width; this.y = Math.random() * height;
        this.vx = (Math.random() - 0.5) * 0.3; this.vy = (Math.random() - 0.5) * 0.3;
        this.type = Math.random() > 0.8 ? 'main' : 'subtle';
        this.radius = this.type === 'main' ? Math.random() * 3 + 2 : Math.random() * 1.5 + 0.5;
        this.color = this.type === 'main' ? 'rgba(37, 99, 235, 0.6)' : 'rgba(148, 163, 184, 0.3)';
    }
    update() {
        this.x += this.vx; this.y += this.vy;
        if (this.x < 0 || this.x > width) this.vx *= -1;
        if (this.y < 0 || this.y > height) this.vy *= -1;
    }
    draw() {
        ctx.beginPath(); ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color; ctx.fill();
    }
}
function initParticles() {
    particles = [];
    for (let i = 0; i < 120; i++) particles.push(new Particle());
}
function animate() {
    ctx.clearRect(0, 0, width, height);
    particles.forEach(p => { p.update(); p.draw(); });
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.1)';
    ctx.lineWidth = 0.6;
    for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
            const dist = Math.hypot(particles[i].x - particles[j].x, particles[i].y - particles[j].y);
            if (dist < 180) {
                ctx.beginPath(); ctx.moveTo(particles[i].x, particles[i].y); ctx.lineTo(particles[j].x, particles[j].y); ctx.stroke();
            }
        }
    }
    requestAnimationFrame(animate);
}
window.addEventListener('resize', resize);
resize(); initParticles(); animate();

window.addEventListener('load', () => {
    const loader = document.querySelector('.loader-progress');
    let progress = 0;
    const interval = setInterval(() => {
        progress += Math.random() * 20;
        if (progress >= 100) {
            progress = 100;
            clearInterval(interval);
            setTimeout(() => {
                document.getElementById('loading-screen').style.opacity = '0';
                document.getElementById('loading-screen').style.visibility = 'hidden';
            }, 500);
        }
        loader.style.width = progress + '%';
    }, 150);
});

function validateEmail(email) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email); }

document.addEventListener('DOMContentLoaded', () => {
    const startScreen = document.getElementById('start-screen');
    const tutorialScreen = document.getElementById('tutorial-screen');
    const startBtn = document.getElementById('start-btn');
    const userNameInput = document.getElementById('user-name');
    const userEmailInput = document.getElementById('user-email');
    const userBadge = document.getElementById('user-badge');
    const premiumCard = startScreen.querySelector('.premium-card');

    startBtn.addEventListener('click', () => {
        const name = userNameInput.value.trim();
        const email = userEmailInput.value.trim();
        
        if (!name || !validateEmail(email)) {
            premiumCard.style.animation = 'shake 0.4s ease';
            userNameInput.style.borderColor = 'var(--error)';
            userEmailInput.style.borderColor = 'var(--error)';
            setTimeout(() => {
                premiumCard.style.animation = '';
            }, 400);
            return;
        }

        STATE.userName = name;
        STATE.userEmail = email;
        userBadge.innerText = `Explorer: ${STATE.userName}`;
        startScreen.classList.add('hidden');
        tutorialScreen.classList.remove('hidden');
        showTutorialStep(0);
    });

    document.getElementById('tutorial-next').addEventListener('click', () => {
        STATE.tutorialStep++;
        if (STATE.tutorialStep < 3) {
            showTutorialStep(STATE.tutorialStep);
        } else {
            tutorialScreen.classList.add('hidden');
            initGame();
        }
    });
});

function showTutorialStep(step) {
    document.querySelectorAll('.tutorial-step').forEach((el, i) => {
        el.classList.toggle('active', i === step);
    });
}

function initGame() {
    updateQuestLog();
    updateMapImage();
}

function updateMapImage() {
    const mapImg = document.getElementById('map-image');
    const count = STATE.claimedSpots.length;
    if (count === LEVELS.length) {
        mapImg.src = `assets/images/map_12.png`;
    } else {
        mapImg.src = `assets/images/map_0.png`;
    }
}

function updateQuestLog() {
    const container = document.getElementById('log-container');
    container.innerHTML = "";
    LEVELS.forEach((l, i) => {
        const isClaimed = STATE.claimedSpots.includes(i);
        const isAvailable = i === 0 || STATE.claimedSpots.includes(i - 1);
        const card = document.createElement('div');
        card.className = `syllabus-card ${isClaimed ? 'claimed' : ''} ${!isAvailable ? 'locked' : ''}`;
        card.innerHTML = `
            <div class="card-top">
                <h3>${l.title}</h3>
                <span class="difficulty-tag">${l.level}</span>
            </div>
            <p>${l.desc || "Master this module to progress."}</p>
            <div class="progress-section">
                <div class="progress-label"><span>Mastery</span><span>${isClaimed ? '100%' : '0%'}</span></div>
                <div class="progress-track"><div class="progress-fill" style="width: ${isClaimed ? '100%' : '0%'}"></div></div>
            </div>
            <button class="btn-action" ${!isAvailable ? 'disabled' : ''} onclick="openLevel(${i})">
                ${isClaimed ? 'Completed ✓' : 'Start Module'}
            </button>
        `;
        container.appendChild(card);
    });
}

const modal = document.getElementById('modal');
const modalUI = document.getElementById('modal-ui');

function openLevel(idx) {
    if (idx > 0 && !STATE.claimedSpots.includes(idx - 1)) {
        alert("This area is still locked. Please claim the previous spot first!");
        return;
    }
    if (STATE.claimedSpots.includes(idx)) {
        alert("You have already claimed this knowledge area!");
        return;
    }

    STATE.activeLevel = idx;
    STATE.currentQuestionIdx = 0;
    STATE.levelCorrectCount = 0;
    
    // Randomize questions: pick 5 from the pool
    const pool = LEVELS[idx].pool;
    STATE.activeQuestions = [...pool].sort(() => 0.5 - Math.random()).slice(0, 5);
    
    loadQuestion();
}

function loadQuestion() {
    const level = LEVELS[STATE.activeLevel];
    const q = STATE.activeQuestions[STATE.currentQuestionIdx];
    
    document.getElementById('modal-title').innerText = `${level.title} - Question ${STATE.currentQuestionIdx + 1}/5`;
    document.getElementById('modal-desc').innerText = q.desc;
    document.getElementById('modal-feedback').innerText = "";
    STATE.currentAnswer = null;
    modalUI.innerHTML = "";

    if (q.type === 'slider') {
        const container = document.createElement('div');
        container.className = "slider-box";
        const valDisp = document.createElement('div');
        valDisp.className = "slider-value";
        valDisp.innerText = "0";
        const slider = document.createElement('input');
        slider.type = "range";
        slider.className = "input-range";
        slider.min = 0; slider.max = 100; slider.step = 0.01;
        slider.oninput = () => {
            valDisp.innerText = slider.value;
            STATE.currentAnswer = slider.value;
        };
        container.appendChild(valDisp);
        container.appendChild(slider);
        modalUI.appendChild(container);
        STATE.currentAnswer = "0";
    } else if (q.type === 'sort') {
        const list = document.createElement('div');
        list.className = "sort-list";
        const options = [...q.options].sort(() => Math.random() - 0.5);
        let selectedOrder = [];
        options.forEach(opt => {
            const item = document.createElement('div');
            item.className = "sort-item";
            item.innerText = opt;
            item.onclick = () => {
                sound.play('click');
                if (!selectedOrder.includes(opt)) {
                    selectedOrder.push(opt);
                    item.classList.add('selected');
                } else {
                    selectedOrder = selectedOrder.filter(o => o !== opt);
                    item.classList.remove('selected');
                }
                STATE.currentAnswer = JSON.stringify(selectedOrder);
            };
            list.appendChild(item);
        });
        modalUI.appendChild(list);
    } else if (q.type === 'match') {
        const container = document.createElement('div');
        container.className = "match-grid";
        const keys = Object.keys(q.pairs);
        const vals = Object.values(q.pairs);
        const left = [...keys].sort(() => Math.random() - 0.5);
        const right = [...vals].sort(() => Math.random() - 0.5);
        let selected = null;
        let matchedPairs = 0;
        const createItem = (text, isKey) => {
            const item = document.createElement('div');
            item.className = "match-item";
            item.innerText = text;
            item.onclick = () => {
                sound.play('click');
                if (selected) {
                    if (selected.isKey !== isKey) {
                        const key = selected.isKey ? selected.text : text;
                        const val = selected.isKey ? text : selected.text;
                        if (q.pairs[key] === val) {
                            selected.el.classList.add('paired');
                            item.classList.add('paired');
                            matchedPairs++;
                            sound.play('success');
                        } else { sound.play('error'); }
                    }
                    selected.el.classList.remove('selected');
                    selected = null;
                } else {
                    selected = { el: item, text, isKey };
                    item.classList.add('selected');
                }
                STATE.currentAnswer = matchedPairs.toString();
            };
            return item;
        };
        const leftCol = document.createElement('div');
        left.forEach(k => leftCol.appendChild(createItem(k, true)));
        const rightCol = document.createElement('div');
        right.forEach(v => rightCol.appendChild(createItem(v, false)));
        container.appendChild(leftCol);
        container.appendChild(rightCol);
        modalUI.appendChild(container);
        STATE.currentAnswer = "0";
    } else if (q.type === 'choice') {
        const grid = document.createElement('div');
        grid.className = "choice-grid";
        q.choices.forEach(choice => {
            const card = document.createElement('div');
            card.className = "choice-card";
            card.innerText = choice;
            card.onclick = () => {
                sound.play('click');
                document.querySelectorAll('.choice-card').forEach(el => el.classList.remove('selected'));
                card.classList.add('selected');
                STATE.currentAnswer = choice;
            };
            grid.appendChild(card);
        });
        modalUI.appendChild(grid);
    } else if (q.type === 'click') {
        const container = document.createElement('div');
        container.className = "slider-box";
        const display = document.createElement('div');
        display.className = "slider-value";
        display.innerText = "0";
        const btn = document.createElement('button');
        btn.className = "btn-primary";
        btn.style.width = "200px";
        btn.innerText = "EXECUTE CYCLE";
        let count = 0;
        btn.onclick = () => {
            sound.play('click');
            count++;
            display.innerText = count;
            STATE.currentAnswer = count.toString();
        };
        container.appendChild(display);
        container.appendChild(btn);
        modalUI.appendChild(container);
        STATE.currentAnswer = "0";
    } else if (q.type === 'text') {
        const container = document.createElement('div');
        container.className = "text-input-box";
        const input = document.createElement('input');
        input.type = "text";
        input.className = "text-input";
        input.placeholder = "Type your answer here...";
        input.oninput = () => {
            STATE.currentAnswer = input.value.trim();
        };
        container.appendChild(input);
        modalUI.appendChild(container);
        STATE.currentAnswer = "";
    }

    modal.classList.add('active');
}

document.getElementById('modal-submit').addEventListener('click', () => {
    const levelIdx = STATE.activeLevel;
    const q = STATE.activeQuestions[STATE.currentQuestionIdx];
    const feedback = document.getElementById('modal-feedback');
    
    if (STATE.currentAnswer === null || STATE.currentAnswer === "") {
        feedback.innerText = "Please provide an answer first! ⚠️";
        feedback.style.color = "var(--gold)";
        modal.querySelector('.modal-content').style.animation = 'shake 0.4s ease';
        setTimeout(() => modal.querySelector('.modal-content').style.animation = '', 400);
        return;
    }

    let correct = false;
    if (q.type === 'slider') {
        correct = Math.abs(parseFloat(STATE.currentAnswer) - q.answer) < 0.1;
    } else if (q.type === 'sort') {
        correct = JSON.stringify(JSON.parse(STATE.currentAnswer || "[]")) === JSON.stringify(q.answer);
    } else if (q.type === 'match') {
        correct = parseInt(STATE.currentAnswer) === Object.keys(q.pairs).length;
    } else if (q.type === 'choice') {
        correct = STATE.currentAnswer === q.answer;
    } else if (q.type === 'click') {
        correct = parseInt(STATE.currentAnswer) === q.answer;
    } else if (q.type === 'text') {
        correct = STATE.currentAnswer.toLowerCase() === q.answer.toLowerCase();
    }

    if (correct) {
        sound.play('success');
        STATE.levelCorrectCount++;
        feedback.innerText = "Correct! ✨";
        feedback.style.color = "var(--success)";
    } else {
        sound.play('error');
        feedback.innerText = "Incorrect! ❌";
        feedback.style.color = "var(--error)";
        modal.querySelector('.modal-content').style.animation = 'shake 0.4s ease';
        setTimeout(() => modal.querySelector('.modal-content').style.animation = '', 400);
    }

    const submitBtn = document.getElementById('modal-submit');
    submitBtn.disabled = true;

    setTimeout(() => {
        submitBtn.disabled = false;
        STATE.currentQuestionIdx++;
        if (STATE.currentQuestionIdx < 5) {
            loadQuestion();
        } else {
            const success = STATE.levelCorrectCount >= 3;
            if (success) {
                alert(`Level Cleared! You solved ${STATE.levelCorrectCount}/5 correctly.`);
                STATE.claimedSpots.push(levelIdx);
                const pulse = document.getElementById(`pulse-${levelIdx}`);
                if (pulse) pulse.style.display = 'none';
                if (levelIdx + 1 < LEVELS.length) {
                    const nextPulse = document.getElementById(`pulse-${levelIdx + 1}`);
                    if (nextPulse) nextPulse.style.display = 'block';
                }
                updateMapImage();
                updateQuestLog();
            } else {
                alert(`Level Failed. You only solved ${STATE.levelCorrectCount}/5. Try again!`);
            }
            modal.classList.remove('active');
        }
    }, 1200);
});

document.querySelector('.modal-close').addEventListener('click', () => {
    modal.classList.remove('active');
});

const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
    STATE.darkMode = !STATE.darkMode;
    document.body.classList.toggle('dark-mode');
    themeToggle.querySelector('.theme-icon').innerText = STATE.darkMode ? '☀️' : '🌙';
    sound.play('click');
});

window.openLevel = openLevel;
