<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diagnostic Test — 20 Questions</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f5f7; color: #1d1d1f; }
        .container { display: flex; height: 100vh; }
        .sidebar { width: 260px; background: white; border-right: 1px solid #e5e5e7; padding: 20px; overflow-y: auto; }
        .sidebar-title { font-size: 11px; font-weight: 700; color: #999; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid #f0f0f0; }
        .question-btn { display: block; width: 100%; padding: 9px 12px; margin-bottom: 4px; border: none; background: #f5f5f7; color: #1d1d1f; border-radius: 6px; cursor: pointer; font-size: 12px; text-align: left; transition: all 0.2s; font-weight: 500; }
        .question-btn:hover { background: #e8e8ed; }
        .question-btn.active { background: #3844FF; color: white; box-shadow: 0 2px 8px rgba(56, 68, 255, 0.3); }
        .question-btn.completed { color: #34C759; font-weight: 600; }
        .question-btn.completed::before { content: "✓ "; margin-right: 4px; }
        .workspace { flex: 1; padding: 40px; overflow-y: auto; background: white; }
        .question-content { max-width: 900px; margin: 0 auto; }
        .question-header { margin-bottom: 30px; }
        .question-number { font-size: 13px; font-weight: 600; color: #3844FF; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
        .question-title { font-size: 32px; font-weight: 700; color: #1d1d1f; margin-bottom: 12px; line-height: 1.2; }
        .question-description { font-size: 18px; line-height: 1.8; color: #1d1d1f; margin-bottom: 30px; background: #f0f7ff; border-left: 4px solid #3844FF; padding: 20px; border-radius: 8px; font-weight: 500; }
        .code-block { background: #f5f5f7; color: #1d1d1f; border-left: 4px solid #3844FF; padding: 20px; margin: 25px 0; font-family: 'Monaco', 'Menlo', 'Courier New', monospace; font-size: 14px; line-height: 1.8; overflow-x: auto; border-radius: 8px; white-space: pre-wrap; word-wrap: break-word; }
        .keyword { color: #3844FF; font-weight: 600; }
        .string { color: #d73a49; }
        .number { color: #005cc5; }
        .comment { color: #6a737d; font-style: italic; }
        .interactive-area { background: #f9f9fb; border: 1px solid #e5e5e7; border-radius: 12px; padding: 30px; margin: 30px 0; }
        .grid-3x3 { display: grid; grid-template-columns: repeat(3, 90px); gap: 12px; margin: 20px 0; }
        .grid-cell { width: 90px; height: 90px; background: white; border: 2px solid #ddd; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; font-weight: 600; font-size: 18px; transition: all 0.2s; user-select: none; }
        .grid-cell:hover { border-color: #3844FF; box-shadow: 0 0 12px rgba(56, 68, 255, 0.2); }
        .grid-cell.clicked { background: #3844FF; color: white; border-color: #3844FF; }
        .grid-cell.error { animation: shake 0.3s; }
        @keyframes shake { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-5px); } 75% { transform: translateX(5px); } }
        .cell-label { font-size: 10px; color: #999; margin-top: 6px; }
        .grid-cell.clicked .cell-label { color: rgba(255, 255, 255, 0.8); }
        .progress { font-size: 14px; color: #666; margin: 20px 0; font-weight: 500; }
        .completion { padding: 16px; background: #d4edda; border: 2px solid #28a745; border-radius: 8px; color: #155724; font-weight: 600; margin-top: 30px; text-align: center; display: none; animation: slideIn 0.3s ease-out; }
        .completion.show { display: block; }
        @keyframes slideIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
        .number-line { position: relative; height: 70px; background: #f5f5f7; border-radius: 8px; margin: 30px 0; padding: 0 20px; display: flex; align-items: center; }
        .number-line-track { position: absolute; width: calc(100% - 40px); height: 6px; background: #ddd; border-radius: 3px; left: 20px; }
        .zone { position: absolute; height: 100%; display: flex; align-items: center; font-size: 12px; font-weight: 600; }
        .zone-label { position: absolute; top: -28px; left: 10px; font-size: 11px; font-weight: 700; color: white; padding: 2px 8px; border-radius: 4px; }
        .zone-F { background: rgba(255, 100, 100, 0.15); }
        .zone-F .zone-label { background: #ff6464; }
        .zone-C { background: rgba(255, 150, 100, 0.15); }
        .zone-C .zone-label { background: #ff9654; }
        .zone-B { background: rgba(255, 200, 100, 0.15); }
        .zone-B .zone-label { background: #ffc854; }
        .zone-A { background: rgba(100, 200, 100, 0.15); }
        .zone-A .zone-label { background: #64c864; }
        .marker { position: absolute; width: 22px; height: 50px; background: white; border: 3px solid #3844FF; border-radius: 4px; cursor: grab; top: 50%; transform: translateY(-50%); user-select: none; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700; color: #3844FF; box-shadow: 0 2px 8px rgba(56, 68, 255, 0.2); }
        .marker:active { cursor: grabbing; }
        .test-case-list { display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin: 20px 0; }
        .test-case { padding: 12px; border-radius: 6px; background: white; border: 1px solid #ddd; text-align: center; font-size: 12px; font-weight: 500; transition: all 0.2s; }
        .test-case.pass { background: #d4edda; border-color: #28a745; color: #155724; }
        .test-case.fail { background: #f8d7da; border-color: #f5c6cb; color: #721c24; }
        canvas { border: 1px solid #ddd; border-radius: 8px; background: white; max-width: 100%; }
        .slider-row { margin: 20px 0; display: grid; grid-template-columns: 60px 1fr 70px; gap: 15px; align-items: center; }
        .slider-label { font-size: 14px; font-weight: 600; color: #1d1d1f; }
        input[type="range"] { width: 100%; height: 6px; border-radius: 3px; background: #ddd; outline: none; -webkit-appearance: none; appearance: none; }
        input[type="range"]::-webkit-slider-thumb { -webkit-appearance: none; width: 20px; height: 20px; border-radius: 50%; background: #3844FF; cursor: pointer; box-shadow: 0 2px 8px rgba(56, 68, 255, 0.3); }
        input[type="range"]::-moz-range-thumb { width: 20px; height: 20px; border-radius: 50%; background: #3844FF; cursor: pointer; border: none; box-shadow: 0 2px 8px rgba(56, 68, 255, 0.3); }
        .slider-value { text-align: right; font-weight: 600; color: #3844FF; font-size: 14px; }
        .gate-button { padding: 12px 16px; background: white; border: 2px solid #3844FF; border-radius: 8px; color: #3844FF; font-weight: 600; cursor: pointer; transition: all 0.2s; font-size: 14px; }
        .gate-button:hover { background: #f0f7ff; box-shadow: 0 2px 8px rgba(56, 68, 255, 0.2); }
        .coming-soon { padding: 40px; text-align: center; background: #f9f9fb; border-radius: 8px; color: #999; font-style: italic; }
    </style>
</head>
<body>
    <div class="container">
        <div class="sidebar">
            <div class="sidebar-title">Introductory (Simple)</div>
            <button class="question-btn active" onclick="switchQuestion(1)">Q1: Classify Numbers</button>
            <button class="question-btn" onclick="switchQuestion(2)">Q2: Line Through Points</button>
            <button class="question-btn" onclick="switchQuestion(3)">Q3: Rectangle Constraints</button>
            <button class="question-btn" onclick="switchQuestion(4)">Q4: Range Checker</button>
            <button class="question-btn" onclick="switchQuestion(5)">Q5: Expression Tree</button>
            <div class="sidebar-title" style="margin-top: 20px;">Basic (Simple-Medium)</div>
            <button class="question-btn" onclick="switchQuestion(6)">Q6: Min Swaps Sort</button>
            <button class="question-btn" onclick="switchQuestion(7)">Q7: Sequence Pairs</button>
            <button class="question-btn" onclick="switchQuestion(8)">Q8: Polynomial Vis</button>
            <button class="question-btn" onclick="switchQuestion(9)">Q9: Paint Order</button>
            <button class="question-btn" onclick="switchQuestion(10)">Q10: Angle Range</button>
            <div class="sidebar-title" style="margin-top: 20px;">Intermediate (Medium)</div>
            <button class="question-btn" onclick="switchQuestion(11)">Q11: Equation Coeff</button>
            <button class="question-btn" onclick="switchQuestion(12)">Q12: String Transform</button>
            <button class="question-btn" onclick="switchQuestion(13)">Q13: Black Box</button>
            <button class="question-btn" onclick="switchQuestion(14)">Q14: Pathfinding</button>
            <button class="question-btn" onclick="switchQuestion(15)">Q15: String v2</button>
            <div class="sidebar-title" style="margin-top: 20px;">Advanced (Hard)</div>
            <button class="question-btn" onclick="switchQuestion(16)">Q16: XOR Circuit</button>
            <button class="question-btn" onclick="switchQuestion(17)">Q17: Three Planets</button>
            <button class="question-btn" onclick="switchQuestion(18)">Q18: Binary Operations</button>
            <button class="question-btn" onclick="switchQuestion(19)">Q19: Build Growth</button>
            <button class="question-btn" onclick="switchQuestion(20)">Q20: Divisibility</button>
        </div>
        <div class="workspace">
            <div class="question-content" id="content"></div>
        </div>
    </div>

    <script>
        const state = {
            current: 1,
            completed: new Set(),
            q1: { clicked: [], verified: false },
            q2: { boundaries: [30, 60, 90] },
            q3: { a: 2, b: 0, c: 0 },
            q4: { nodes: [], outSource: null },
            q5: { probes: {}, pipeline: [] },
            q6: {},
            q7: {},
            q8: {},
            q9: {},
            q10: {},
            q11: {},
            q12: {},
            q13: {},
            q14: {},
            q15: {},
            q16: {},
            q17: {},
            q18: {},
            q19: {},
            q20: {}
        };

        function switchQuestion(n) {
            state.current = n;
            document.querySelectorAll('.question-btn').forEach((btn, i) => {
                btn.classList.toggle('active', i + 1 === n);
            });
            render();
        }

        function render() {
            const content = document.getElementById('content');
            // Маппинг новый номер → старый номер функции
            // Новый порядок: Q9, Q8, Q16, Q11, Q7, Q15, Q12, Q13, Q1, Q2, Q3, Q10, Q5, Q6, Q14, Q4, Q17, Q18, Q19, Q20
            const mapping = [null, 9, 8, 16, 11, 7, 15, 12, 13, 1, 2, 3, 10, 5, 6, 14, 4, 17, 18, 19, 20];
            const oldQ = mapping[state.current];

            switch (oldQ) {
                case 1: content.innerHTML = renderQ1(); break;
                case 2: content.innerHTML = renderQ2(); break;
                case 3: content.innerHTML = renderQ3(); break;
                case 4: content.innerHTML = renderQ4(); break;
                case 5: content.innerHTML = renderQ5(); break;
                case 6: content.innerHTML = renderQ6(); break;
                case 7: content.innerHTML = renderQ7(); break;
                case 8: content.innerHTML = renderQ8(); break;
                case 9: content.innerHTML = renderQ9(); break;
                case 10: content.innerHTML = renderQ10(); break;
                case 11: content.innerHTML = renderQ11(); break;
                case 12: content.innerHTML = renderQ12(); break;
                case 13: content.innerHTML = renderQ13(); break;
                case 14: content.innerHTML = renderQ14(); break;
                case 15: content.innerHTML = renderQ15(); break;
                case 16: content.innerHTML = renderQ16(); break;
                case 17: content.innerHTML = renderQ17(); break;
                case 18: content.innerHTML = renderQ18(); break;
                case 19: content.innerHTML = renderQ19(); break;
                case 20: content.innerHTML = renderQ20(); break;
                default: content.innerHTML = `<div class="coming-soon">Question not found</div>`;
            }
        }

        function renderQ1() {
            const grid = [[7, 4, 9], [2, 5, 8], [3, 6, 1]];
            const correct = [[2,0], [2,2], [1,1], [0,0], [0,2]];

            let html = `<div class="question-header"><div class="question-number">Introductory • Programming</div>
                <div class="question-title">Q9: Paint Order</div></div>
                <div class="question-description">Click cells in the exact order the code will paint them. Select all 5, then click Check.</div>
                <div class="code-block"><span class="keyword">for</span> i <span class="keyword">in</span> <span class="keyword">range</span>(<span class="number">2</span>, <span class="number">-1</span>, <span class="number">-1</span>):
    <span class="keyword">for</span> j <span class="keyword">in</span> <span class="keyword">range</span>(<span class="number">3</span>):
        <span class="keyword">if</span> (i + j) % <span class="number">2</span> == <span class="number">0</span>:
            <span class="keyword">paint</span>(grid[i][j])</div>
                <div class="interactive-area"><div class="grid-3x3">`;
            for (let i = 0; i < 3; i++) {
                for (let j = 0; j < 3; j++) {
                    const clickIndex = state.q1.clicked.findIndex(c => c[0] === i && c[1] === j);
                    const isSelected = clickIndex !== -1;
                    html += `<div class="grid-cell ${isSelected ? 'clicked' : ''}"
                             onclick="toggleQ1Cell(${i}, ${j})"
                             data-q1-index="${clickIndex !== -1 ? clickIndex + 1 : ''}">
                        ${grid[i][j]}<span class="cell-label">${isSelected ? clickIndex + 1 : '[' + i + ',' + j + ']'}</span></div>`;
                }
            }
            html += `</div>
                <div class="progress">Selected: ${state.q1.clicked.length} / 5</div>
                <div style="margin-top: 20px;">`;

            if (state.q1.clicked.length > 0) {
                html += `<button onclick="undoQ1()" style="margin-right: 12px; padding: 8px 12px; background: #ccc; color: #333; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">← Undo</button>`;
            }

            if (state.q1.clicked.length === 5) {
                html += `<button onclick="checkQ1()" style="padding: 8px 24px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">Check Answer</button>`;
            }

            html += `</div>`;

            if (state.q1.verified) {
                html += `<div class="completion show">✓ Correct! You traced the nested loops correctly.</div>`;
                markCompleted(1);
            }
            html += `<button onclick="resetQuestion(1)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        function toggleQ1Cell(i, j) {
            if (state.q1.clicked.length >= 5) return;
            const idx = state.q1.clicked.findIndex(c => c[0] === i && c[1] === j);
            if (idx === -1) {
                state.q1.clicked.push([i, j]);
            } else {
                state.q1.clicked.splice(idx, 1);
            }
            render();
        }

        function undoQ1() {
            if (state.q1.clicked.length > 0) {
                state.q1.clicked.pop();
                render();
            }
        }

        function checkQ1() {
            const correct = [[2,0], [2,2], [1,1], [0,0], [0,2]];
            const isCorrect = state.q1.clicked.length === correct.length &&
                correct.every((c, i) => JSON.stringify(state.q1.clicked[i]) === JSON.stringify(c));
            if (!isCorrect) {
                state.q1.clicked = [];
                state.q1.verified = false;
            } else {
                state.q1.verified = true;
            }
            render();
        }

        function renderQ2() {
            const testCases = [
                {val: 49, expected: 'F'}, {val: 50, expected: 'C'},
                {val: 69, expected: 'C'}, {val: 70, expected: 'B'},
                {val: 84, expected: 'B'}, {val: 85, expected: 'A'}
            ];
            const [a, b, c] = state.q2.boundaries;
            const allPass = testCases.every(tc => getGrade(tc.val, a, b, c) === tc.expected);

            let html = `<div class="question-header"><div class="question-number">Intermediate • Programming, Reasoning</div>
                <div class="question-title">Q10: Angle Range</div></div>
                <div class="question-description">Adjust three boundaries so all test cases pass.</div>
                <div class="code-block"><span class="keyword">if</span> score < ⟦A⟧:
    <span class="keyword">return</span> <span class="string">"F"</span>
<span class="keyword">elif</span> score < ⟦B⟧:
    <span class="keyword">return</span> <span class="string">"C"</span>
<span class="keyword">elif</span> score < ⟦C⟧:
    <span class="keyword">return</span> <span class="string">"B"</span>
<span class="keyword">else</span>:
    <span class="keyword">return</span> <span class="string">"A"</span></div>
                <div class="interactive-area"><div class="number-line">
                    <div class="number-line-track"></div>
                    <div class="zone zone-F" style="left: 0; width: ${(a/100)*100}%;"><span class="zone-label">F</span></div>
                    <div class="zone zone-C" style="left: ${(a/100)*100}%; width: ${((b-a)/100)*100}%;"><span class="zone-label">C</span></div>
                    <div class="zone zone-B" style="left: ${(b/100)*100}%; width: ${((c-b)/100)*100}%;"><span class="zone-label">B</span></div>
                    <div class="zone zone-A" style="left: ${(c/100)*100}%; width: ${((100-c)/100)*100}%;"><span class="zone-label">A</span></div>
                    <div class="marker" style="left: ${a}%" onmousedown="dragMarker(event, 0)">A</div>
                    <div class="marker" style="left: ${b}%" onmousedown="dragMarker(event, 1)">B</div>
                    <div class="marker" style="left: ${c}%" onmousedown="dragMarker(event, 2)">C</div>
                </div><div class="test-case-list">`;
            testCases.forEach(tc => {
                const grade = getGrade(tc.val, a, b, c);
                const pass = grade === tc.expected;
                html += `<div class="test-case ${pass ? 'pass' : 'fail'}">${tc.val} → ${grade}</div>`;
            });
            html += `<button onclick="resetQuestion(2)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            if (allPass && a === 50 && b === 70 && c === 85) {
                html += `<div class="completion show">✓ Correct! All test cases pass.</div>`;
                markCompleted(2);
            }
            html += `<button onclick="resetQuestion(2)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        function getGrade(score, a, b, c) {
            if (score < a) return 'F';
            if (score < b) return 'C';
            if (score < c) return 'B';
            return 'A';
        }

        function dragMarker(e, idx) {
            const line = e.target.parentElement;
            const rect = line.getBoundingClientRect();
            const startX = e.clientX;
            const startVal = state.q2.boundaries[idx];

            function move(me) {
                const delta = me.clientX - startX;
                const newVal = Math.max(0, Math.min(100, startVal + (delta / rect.width) * 100));
                state.q2.boundaries[idx] = Math.round(newVal);
                render();
            }

            function stop() {
                document.removeEventListener('mousemove', move);
                document.removeEventListener('mouseup', stop);
            }

            document.addEventListener('mousemove', move);
            document.addEventListener('mouseup', stop);
        }

        function renderQ3() {
            const {a, b, c} = state.q3;
            const points = [[0, 3], [1, 0], [3, 0]];
            const check3 = checkParabola(a, b, c, points);

            let html = `<div class="question-header"><div class="question-number">Intermediate • Mathematics</div>
                <div class="question-title">Q11: Equation Coeff</div></div>
                <div class="question-description">Adjust a, b, c so the parabola passes through all three rings.</div>
                <div class="code-block">y = a·x² + b·x + c</div>
                <div class="interactive-area"><canvas id="canvas" width="500" height="400"></canvas>
                <div class="slider-row">
                    <div class="slider-label">a:</div>
                    <input type="range" min="-5" max="5" step="0.1" value="${a}" oninput="state.q3.a = parseFloat(this.value); render()">
                    <input type="number" step="0.01" value="${a.toFixed(2)}" onchange="state.q3.a = parseFloat(this.value); render();" style="width: 70px; padding: 4px; border: 1px solid #ddd; border-radius: 4px; margin-left: 10px;">
                </div>
                <div class="slider-row">
                    <div class="slider-label">b:</div>
                    <input type="range" min="-10" max="10" step="0.1" value="${b}" oninput="state.q3.b = parseFloat(this.value); render()">
                    <input type="number" step="0.01" value="${b.toFixed(2)}" onchange="state.q3.b = parseFloat(this.value); render();" style="width: 70px; padding: 4px; border: 1px solid #ddd; border-radius: 4px; margin-left: 10px;">
                </div>
                <div class="slider-row">
                    <div class="slider-label">c:</div>
                    <input type="range" min="-5" max="10" step="0.1" value="${c}" oninput="state.q3.c = parseFloat(this.value); render()">
                    <input type="number" step="0.01" value="${c.toFixed(2)}" onchange="state.q3.c = parseFloat(this.value); render();" style="width: 70px; padding: 4px; border: 1px solid #ddd; border-radius: 4px; margin-left: 10px;">
                </div>`;
            if (check3) {
                html += `<div class="completion show">✓ Correct! Parabola passes through all points.</div>`;
                markCompleted(3);
            }
            html += `<button onclick="resetQuestion(3)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            setTimeout(() => drawParabola(), 0);
            return html;
        }

        function checkParabola(a, b, c, points) {
            const tol = 0.05;
            return points.every(p => Math.abs(a * p[0] * p[0] + b * p[0] + c - p[1]) < tol);
        }

        function drawParabola() {
            const canvas = document.getElementById('canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = canvas.width, h = canvas.height;
            const cx = w / 2, cy = h / 2;
            const scale = 40;

            ctx.clearRect(0, 0, w, h);
            ctx.strokeStyle = '#eee';
            ctx.lineWidth = 1;
            for (let i = -5; i <= 5; i++) {
                ctx.beginPath();
                ctx.moveTo(cx + i * scale, 0);
                ctx.lineTo(cx + i * scale, h);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(0, cy - i * scale);
                ctx.lineTo(w, cy - i * scale);
                ctx.stroke();
            }
            ctx.strokeStyle = '#333';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(cx, 0);
            ctx.lineTo(cx, h);
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(0, cy);
            ctx.lineTo(w, cy);
            ctx.stroke();
            ctx.strokeStyle = '#3844FF';
            ctx.lineWidth = 3;
            ctx.beginPath();
            for (let px = -5; px <= 5; px += 0.1) {
                const py = state.q3.a * px * px + state.q3.b * px + state.q3.c;
                const x = cx + px * scale;
                const y = cy - py * scale;
                if (Math.abs(px + 5) < 0.01) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.stroke();
            const targets = [[0, 3], [1, 0], [3, 0]];
            targets.forEach(p => {
                const x = cx + p[0] * scale;
                const y = cy - p[1] * scale;
                ctx.strokeStyle = '#34C759';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.arc(x, y, 14, 0, 2 * Math.PI);
                ctx.stroke();
            });
        }

        function renderQ4() {
            let html = `<div class="question-header"><div class="question-number">Advanced • Programming, Reasoning</div>
                <div class="question-title">Q16: Build XOR Circuit</div></div>
                <div class="question-description">Add gates and connect inputs to build a circuit that outputs XOR.</div>
                <div class="code-block"><code>🎯 Target: XOR (A ⊕ B)
A | B | Out
0 | 0 |  0
0 | 1 |  1
1 | 0 |  1
1 | 1 |  0</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: 200px 1fr 130px; gap: 20px;">
                        <div>
                            <strong style="display: block; margin-bottom: 12px;">🎛️ Add Gates</strong>
                            <button class="gate-button" onclick="q4AddGate('AND')" style="width: 100%; margin-bottom: 6px; padding: 6px; font-size: 12px;">+ AND</button>
                            <button class="gate-button" onclick="q4AddGate('OR')" style="width: 100%; margin-bottom: 6px; padding: 6px; font-size: 12px;">+ OR</button>
                            <button class="gate-button" onclick="q4AddGate('NOT')" style="width: 100%; margin-bottom: 12px; padding: 6px; font-size: 12px;">+ NOT</button>
                            <div id="q4GateList" style="background: #f9f9fb; padding: 8px; border-radius: 6px; font-size: 11px;"></div>
                        </div>
                        <canvas id="q4Canvas" width="400" height="280" style="background: white; border: 1px solid #ddd; border-radius: 8px;"></canvas>
                        <div>
                            <strong style="display: block; margin-bottom: 8px; font-size: 12px;">📊 Output</strong>
                            <div id="q4TruthTable" style="font-family: monospace; font-size: 10px; background: white; padding: 8px; border: 1px solid #ddd; border-radius: 6px; line-height: 1.4;"></div>
                            <div id="q4OutputSelector" style="margin-top: 12px; padding: 8px; background: #e7f3ff; border-radius: 6px; border: 1px solid #3844FF;">
                                <label style="display: block; font-size: 10px; color: #666; margin-bottom: 4px;">Final output:</label>
                                <select id="q4OutputSelect" onchange="q4SetOutput(this.value)" style="width: 100%; padding: 4px; font-size: 11px; border: 1px solid #3844FF; border-radius: 4px;">
                                    <option value="">— Select —</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <button onclick="resetQuestion(4)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button>
                </div>`;

            setTimeout(() => {
                q4Draw();
                q4UpdateTruthTable();
            }, 0);
            return html;
        }

        function q4AddGate(type) {
            if (!state.q4.nodes) state.q4.nodes = [];
            const idx = state.q4.nodes.length + 1;
            state.q4.nodes.push({
                id: 'G' + idx,
                type,
                in1: null,
                in2: null
            });
            q4RenderGateList();
            q4Draw();
            q4UpdateTruthTable();
        }

        function q4RenderGateList() {
            const list = document.getElementById('q4GateList');
            if (!list || !state.q4.nodes) return;

            let html = '';
            state.q4.nodes.forEach((gate, idx) => {
                const num = idx + 1;
                html += `<div style="background: white; padding: 8px; border-radius: 4px; margin-bottom: 6px; border: 1px solid #ddd;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <strong style="font-size: 11px;">G${num}: ${gate.type}</strong>
                        <button onclick="q4RemoveGate(${idx})" style="background: #ff4444; color: white; border: none; border-radius: 3px; padding: 2px 6px; cursor: pointer; font-size: 9px;">✕</button>
                    </div>
                    ${gate.type !== 'NOT' ? `<select onchange="q4SetInput('${gate.id}', 0, this.value)" style="width: 100%; padding: 3px; font-size: 10px; border: 1px solid #ddd; border-radius: 3px; margin-bottom: 3px;">
                        <option value="">In1: —</option>
                        <option value="A" ${gate.in1 === 'A' ? 'selected' : ''}>In1: A</option>
                        <option value="B" ${gate.in1 === 'B' ? 'selected' : ''}>In1: B</option>
                        ${state.q4.nodes.slice(0, idx).map((g, i) => `<option value="G${i+1}" ${gate.in1 === 'G' + (i+1) ? 'selected' : ''}>In1: G${i+1}</option>`).join('')}
                    </select>` : ''}
                    ${gate.type !== 'NOT' ? `<select onchange="q4SetInput('${gate.id}', 1, this.value)" style="width: 100%; padding: 3px; font-size: 10px; border: 1px solid #ddd; border-radius: 3px;">
                        <option value="">In2: —</option>
                        <option value="A" ${gate.in2 === 'A' ? 'selected' : ''}>In2: A</option>
                        <option value="B" ${gate.in2 === 'B' ? 'selected' : ''}>In2: B</option>
                        ${state.q4.nodes.slice(0, idx).map((g, i) => `<option value="G${i+1}" ${gate.in2 === 'G' + (i+1) ? 'selected' : ''}>In2: G${i+1}</option>`).join('')}
                    </select>` : `<select onchange="q4SetInput('${gate.id}', 0, this.value)" style="width: 100%; padding: 3px; font-size: 10px; border: 1px solid #ddd; border-radius: 3px;">
                        <option value="">Input: —</option>
                        <option value="A" ${gate.in1 === 'A' ? 'selected' : ''}>Input: A</option>
                        <option value="B" ${gate.in1 === 'B' ? 'selected' : ''}>Input: B</option>
                        ${state.q4.nodes.slice(0, idx).map((g, i) => `<option value="G${i+1}" ${gate.in1 === 'G' + (i+1) ? 'selected' : ''}>Input: G${i+1}</option>`).join('')}
                    </select>`}
                </div>`;
            });

            if (state.q4.nodes.length === 0) {
                html = `<div style="color: #999; font-size: 10px;">Add gates →</div>`;
            }

            list.innerHTML = html;

            const select = document.getElementById('q4OutputSelect');
            if (select) {
                let options = `<option value="">— Select —</option>
                    <option value="A" ${state.q4.outSource === 'A' ? 'selected' : ''}>A</option>
                    <option value="B" ${state.q4.outSource === 'B' ? 'selected' : ''}>B</option>`;
                if (state.q4.nodes) {
                    state.q4.nodes.forEach((g, i) => {
                        options += `<option value="G${i+1}" ${state.q4.outSource === 'G' + (i+1) ? 'selected' : ''}>G${i+1}</option>`;
                    });
                }
                select.innerHTML = options;
            }
        }

        function q4SetInput(gateId, inputIdx, value) {
            const gate = state.q4.nodes.find(g => g.id === gateId);
            if (gate) {
                if (inputIdx === 0) gate.in1 = value || null;
                else gate.in2 = value || null;
                q4Draw();
                q4UpdateTruthTable();
            }
        }

        function q4SetOutput(value) {
            state.q4.outSource = value || null;
            q4Draw();
            q4UpdateTruthTable();
        }

        function q4RemoveGate(idx) {
            const gateId = 'G' + (idx + 1);
            state.q4.nodes.splice(idx, 1);
            if (state.q4.outSource === gateId) state.q4.outSource = null;
            state.q4.nodes.forEach((g, i) => {
                if (g.in1 === gateId || g.in2 === gateId) {
                    if (g.in1 === gateId) g.in1 = null;
                    if (g.in2 === gateId) g.in2 = null;
                }
            });
            q4RenderGateList();
            q4Draw();
            q4UpdateTruthTable();
        }

        function q4Draw() {
            const canvas = document.getElementById('q4Canvas');
            if (!canvas || !state.q4.nodes) return;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#fff';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.strokeStyle = '#eee';
            ctx.lineWidth = 1;
            ctx.strokeRect(0, 0, canvas.width, canvas.height);

            const inputAX = 20, inputAY = 60;
            const inputBX = 20, inputBY = 140;

            ctx.fillStyle = '#3844FF';
            ctx.font = 'bold 12px sans-serif';
            ctx.fillText('A', inputAX + 15, inputAY + 5);
            ctx.fillRect(inputAX - 8, inputAY - 8, 16, 16);

            ctx.fillText('B', inputBX + 15, inputBY + 5);
            ctx.fillRect(inputBX - 8, inputBY - 8, 16, 16);

            const gateY = 40;
            const gateSpacingX = 110;
            const gateW = 50, gateH = 40;

            state.q4.nodes.forEach((gate, idx) => {
                const x = 80 + idx * gateSpacingX;
                const y = gateY;

                ctx.fillStyle = '#e7f3ff';
                ctx.strokeStyle = '#3844FF';
                ctx.lineWidth = 2;
                ctx.fillRect(x, y, gateW, gateH);
                ctx.strokeRect(x, y, gateW, gateH);

                ctx.fillStyle = '#1d1d1f';
                ctx.font = 'bold 14px sans-serif';
                ctx.textAlign = 'center';
                const sym = gate.type === 'AND' ? '∧' : gate.type === 'OR' ? '∨' : '¬';
                ctx.fillText(sym, x + gateW / 2, y + gateH / 2 + 5);

                if (gate.in1) {
                    const [sx, sy] = q4GetSourcePos(gate.in1);
                    ctx.strokeStyle = '#3844FF';
                    ctx.lineWidth = 2;
                    ctx.beginPath();
                    ctx.moveTo(sx + 8, sy);
                    ctx.lineTo(x - 5, y + 12);
                    ctx.stroke();
                }

                if (gate.in2) {
                    const [sx, sy] = q4GetSourcePos(gate.in2);
                    ctx.strokeStyle = '#3844FF';
                    ctx.lineWidth = 2;
                    ctx.beginPath();
                    ctx.moveTo(sx + 8, sy);
                    ctx.lineTo(x - 5, y + 28);
                    ctx.stroke();
                }
            });

            if (state.q4.outSource) {
                const [sx, sy] = q4GetSourcePos(state.q4.outSource);
                ctx.strokeStyle = '#34C759';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(sx + 8, sy);
                ctx.lineTo(360, 100);
                ctx.stroke();

                ctx.fillStyle = '#34C759';
                ctx.fillRect(360 - 8, 100 - 8, 16, 16);
                ctx.fillStyle = '#fff';
                ctx.font = 'bold 12px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('✓', 360, 105);
            }
        }

        function q4GetSourcePos(sourceId) {
            if (sourceId === 'A') return [20, 60];
            if (sourceId === 'B') return [20, 140];
            const match = sourceId.match(/G(\d+)/);
            if (match) {
                const idx = parseInt(match[1]) - 1;
                const x = 80 + idx * 110 + 50;
                const y = 40 + 20;
                return [x, y];
            }
            return [0, 0];
        }

        function q4UpdateTruthTable() {
            const area = document.getElementById('q4TruthTable');
            if (!area) return;

            const xorTable = [[0,0,0], [0,1,1], [1,0,1], [1,1,0]];
            let allPass = true;

            let html = `<div style="margin-bottom: 6px;"><strong>Expected</strong></div>A B X<br>`;

            xorTable.forEach(row => {
                const [a, b, expected] = row;
                html += `${a} ${b} ${expected}<br>`;
            });

            html += `<div style="margin-top: 8px; margin-bottom: 6px;"><strong>Actual</strong></div>A B O<br>`;

            xorTable.forEach(row => {
                const [a, b, expected] = row;
                const actual = evalGate(state.q4.outSource, a, b);
                const match = actual === expected;
                if (!match) allPass = false;
                const color = actual === null ? '#999' : (match ? '#34C759' : '#ff4444');
                const display = actual === null ? '?' : actual;
                html += `<span style="color: ${color};">${a} ${b} ${display}</span><br>`;
            });

            if (allPass && state.q4.outSource) {
                html += `<div style="margin-top: 8px; padding: 6px; background: #d4edda; border: 1px solid #28a745; border-radius: 4px; color: #155724; font-weight: 600; font-size: 10px; text-align: center;">✓ Correct!</div>`;
                markCompleted(4);
            }

            area.innerHTML = html;
        }

        function evalGate(sourceId, a, b) {
            if (sourceId === 'A') return a;
            if (sourceId === 'B') return b;
            const node = state.q4.nodes.find(n => n.id === sourceId);
            if (!node) return null;
            const in1 = evalGate(node.in1, a, b);
            const in2 = evalGate(node.in2, a, b);
            if (in1 === null || (node.type !== 'NOT' && in2 === null)) return null;
            if (node.type === 'AND') return (in1 && in2) ? 1 : 0;
            if (node.type === 'OR') return (in1 || in2) ? 1 : 0;
            if (node.type === 'NOT') return in1 ? 0 : 1;
            return null;
        }

        function updateTruthTable() {
            const area = document.getElementById('truthTable');
            if (!area) return;

            const xorTable = [[0,0,0], [0,1,1], [1,0,1], [1,1,0]];
            let allPass = true;

            let html = `<table style="width: 100%; border-collapse: collapse;">
                <tr style="border-bottom: 1px solid #ddd;">
                    <td style="padding: 4px;">A</td><td style="padding: 4px;">B</td><td style="padding: 4px;">Out</td>
                </tr>`;

            xorTable.forEach(row => {
                const [a, b, expected] = row;
                const actual = evalGate(state.q4.outSource, a, b);
                const match = actual === expected;
                if (!match) allPass = false;
                const color = actual === null ? '#ccc' : (match ? '#34C759' : '#ff4444');
                const display = actual === null ? '?' : actual;
                html += `<tr style="border-bottom: 1px solid #eee;"><td style="padding: 4px;">${a}</td><td style="padding: 4px;">${b}</td><td style="padding: 4px; color: ${color}; font-weight: 600;">${display}</td></tr>`;
            });

            html += `</table>`;
            if (allPass && state.q4.outSource) {
                html += `<div class="completion show" style="margin-top: 15px;">✓ XOR circuit complete!</div>`;
                markCompleted(4);
            }

            area.innerHTML = html;
        }

        function renderQ5() {
            if (!state.q5.probes) state.q5.probes = {};
            if (!state.q5.pipeline) state.q5.pipeline = [];

            let html = `<div class="question-header"><div class="question-number">Advanced • Programming, Reasoning</div>
                <div class="question-title">Q13: Black Box</div></div>
                <div class="question-description">Discover a hidden function by probing it, then build a pipeline that replicates its behavior on all test inputs.</div>
                <div class="code-block"><code>Test range: x = 0..20 (21 test cases)
Probe any value to learn the pattern.
Assemble pipeline to match on ALL inputs.</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div>
                            <strong>🔬 Probe Function</strong>
                            <div style="margin: 10px 0;">
                                <input type="number" id="probeInput" min="0" max="20" value="0" style="padding: 8px; width: 60px; border: 1px solid #ddd; border-radius: 4px;">
                                <button onclick="probeFunction()" style="padding: 8px 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Get f(x)</button>
                            </div>
                            <div id="probeLog" style="background: white; padding: 10px; border: 1px solid #ddd; border-radius: 6px; min-height: 150px; font-family: monospace; font-size: 11px; overflow-y: auto;"></div>
                        </div>
                        <div>
                            <strong>⚙️ Build Pipeline</strong>
                            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin: 10px 0;">
                                <button class="gate-button" onclick="addQ5Block('×2')" style="padding: 8px; font-size: 12px;">×2</button>
                                <button class="gate-button" onclick="addQ5Block('×3')" style="padding: 8px; font-size: 12px;">×3</button>
                                <button class="gate-button" onclick="addQ5Block('+1')" style="padding: 8px; font-size: 12px;">+1</button>
                                <button class="gate-button" onclick="addQ5Block('+2')" style="padding: 8px; font-size: 12px;">+2</button>
                                <button class="gate-button" onclick="addQ5Block('−1')" style="padding: 8px; font-size: 12px;">−1</button>
                                <button class="gate-button" onclick="addQ5Block('mod 5')" style="padding: 8px; font-size: 12px;">mod 5</button>
                                <button class="gate-button" onclick="addQ5Block('mod 7')" style="padding: 8px; font-size: 12px;">mod 7</button>
                                <button class="gate-button" onclick="addQ5Block('x²')" style="padding: 8px; font-size: 12px;">x²</button>
                            </div>
                            <div id="pipeline" style="background: white; padding: 10px; border: 1px solid #ddd; border-radius: 6px; min-height: 60px; display: flex; flex-wrap: wrap; gap: 6px; align-items: center;"></div>
                            <div id="resultQ5" style="margin-top: 10px; padding: 8px; background: #e7f3ff; border-radius: 6px; font-family: monospace; font-size: 12px; font-weight: 600;">Result for x=0: —</div>
                            <div id="matchCount" style="margin-top: 10px; text-align: center; font-weight: 600; padding: 8px; background: #f0f7ff; border-radius: 6px;">Match: 0 / 21</div>
                            <button id="submitQ5" onclick="submitQ5()" style="margin-top: 12px; width: 100%; padding: 10px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px; display: none;">✓ Submit Pipeline</button>
                            <div id="q5TestResults" style="margin-top: 12px; max-height: 150px; overflow-y: auto; font-family: monospace; font-size: 10px; background: white; padding: 8px; border: 1px solid #ddd; border-radius: 6px;"></div>
                        </div>
                    </div>
                    <button onclick="resetQuestion(5)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button>
                </div>`;

            updateQ5Probes();
            setTimeout(() => checkQ5Pipeline(), 0);
            return html;
        }

        function probeFunction() {
            const input = parseInt(document.getElementById('probeInput').value);
            if (isNaN(input) || input < 0 || input > 20) return;
            if (!state.q5.probes) state.q5.probes = {};
            const result = (input * 3 + 1) % 7;
            state.q5.probes[input] = result;
            updateQ5Probes();
            checkQ5Pipeline();
        }

        function updateQ5Probes() {
            const log = document.getElementById('probeLog');
            if (!log) return;
            if (!state.q5.probes || Object.keys(state.q5.probes).length === 0) {
                log.innerHTML = '[No probes yet]';
                return;
            }
            let html = Object.keys(state.q5.probes).sort((a,b) => parseInt(a) - parseInt(b)).map(x => `x=${x} → ${state.q5.probes[x]}`).join('<br>');
            log.innerHTML = html;
        }

        function addQ5Block(op) {
            if (!state.q5.pipeline) state.q5.pipeline = [];
            state.q5.pipeline.push(op);
            checkQ5Pipeline();
        }

        function removeQ5Block(idx) {
            state.q5.pipeline.splice(idx, 1);
            checkQ5Pipeline();
        }

        function checkQ5Pipeline() {
            const counter = document.getElementById('matchCount');
            const area = document.getElementById('pipeline');
            const resultArea = document.getElementById('resultQ5');
            const testResults = document.getElementById('q5TestResults');
            if (!counter || !area) return;

            if (!state.q5.pipeline || state.q5.pipeline.length === 0) {
                area.innerHTML = '<div style="color: #999;">Pipeline: [empty]</div>';
                counter.innerHTML = 'Match: 0 / 21';
                resultArea.innerHTML = 'Result for x=0: —';
                testResults.innerHTML = '';
                return;
            }

            let match = 0;
            let testHtml = `<table style="width: 100%; border-collapse: collapse; font-size: 11px;">
                <tr style="background: #f0f0f0; font-weight: 600; border-bottom: 2px solid #ddd;">
                    <td style="padding: 4px; text-align: center;">x</td>
                    <td style="padding: 4px; text-align: center;">Expected</td>
                    <td style="padding: 4px; text-align: center;">Actual</td>
                    <td style="padding: 4px; text-align: center;">Result</td>
                </tr>`;

            for (let x = 0; x <= 20; x++) {
                const actual = applyQ5Pipeline(state.q5.pipeline, x);
                const expected = (x * 3 + 1) % 7;
                const isMatch = actual === expected;
                if (isMatch) match++;
                const bgColor = isMatch ? '#f0fff4' : '#fff5f5';
                const textColor = isMatch ? '#34C759' : '#ff4444';
                const status = isMatch ? '✓' : '✗';
                testHtml += `<tr style="background: ${bgColor}; border-bottom: 1px solid #eee;">
                    <td style="padding: 4px; text-align: center;">${x}</td>
                    <td style="padding: 4px; text-align: center;">${expected}</td>
                    <td style="padding: 4px; text-align: center; font-weight: 600; color: ${textColor};">${actual}</td>
                    <td style="padding: 4px; text-align: center; color: ${textColor}; font-weight: 700;">${status}</td>
                </tr>`;
            }
            testHtml += '</table>';
            testResults.innerHTML = testHtml;

            const hiddenTests = [35, 100, 7, 13];
            let allMatch = match === 21;
            hiddenTests.forEach(x => {
                const actual = applyQ5Pipeline(state.q5.pipeline, x);
                const expected = (x * 3 + 1) % 7;
                if (actual !== expected) allMatch = false;
            });

            let pipeDisplay = state.q5.pipeline.map((p, i) =>
                `<span style="background: #3844FF; color: white; padding: 6px 10px; border-radius: 4px; display: inline-flex; align-items: center; gap: 6px; font-size: 12px;">
                    ${p}
                    <button onclick="removeQ5Block(${i})" style="background: rgba(255,255,255,0.3); border: none; color: white; padding: 2px 4px; border-radius: 2px; cursor: pointer; font-weight: 600; font-size: 11px;">×</button>
                </span>`
            ).join(' ');
            area.innerHTML = pipeDisplay;

            const result0 = applyQ5Pipeline(state.q5.pipeline, 0);
            resultArea.innerHTML = `Result for x=0: <strong>${result0}</strong>`;

            counter.innerHTML = `Match: ${match} / 21`;

            const submitBtn = document.getElementById('submitQ5');
            if (submitBtn) {
                if (allMatch) {
                    submitBtn.style.display = 'block';
                    submitBtn.style.background = '#34C759';
                    counter.innerHTML = `<span style="color: #34C759; font-weight: 700;">✓ All tests pass! (${match}/21)</span>`;
                    counter.style.background = '#d4edda';
                } else {
                    submitBtn.style.display = 'none';
                }
            }
        }

        function submitQ5() {
            markCompleted(5);
            const area = document.getElementById('pipeline');
            if (area) {
                area.innerHTML += `<div class="completion show" style="margin-top: 10px; width: 100%; text-align: center;">✓ Pipeline submitted successfully!</div>`;
            }
            document.getElementById('submitQ5').style.display = 'none';
        }

        function applyQ5Pipeline(pipeline, x) {
            let result = x;
            pipeline.forEach(op => {
                if (op === '×2') result *= 2;
                else if (op === '×3') result *= 3;
                else if (op === '+1') result += 1;
                else if (op === '+2') result += 2;
                else if (op === '−1') result -= 1;
                else if (op === 'mod 5') result = result % 5;
                else if (op === 'mod 7') result = result % 7;
                else if (op === 'x²') result = result * result;
            });
            return result;
        }

        // ====== Q6: Route to Number ======
        function renderQ6() {
            if (!state.q6.grid) {
                state.q6.grid = [
                    ['+2', '×2', '+1', '−1'],
                    ['×3', '+4', '×2', '+5'],
                    ['+1', '−2', '+6', '×2'],
                    ['×2', '+3', '−1', '+4']
                ];
                state.q6.current = 3;
                state.q6.path = [[0,0]];
                state.q6.target = 48;
            }

            let html = `<div class="question-header"><div class="question-number">Intermediate • Mathematics, Reasoning</div>
                <div class="question-title">Q14: Pathfinding</div></div>
                <div class="question-description">Navigate right or down from start to reach the target number.</div>
                <div class="code-block"><code>Start: 3 | Current: ${state.q6.current} | Goal: ${state.q6.target}
Only move RIGHT or DOWN!</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: repeat(4, 85px); gap: 10px; margin: 20px 0;">`;

            state.q6.grid.forEach((row, i) => {
                row.forEach((op, j) => {
                    const isPath = state.q6.path.some(p => p[0] === i && p[1] === j);
                    const last = state.q6.path[state.q6.path.length-1];
                    const canMove = (i === last[0] && j === last[1] + 1) || (j === last[1] && i === last[0] + 1);
                    html += `<div style="padding: 12px; background: ${isPath ? '#3844FF' : '#f0f7ff'}; color: ${isPath ? 'white' : '#1d1d1f'}; border-radius: 8px; text-align: center; cursor: ${canMove ? 'pointer' : 'default'}; border: 2px solid ${isPath ? '#3844FF' : '#ddd'}; font-size: 14px; font-weight: 600;" onclick="${canMove ? `moveQ6(${i}, ${j})` : ''}">
                        ${op}</div>`;
                });
            });

            html += `<button onclick="resetQuestion(6)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            if (state.q6.current === state.q6.target && state.q6.path[state.q6.path.length-1][0] === 3 && state.q6.path[state.q6.path.length-1][1] === 3) {
                html += `<div class="completion show">✓ Reached target!</div>`;
                markCompleted(6);
            }
            html += `<button onclick="resetQ6()" style="margin-top: 15px; padding: 8px 12px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Reset</button>
                </div>`;
            return html;
        }

        function moveQ6(i, j) {
            const last = state.q6.path[state.q6.path.length - 1];
            if (!((i === last[0] && j === last[1] + 1) || (j === last[1] && i === last[0] + 1))) return;

            const op = state.q6.grid[i][j];
            if (op[0] === '+') state.q6.current += parseInt(op.substr(1));
            else if (op[0] === '−') state.q6.current -= parseInt(op.substr(1));
            else if (op[0] === '×') state.q6.current *= parseInt(op.substr(1));

            state.q6.path.push([i, j]);
            render();
        }

        function resetQ6() {
            state.q6.current = 3;
            state.q6.path = [[0,0]];
            render();
        }

        // ====== Q7: Fix Pattern ======
        function renderQ7() {
            if (!state.q7.expr) state.q7.expr = '';

            let pattern = [];
            if (state.q7.expr) {
                try {
                    const match = state.q7.expr.match(/range\(([^)]+)\)/);
                    if (match) {
                        const expr = match[1];
                        for (let i = 0; i < 5; i++) {
                            const end = Function('i', 'return ' + expr)(i);
                            if (!isNaN(end) && end > 0) {
                                for (let j = 0; j < parseInt(end); j++) pattern.push([i, j]);
                            }
                        }
                    }
                } catch (e) {}
            }

            const target = [[0,0],[1,0],[1,1],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2],[3,3],[4,0],[4,1],[4,2],[4,3],[4,4]];
            const isCorrect = state.q7.expr === 'range(i+1)';
            const matchCount = pattern.filter(p => target.some(t => t[0] === p[0] && t[1] === p[1])).length;
            const accuracy = matchCount + ' / 15 match';

            let html = `<div class="question-header"><div class="question-number">Intermediate • Programming</div>
                <div class="question-title">Q5: Expression Tree</div></div>
                <div class="question-description">Enter the loop boundary expression to create the triangle pattern.</div>
                <div class="code-block"><code><span class="keyword">for</span> i <span class="keyword">in</span> <span class="keyword">range</span>(<span class="number">5</span>):
    <span class="keyword">for</span> j <span class="keyword">in</span> <span style="color: #ff9500; font-weight: 600;">${state.q7.expr || 'range(?)'}</span>:
        <span class="keyword">draw</span>(i, j)</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div>
                            <strong>Enter boundary:</strong>
                            <div style="margin: 15px 0;">
                                <input type="text" value="${state.q7.expr}" onchange="state.q7.expr = this.value; render();" placeholder="e.g. range(i+1), range(5), range(2*i)" style="width: 100%; padding: 10px; border: 2px solid #ddd; border-radius: 6px; font-family: monospace; font-size: 13px;">
                            </div>
                        </div>
                        <div>
                            <strong>Accuracy: ${accuracy}</strong>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;">
                                <div><strong style="font-size: 12px;">Now:</strong><div style="display: grid; grid-template-columns: repeat(5, 35px); gap: 5px;">
                                    ${Array(25).fill(0).map((_, idx) => {
                                        const i = Math.floor(idx/5), j = idx % 5;
                                        const inPattern = pattern.some(p => p[0] === i && p[1] === j);
                                        const inTarget = target.some(p => p[0] === i && p[1] === j);
                                        const correct = inPattern && inTarget;
                                        const wrong = inPattern && !inTarget;
                                        let bg = '#f0f0f0';
                                        if (correct) bg = '#34C759';
                                        if (wrong) bg = '#ff6464';
                                        return `<div style="width: 35px; height: 35px; background: ${bg}; border-radius: 4px;"></div>`;
                                    }).join('')}
                                </div></div>
                                <div><strong style="font-size: 12px;">Goal:</strong><div style="display: grid; grid-template-columns: repeat(5, 35px); gap: 5px;">
                                    ${Array(25).fill(0).map((_, idx) => `<div style="width: 35px; height: 35px; background: ${target.some(p => p[0] === Math.floor(idx/5) && p[1] === idx%5) ? '#34C759' : '#f0f0f0'}; border-radius: 4px;"></div>`).join('')}
                                </div></div>
                            </div>
                        </div>
                    </div>`;

            if (isCorrect) {
                html += `<div class="completion show">✓ Pattern matches target!</div>`;
                markCompleted(7);
            }

            html += `<button onclick="resetQuestion(7)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        // ====== Q8: Line Through Two Points ======
        function renderQ8() {
            if (state.q8.a === undefined) state.q8.a = 1;
            if (state.q8.b === undefined) state.q8.b = 0;
            const a = state.q8.a, b = state.q8.b;
            const tol = 0.15;
            const p1 = [0, -1], p2 = [2, 3];
            const pass1 = Math.abs(a * p1[0] + b - p1[1]) < tol;
            const pass2 = Math.abs(a * p2[0] + b - p2[1]) < tol;

            let html = `<div class="question-header"><div class="question-number">Introductory • Mathematics</div>
                <div class="question-title">Q2: Line Through Points</div></div>
                <div class="question-description">Adjust slope (a) and intercept (b) so the line passes through both target points.</div>
                <div class="code-block"><code>y = a·x + b
Points: (0, -1) and (2, 3)</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div>
                            <strong>Slope (a):</strong>
                            <div style="display: flex; gap: 10px; margin: 12px 0; align-items: center;">
                                <button onclick="state.q8.a = Math.max(-5, state.q8.a - 0.5); render();" style="padding: 8px 12px; background: #999; color: white; border: none; border-radius: 4px; cursor: pointer;">−</button>
                                <span style="font-weight: 600; font-size: 18px; min-width: 40px; text-align: center;">${a.toFixed(1)}</span>
                                <button onclick="state.q8.a = Math.min(5, state.q8.a + 0.5); render();" style="padding: 8px 12px; background: #3844FF; color: white; border: none; border-radius: 4px; cursor: pointer;">+</button>
                            </div>
                        </div>
                        <div>
                            <strong>Intercept (b):</strong>
                            <div style="display: flex; gap: 10px; margin: 12px 0; align-items: center;">
                                <button onclick="state.q8.b = Math.max(-5, state.q8.b - 0.5); render();" style="padding: 8px 12px; background: #999; color: white; border: none; border-radius: 4px; cursor: pointer;">−</button>
                                <span style="font-weight: 600; font-size: 18px; min-width: 40px; text-align: center;">${b.toFixed(1)}</span>
                                <button onclick="state.q8.b = Math.min(5, state.q8.b + 0.5); render();" style="padding: 8px 12px; background: #3844FF; color: white; border: none; border-radius: 4px; cursor: pointer;">+</button>
                            </div>
                        </div>
                    </div>
                    <canvas id="canvas8" width="500" height="400" style="border: 1px solid #ddd; border-radius: 8px; background: white; margin-top: 20px; display: block;"></canvas>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px;">
                        <div style="padding: 12px; background: ${pass1 ? '#d4edda' : '#f8d7da'}; border-radius: 6px; color: ${pass1 ? '#155724' : '#721c24'}; font-weight: 600;">
                            Point 1: (0, -1) ${pass1 ? '✓' : '✗'}
                        </div>
                        <div style="padding: 12px; background: ${pass2 ? '#d4edda' : '#f8d7da'}; border-radius: 6px; color: ${pass2 ? '#155724' : '#721c24'}; font-weight: 600;">
                            Point 2: (2, 3) ${pass2 ? '✓' : '✗'}
                        </div>
                    </div>`;
            if (pass1 && pass2) {
                html += `<div class="completion show">✓ Line passes through both points!</div>`;
                markCompleted(8);
            }
            html += `<button onclick="resetQuestion(8)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            setTimeout(() => drawLine8(), 0);
            return html;
        }

        function drawLine8() {
            const canvas = document.getElementById('canvas8');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = 500, h = 400;
            const cx = w / 2, cy = h / 2;
            const scale = 50;

            ctx.clearRect(0, 0, w, h);
            ctx.strokeStyle = '#eee';
            ctx.lineWidth = 1;
            for (let i = -5; i <= 5; i++) {
                ctx.beginPath(); ctx.moveTo(cx + i * scale, 0); ctx.lineTo(cx + i * scale, h); ctx.stroke();
                ctx.beginPath(); ctx.moveTo(0, cy - i * scale); ctx.lineTo(w, cy - i * scale); ctx.stroke();
            }
            ctx.strokeStyle = '#333'; ctx.lineWidth = 2;
            ctx.beginPath(); ctx.moveTo(cx, 0); ctx.lineTo(cx, h); ctx.stroke();
            ctx.beginPath(); ctx.moveTo(0, cy); ctx.lineTo(w, cy); ctx.stroke();

            ctx.strokeStyle = '#3844FF'; ctx.lineWidth = 3;
            ctx.beginPath();
            for (let x = -5; x <= 5; x += 0.1) {
                const y = state.q8.a * x + state.q8.b;
                const px = cx + x * scale;
                const py = cy - y * scale;
                if (Math.abs(x + 5) < 0.01) ctx.moveTo(px, py);
                else ctx.lineTo(px, py);
            }
            ctx.stroke();

            [[0, -1], [2, 3]].forEach((p, idx) => {
                const x = cx + p[0] * scale;
                const y = cy - p[1] * scale;
                ctx.fillStyle = idx === 0 ? '#ff6464' : '#34C759';
                ctx.beginPath(); ctx.arc(x, y, 12, 0, 2 * Math.PI); ctx.fill();
            });
        }

        // ====== Q9: Bin Numbers ======
        function renderQ9() {
            if (!state.q9.placed) state.q9.placed = {};
            const numbers = [1, 7, 12, 15, 18, 23, 30, 49, 51, 64];
            const bins = {
                prime: [7, 23],
                div3: [12, 15, 18, 30, 51],
                neither: [1, 49, 64]
            };

            let placed = 0, correct = 0;
            numbers.forEach(n => {
                if (state.q9.placed[n]) {
                    placed++;
                    Object.keys(bins).forEach(bName => {
                        if (bins[bName].includes(n) && state.q9.placed[n] === bName) correct++;
                    });
                }
            });

            let html = `<div class="question-header"><div class="question-number">Introductory • Mathematics</div>
                <div class="question-title">Q1: Classify Numbers</div></div>
                <div class="question-description">Drag each number to the correct bin (or click to place/remove).</div>
                <div class="code-block"><code>Bins:
• Prime: only divisible by 1 and itself
• Divisible by 3: n % 3 == 0
• Neither: everything else</code></div>
                <div class="interactive-area">
                    <div style="margin-bottom: 30px;">
                        <strong style="display: block; margin-bottom: 12px;">Numbers to Classify:</strong>
                        <div style="display: flex; flex-wrap: wrap; gap: 8px; padding: 15px; background: #f9f9fb; border-radius: 8px; min-height: 60px;">
                            ${numbers.map(n =>
                                `<button onclick="toggleQ9Num(${n})" style="padding: 10px 16px; background: ${state.q9.placed[n] ? '#ddd' : (state.q9.selected === n ? '#3844FF' : '#fff')}; color: ${state.q9.placed[n] || state.q9.selected === n ? 'white' : '#1d1d1f'}; border: 2px solid ${state.q9.placed[n] ? '#999' : (state.q9.selected === n ? '#3844FF' : '#ddd')}; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 14px; opacity: ${state.q9.placed[n] ? '0.6' : '1'}; text-decoration: ${state.q9.placed[n] ? 'line-through' : 'none'};">${n}</button>`
                            ).join('')}
                        </div>
                        ${state.q9.selected ? `<div style="margin-top: 15px; padding: 12px; background: #e7f3ff; border-radius: 6px; font-weight: 600;">
                            Selected: ${state.q9.selected} — Click a bin to place, or click number again to cancel
                        </div>` : ''}
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">
                        ${['prime', 'div3', 'neither'].map(binName => {
                            const binLabel = binName === 'prime' ? 'Prime' : binName === 'div3' ? 'Div by 3' : 'Neither';
                            return `<div style="padding: 15px; background: #f9f9fb; border: 3px dashed ${state.q9.selected ? '#3844FF' : '#ddd'}; border-radius: 8px; min-height: 150px; cursor: ${state.q9.selected ? 'pointer' : 'default'};" ${state.q9.selected ? `onclick="classifyNum('${binName}')"` : ''}>
                                <strong style="display: block; margin-bottom: 12px;">${binLabel}</strong>
                                <div style="min-height: 100px;">
                                    ${numbers.filter(n => state.q9.placed[n] === binName).map(n => `<div style="background: #3844FF; color: white; padding: 8px; border-radius: 4px; margin: 4px 0; font-weight: 600; cursor: pointer;" onclick="removeQ9Num(${n})">${n} ✕</div>`).join('')}
                                </div>
                            </div>`;
                        }).join('')}
                    </div>
                    <div style="margin-top: 20px; text-align: center; font-weight: 600; padding: 12px; background: #f0f7ff; border-radius: 6px;">
                        Classified: ${placed} / 10 | Correct: ${correct} / 10
                    </div>`;

            if (correct === 10) {
                html += `<div class="completion show">✓ All numbers classified correctly!</div>`;
                markCompleted(9);
            }

            html += `<button onclick="resetQuestion(9)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        function toggleQ9Num(n) {
            if (state.q9.placed[n]) {
                delete state.q9.placed[n];
            } else {
                state.q9.selected = n;
            }
            render();
        }

        function removeQ9Num(n) {
            delete state.q9.placed[n];
            render();
        }

        function classifyNum(binName) {
            if (!state.q9.selected) return;
            state.q9.placed[state.q9.selected] = binName;
            state.q9.selected = null;
            render();
        }

        // ====== Q10: Transform List ======
        function renderQ10() {
            if (!state.q10.chain) state.q10.chain = [];
            const start = [1, 2, 3, 4, 5];
            const target = [8, 6, 4];
            const cards = ['×2', '+1', 'remove odd', 'reverse', 'pop', 'keep first 3'];

            let current = [...start];
            state.q10.chain.forEach(op => {
                if (op === '×2') current = current.map(x => x * 2);
                else if (op === '+1') current = current.map(x => x + 1);
                else if (op === 'remove odd') current = current.filter(x => x % 2 === 0);
                else if (op === 'reverse') current = current.reverse();
                else if (op === 'pop') current.pop();
                else if (op === 'keep first 3') current = current.slice(0, 3);
            });

            const isCorrect = JSON.stringify(current) === JSON.stringify(target);

            let html = `<div class="question-header"><div class="question-number">Intermediate • Programming</div>
                <div class="question-title">Q12: String Transform</div></div>
                <div class="question-description">Build a chain of operations to transform the start list into the target.</div>
                <div class="code-block"><code>Start:  ${JSON.stringify(start)}
Target: ${JSON.stringify(target)}
Chain operations to reach target!</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div>
                            <strong>Available Operations:</strong>
                            <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 10px;">
                                ${cards.map(card => `<button class="gate-button" onclick="addQ10Op('${card}')" style="padding: 10px; font-size: 12px;">${card}</button>`).join('')}
                            </div>
                        </div>
                        <div>
                            <strong>Chain:</strong>
                            <div style="background: white; padding: 12px; border: 1px solid #ddd; border-radius: 6px; min-height: 150px; font-family: monospace; font-size: 12px;">
                                ${state.q10.chain.length === 0 ? '[empty]' : state.q10.chain.map((op, i) => `<div style="padding: 6px; background: #e7f3ff; border-radius: 4px; margin: 4px 0;">
                                    ${i + 1}. ${op} <button onclick="removeQ10Op(${i})" style="float: right; background: #ff4444; color: white; border: none; padding: 2px 6px; border-radius: 3px; cursor: pointer; font-size: 10px;">×</button>
                                </div>`).join('')}
                            </div>
                            <div style="margin-top: 10px; padding: 10px; background: #f0f7ff; border-radius: 6px; font-family: monospace;">
                                Result: ${JSON.stringify(current)}
                            </div>
                        </div>
                    </div>`;

            if (isCorrect) {
                html += `<div class="completion show">✓ List transformed correctly!</div>`;
                markCompleted(10);
            }

            html += `<button onclick="resetQuestion(10)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        function addQ10Op(op) {
            if (!state.q10.chain) state.q10.chain = [];
            state.q10.chain.push(op);
            render();
        }

        function removeQ10Op(idx) {
            state.q10.chain.splice(idx, 1);
            render();
        }

        // ====== Q11: Extract Fragment ======
        function renderQ11() {
            if (state.q11.start === undefined) state.q11.start = null;
            if (state.q11.stop === undefined) state.q11.stop = null;
            if (state.q11.step === undefined) state.q11.step = null;

            const arr = [5, 10, 15, 20, 25, 30, 35];
            const target = [30, 20, 10];

            let result = [];
            if (state.q11.start !== null && state.q11.stop !== null && state.q11.step !== null) {
                const s = state.q11.start < 0 ? 7 + state.q11.start : state.q11.start;
                const e = state.q11.stop < 0 ? 7 + state.q11.stop : state.q11.stop;
                if (state.q11.step > 0) {
                    for (let i = s; i < e; i += state.q11.step) result.push(arr[i]);
                } else if (state.q11.step < 0) {
                    for (let i = s; i > e; i += state.q11.step) result.push(arr[i]);
                }
            }

            const isCorrect = JSON.stringify(result) === JSON.stringify(target);

            let html = `<div class="question-header"><div class="question-number">Intermediate • Programming</div>
                <div class="question-title">Q11: Extract Fragment</div></div>
                <div class="question-description">Use slice notation [start:stop:step] to extract the target sequence.</div>
                <div class="code-block"><code>arr = [5, 10, 15, 20, 25, 30, 35]
Target: [30, 20, 10]
arr[⟦start⟧:⟦stop⟧:⟦step⟧]</code></div>
                <div class="interactive-area">
                    <div style="margin: 20px 0; font-family: monospace; font-weight: 600;">
                        arr[<input type="number" style="width: 40px; padding: 4px; border: 1px solid #ddd; border-radius: 4px;" value="${state.q11.start ?? ''}" onchange="state.q11.start = this.value === '' ? null : parseInt(this.value); render();">
                        :<input type="number" style="width: 40px; padding: 4px; border: 1px solid #ddd; border-radius: 4px;" value="${state.q11.stop ?? ''}" onchange="state.q11.stop = this.value === '' ? null : parseInt(this.value); render();">
                        :<input type="number" style="width: 40px; padding: 4px; border: 1px solid #ddd; border-radius: 4px;" value="${state.q11.step ?? ''}" onchange="state.q11.step = this.value === '' ? null : parseInt(this.value); render();">]
                    </div>
                    <div style="padding: 12px; background: #f0f7ff; border-radius: 6px; margin: 15px 0; font-family: monospace;">
                        Result: ${JSON.stringify(result)}
                    </div>
                    <div style="padding: 12px; background: #e7f3ff; border-radius: 6px; font-family: monospace;">
                        Target: ${JSON.stringify(target)}
                    </div>`;

            if (isCorrect) {
                html += `<div class="completion show">✓ Slice extracts correct fragment!</div>`;
                markCompleted(11);
            }

            html += `<button onclick="resetQuestion(11)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        // ====== Q12: Build Dictionary ======
        function renderQ12() {
            if (!state.q12.pairs) state.q12.pairs = [];
            const keys = ['a', 'b', 'c'];
            const d = {};
            state.q12.pairs.forEach(p => d[p[0]] = p[1]);

            const checks = [
                {expr: `d["a"] == 2`, value: d['a'] === 2},
                {expr: `d.get("b", 0) == 0`, value: d['b'] === undefined},
                {expr: `d["c"] == d["a"] + 3`, value: d['c'] === d['a'] + 3},
                {expr: `len(d) == 2`, value: Object.keys(d).length === 2}
            ];

            const allPass = checks.every(c => c.value);

            let html = `<div class="question-header"><div class="question-number">Advanced • Programming</div>
                <div class="question-title">Q7: Sequence Pairs</div></div>
                <div class="question-description">Build a dictionary that satisfies all four requirements simultaneously.</div>
                <div class="code-block"><code>${checks.map(c => c.value ? `✓ ${c.expr}` : `✗ ${c.expr}`).join('\n')}</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div>
                            <strong>Add Pairs:</strong>
                            <div style="margin-top: 10px;">
                                <select id="keySelect" style="padding: 6px; border: 1px solid #ddd; border-radius: 4px;">
                                    ${keys.map(k => `<option value="${k}">${k}</option>`).join('')}
                                </select>
                                <input type="number" id="valInput" style="padding: 6px; border: 1px solid #ddd; border-radius: 4px; margin: 0 4px; width: 60px;" placeholder="value">
                                <button onclick="addQ12Pair()" class="gate-button" style="padding: 6px 12px; font-size: 12px;">Add</button>
                            </div>
                            <div style="margin-top: 15px;">
                                <strong style="font-size: 12px;">Current Dictionary:</strong>
                                <div style="font-family: monospace; background: white; padding: 10px; border: 1px solid #ddd; border-radius: 6px; margin-top: 8px;">
                                    ${Object.entries(d).length === 0 ? '{}' : '{' + Object.entries(d).map((e, i) => `<div style="display: flex; justify-content: space-between; align-items: center;"><span>"${e[0]}": ${e[1]}</span><button onclick="removeQ12Pair('${e[0]}')" style="background: #ff4444; color: white; border: none; padding: 2px 6px; border-radius: 3px; cursor: pointer; font-size: 10px; margin-left: 10px;">Remove</button></div>`).join('') + '}'}
                                </div>
                            </div>
                        </div>
                        <div>
                            <strong>Requirements:</strong>
                            ${checks.map(c => `<div style="padding: 8px; background: ${c.value ? '#d4edda' : '#f8d7da'}; border-radius: 6px; margin: 6px 0; color: ${c.value ? '#155724' : '#721c24'}; font-weight: 600; font-family: monospace; font-size: 11px;">
                                ${c.value ? '✓' : '✗'} ${c.expr}
                            </div>`).join('')}
                        </div>
                    </div>`;

            if (allPass) {
                html += `<div class="completion show">✓ Dictionary satisfies all requirements!</div>`;
                markCompleted(12);
            }

            html += `<button onclick="resetQuestion(12)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        function addQ12Pair() {
            const key = document.getElementById('keySelect').value;
            const val = parseInt(document.getElementById('valInput').value);
            if (isNaN(val)) return;
            if (!state.q12.pairs) state.q12.pairs = [];
            const existing = state.q12.pairs.findIndex(p => p[0] === key);
            if (existing >= 0) state.q12.pairs[existing] = [key, val];
            else state.q12.pairs.push([key, val]);
            document.getElementById('valInput').value = '';
            render();
        }

        function removeQ12Pair(key) {
            if (!state.q12.pairs) return;
            state.q12.pairs = state.q12.pairs.filter(p => p[0] !== key);
            render();
        }

        // ====== Q13: Sequence Law ======
        function renderQ13() {
            if (!state.q13.c2) state.q13.c2 = 0;
            if (!state.q13.c1) state.q13.c1 = 0;
            if (!state.q13.c0) state.q13.c0 = 0;

            const target = [2, 6, 12, 20, 30, 42, 56];
            const c2 = state.q13.c2, c1 = state.q13.c1, c0 = state.q13.c0;
            const generated = Array.from({length: 7}, (_, i) => c2 * (i+1) * (i+1) + c1 * (i+1) + c0);
            const allPass = generated.every((v, i) => v === target[i]);

            let html = `<div class="question-header"><div class="question-number">Advanced • Mathematics</div>
                <div class="question-title">Q8: Polynomial Visualization</div></div>
                <div class="question-description">Adjust coefficients to generate the exact sequence, including hidden test cases.</div>
                <div class="code-block"><code>a(n) = c2·n² + c1·n + c0
Visible: n=1..5: [2, 6, 12, 20, 30]
(More hidden tests will check your solution)</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0;">
                        <div><label>c2 (n²)</label><input type="number" value="${c2}" onchange="state.q13.c2 = parseInt(this.value); render();" style="width: 100%; padding: 6px; border: 1px solid #ddd; border-radius: 4px;"></div>
                        <div><label>c1 (n)</label><input type="number" value="${c1}" onchange="state.q13.c1 = parseInt(this.value); render();" style="width: 100%; padding: 6px; border: 1px solid #ddd; border-radius: 4px;"></div>
                        <div><label>c0 (const)</label><input type="number" value="${c0}" onchange="state.q13.c0 = parseInt(this.value); render();" style="width: 100%; padding: 6px; border: 1px solid #ddd; border-radius: 4px;"></div>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 8px; margin: 15px 0;">
                        ${target.map((expected, i) => {
                            const actual = generated[i];
                            const match = actual === expected;
                            return `<div style="padding: 12px; background: ${match ? '#d4edda' : '#f8d7da'}; border-radius: 6px; text-align: center; color: ${match ? '#155724' : '#721c24'}; font-weight: 600;">
                                n=${i+1}<br>${actual} ${match ? '✓' : '✗'}
                            </div>`;
                        }).join('')}
                    </div>`;

            if (allPass) {
                html += `<div class="completion show">✓ Sequence law found!</div>`;
                markCompleted(13);
            }

            html += `<button onclick="resetQuestion(13)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        // ====== Q14: String Operations ======
        function renderQ14() {
            if (!state.q14.chain) state.q14.chain = [];
            const start = "hello world";
            const target = "DLROWOLLEH";
            const ops = [
                {id: 'upper', label: 'upper()', fn: s => s.toUpperCase()},
                {id: 'lower', label: 'lower()', fn: s => s.toLowerCase()},
                {id: 'reverse', label: 'reverse()', fn: s => s.split('').reverse().join('')},
                {id: 'remove_space', label: 'remove spaces', fn: s => s.replace(/ /g, '')},
                {id: 'remove_vowels', label: 'remove vowels', fn: s => s.replace(/[aeiouAEIOU]/g, '')}
            ];

            let current = start;
            state.q14.chain.forEach(opId => {
                const op = ops.find(o => o.id === opId);
                if (op) current = op.fn(current);
            });

            const isCorrect = current === target;

            let html = `<div class="question-header"><div class="question-number">Intermediate • Programming</div>
                <div class="question-title">Q15: String Transform v2</div></div>
                <div class="question-description">Chain operations in the correct order to match the target.</div>
                <div class="code-block"><code>Start:  "${start}"
Target: "${target}"

Transform: Remove spaces →
Reverse → Uppercase</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div>
                            <strong>Available Operations:</strong>
                            <div style="display: grid; grid-template-columns: 1fr; gap: 6px; margin-top: 10px;">
                                ${ops.map(op => `<button class="gate-button" onclick="addQ14Op('${op.id}')" style="padding: 8px; font-size: 12px;">${op.label}</button>`).join('')}
                            </div>
                        </div>
                        <div>
                            <strong>Transformation Chain:</strong>
                            <div style="background: white; padding: 10px; border: 1px solid #ddd; border-radius: 6px; font-family: monospace; font-size: 11px; min-height: 60px; margin-bottom: 10px;">
                                <div style="color: #666; margin-bottom: 8px;">0. "${start}"</div>
                                ${state.q14.chain.length === 0 ? '<div style="color: #999;">[add operations →]</div>' : state.q14.chain.map((opId, i) => {
                                    const op = ops.find(o => o.id === opId);
                                    let stepResult = start;
                                    for (let j = 0; j <= i; j++) {
                                        const stepOp = ops.find(o => o.id === state.q14.chain[j]);
                                        if (stepOp) stepResult = stepOp.fn(stepResult);
                                    }
                                    return `<div style="display: flex; justify-content: space-between; margin: 4px 0; padding: 4px 0; border-bottom: 1px solid #eee;">
                                        <span>${i+1}. ${op ? op.label : opId}</span>
                                        <button onclick="removeQ14Op(${i})" style="font-size: 10px; padding: 0 4px; background: #ff4444; color: white; border: none; border-radius: 2px; cursor: pointer;">×</button>
                                    </div>
                                    <div style="color: #3844FF; font-weight: 600; margin: 2px 0 8px 0;">${stepResult}</div>`;
                                }).join('')}
                            </div>
                            <div style="padding: 10px; background: ${isCorrect ? '#d4edda' : '#e7f3ff'}; border-radius: 6px; border: 1px solid ${isCorrect ? '#28a745' : '#3844FF'};">
                                <div style="font-size: 10px; color: #666; margin-bottom: 4px;">Result:</div>
                                <div style="font-family: monospace; font-weight: 600; font-size: 12px; color: ${isCorrect ? '#155724' : '#1d1d1f'};}">"${current}"</div>
                            </div>
                        </div>
                    </div>`;

            if (isCorrect) {
                html += `<div class="completion show">✓ String transformation successful!</div>`;
                markCompleted(14);
            }

            html += `<button onclick="resetQuestion(14)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        function addQ14Op(opId) {
            if (!state.q14.chain) state.q14.chain = [];
            state.q14.chain.push(opId);
            render();
        }

        function removeQ14Op(idx) {
            state.q14.chain.splice(idx, 1);
            render();
        }

        // ====== Q15: Bubble Sort ======
        function renderQ15() {
            if (!state.q15.arr) {
                state.q15.arr = [8, 2, 6, 1, 7, 3, 5, 4];
                state.q15.swaps = 0;
            }
            if (state.q15.minSwaps === undefined) {
                state.q15.minSwaps = countInversions([8, 2, 6, 1, 7, 3, 5, 4]);
            }

            const arr = state.q15.arr;
            const sorted = [...arr].sort((a, b) => a - b);
            const isSorted = JSON.stringify(arr) === JSON.stringify(sorted);
            const minSwaps = state.q15.minSwaps;

            let html = `<div class="question-header"><div class="question-number">Advanced • Programming</div>
                <div class="question-title">Q6: Sort with Minimum Swaps</div></div>
                <div class="question-description">Sort the array using ONLY adjacent swaps, in minimum moves.</div>
                <div class="code-block"><code>Array: [${arr.join(', ')}]
Only swap neighbors!
Target: minimum ${minSwaps} swaps</code></div>
                <div class="interactive-area">
                    <div style="display: flex; gap: 8px; align-items: flex-end; margin: 20px 0; height: 200px;">
                        ${arr.map((val, i) => `<div style="width: 40px; height: ${val * 30}px; background: #3844FF; border-radius: 4px; position: relative;">
                            ${i < arr.length - 1 ? `<button onclick="swapQ15(${i})" style="position: absolute; bottom: -25px; left: 50%; transform: translateX(-50%); padding: 4px 8px; background: #999; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 11px;">⇄</button>` : ''}
                        </div>`).join('')}
                    </div>
                    <div style="text-align: center; font-weight: 600; padding: 12px; background: #f0f7ff; border-radius: 6px;">
                        Swaps: ${state.q15.swaps} ${state.q15.swaps === minSwaps && isSorted ? '✓' : (isSorted ? `(need minimum ${minSwaps})` : '')}
                    </div>`;

            if (isSorted && state.q15.swaps === minSwaps) {
                html += `<div class="completion show">✓ Sorted in minimum swaps!</div>`;
                markCompleted(15);
            } else if (isSorted && state.q15.swaps > minSwaps) {
                html += `<div style="padding: 12px; background: #fff3cd; border: 1px solid #ffc107; border-radius: 6px; color: #856404; margin-top: 15px; font-weight: 600;">⚠ Sorted, but used ${state.q15.swaps} swaps instead of ${minSwaps}. Try again!</div>`;
            }
            html += `<button onclick="resetQuestion(15)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button>
                </div>`;
            return html;
        }

        function swapQ15(i) {
            [state.q15.arr[i], state.q15.arr[i+1]] = [state.q15.arr[i+1], state.q15.arr[i]];
            state.q15.swaps++;
            render();
        }

        // ====== Q16: Shape with Constraints ======
        function renderQ16() {
            if (!state.q16.w) state.q16.w = 3;
            if (!state.q16.h) state.q16.h = 8;
            const w = state.q16.w, h = state.q16.h;
            const area = w * h, perim = 2 * (w + h);
            const areaMatch = area === 24, perimMatch = perim === 20;

            let html = `<div class="question-header"><div class="question-number">Introductory • Mathematics</div>
                <div class="question-title">Q3: Rectangle Constraints</div></div>
                <div class="question-description">Adjust width and height so BOTH area = 24 AND perimeter = 20.</div>
                <div class="code-block"><code>area = w × h = 24
perim = 2(w + h) = 20</code></div>
                <div class="interactive-area">
                    <div style="text-align: center; margin: 30px 0;">
                        <div style="display: inline-block; width: ${w * 20}px; height: ${h * 20}px; background: #3844FF; border: 2px solid #333; border-radius: 4px;"></div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
                        <div>
                            <label style="font-weight: 600;">Width (w)</label>
                            <input type="number" value="${w}" onchange="state.q16.w = parseInt(this.value); render();" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; margin-top: 6px;">
                        </div>
                        <div>
                            <label style="font-weight: 600;">Height (h)</label>
                            <input type="number" value="${h}" onchange="state.q16.h = parseInt(this.value); render();" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; margin-top: 6px;">
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                        <div style="padding: 12px; background: ${areaMatch ? '#d4edda' : '#f8d7da'}; border-radius: 6px; color: ${areaMatch ? '#155724' : '#721c24'}; font-weight: 600;">
                            Area = ${area} ${areaMatch ? '✓' : '✗'}
                        </div>
                        <div style="padding: 12px; background: ${perimMatch ? '#d4edda' : '#f8d7da'}; border-radius: 6px; color: ${perimMatch ? '#155724' : '#721c24'}; font-weight: 600;">
                            Perim = ${perim} ${perimMatch ? '✓' : '✗'}
                        </div>
                    </div>`;

            if (areaMatch && perimMatch) {
                html += `<div class="completion show">✓ Both constraints satisfied!</div>`;
                markCompleted(16);
            }

            html += `<button onclick="resetQuestion(16)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        // ====== Q17: Orbit on Circle ======
        function renderQ17() {
            if (state.q17.p === undefined) state.q17 = { p: 2, q: 3, r: 4 };
            const p = state.q17.p, q = state.q17.q, r = state.q17.r;
            const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);
            const lcm2 = (a, b) => a * b / gcd(a, b);
            const lcm = lcm2(lcm2(p, q), r);
            const pairwiseCoprime = gcd(p, q) === 1 && gcd(q, r) === 1 && gcd(p, r) === 1;
            const TARGET = 105;
            const isCorrect = (lcm === TARGET && pairwiseCoprime);

            const planets = [
                { key: 'p', val: p, name: 'A', color: '#3844FF' },
                { key: 'q', val: q, name: 'B', color: '#FF8C00' },
                { key: 'r', val: r, name: 'C', color: '#34C759' }
            ];

            const ctrl = (pl) => `
                <div style="text-align:center;">
                    <label style="font-weight:600;display:block;margin-bottom:6px;color:${pl.color};font-size:13px;">Planet ${pl.name} — period (2–9)</label>
                    <div style="display:flex;justify-content:center;gap:8px;align-items:center;">
                        <button onclick="state.q17.${pl.key}=Math.max(2,state.q17.${pl.key}-1);render();" style="padding:8px 12px;background:#999;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:600;">−</button>
                        <span style="font-size:24px;font-weight:700;min-width:40px;text-align:center;color:${pl.color};">${pl.val}</span>
                        <button onclick="state.q17.${pl.key}=Math.min(9,state.q17.${pl.key}+1);render();" style="padding:8px 12px;background:${pl.color};color:white;border:none;border-radius:4px;cursor:pointer;font-weight:600;">+</button>
                    </div>
                    <div style="font-size:11px;color:#777;margin-top:6px;">returns at: ${[1, 2, 3, 4].map(k => pl.val * k).join(', ')}, …</div>
                </div>`;

            const pairRows = [['A', 'B', lcm2(p, q)], ['A', 'C', lcm2(p, r)], ['B', 'C', lcm2(q, r)]]
                .map(([x, y, L]) => `<div style="padding:6px 10px;background:white;border:1px solid #eee;border-radius:6px;font-size:12px;">${x} & ${y} meet at <b>${L}</b></div>`)
                .join('');

            let guidance = '';
            if (!isCorrect) {
                if (lcm === TARGET && !pairwiseCoprime) {
                    guidance = `<div style="text-align:center;padding:10px;background:#fff3cd;border-radius:6px;color:#856404;font-weight:600;margin-top:12px;">All three reunite at tick 105, but two of them share a common factor. Make every pair coprime.</div>`;
                } else {
                    guidance = `<div style="text-align:center;padding:10px;background:#f1f1f4;border-radius:6px;color:#555;font-weight:600;margin-top:12px;">All three first reunite at tick ${lcm}. Target: exactly ${TARGET}.</div>`;
                }
            }

            let html = `<div class="question-header"><div class="question-number">Advanced • Mathematics</div>
                <div class="question-title">Q17: Three Planets</div></div>
                <div class="question-description">Three planets start together at 0. Each returns to the start after its own period. Set the three periods so that ALL THREE first return to the start <i>together</i> at exactly tick <b>105</b> — and no two of them share a common factor greater than 1.</div>
                <div class="code-block"><code>Each planet is back at start on multiples of its period.
First time all three meet = least common multiple(p, q, r)
Goal: LCM(p, q, r) = 105   AND   every pair is coprime</code></div>
                <div class="interactive-area">
                    <div style="display:flex;justify-content:center;gap:30px;flex-wrap:wrap;margin:10px 0 20px;">
                        ${planets.map(ctrl).join('')}
                    </div>
                    <div style="text-align:center;padding:16px;border-radius:8px;background:${isCorrect ? '#d4edda' : '#f6f6f8'};margin:10px 0;">
                        <div style="font-size:13px;color:#555;margin-bottom:4px;">First time all three meet at the start:</div>
                        <div style="font-size:30px;font-weight:800;color:${isCorrect ? '#155724' : (lcm === TARGET ? '#856404' : '#1d1d1f')};">tick ${lcm}${isCorrect ? ' ✓' : ''}</div>
                    </div>
                    <div style="display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin:8px 0;">${pairRows}</div>
                    ${guidance}`;

            if (isCorrect) {
                html += `<div class="completion show">✓ Periods 3, 5, 7: all three first reunite at tick 105, every pair coprime.</div>`;
                markCompleted(17);
            }

            html += `<button onclick="resetQuestion(17)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        // ====== Q18: Bits ======
        function renderQ18() {
            if (!state.q18.b) state.q18.b = [0, 0, 0, 0, 0];
            const a = [1, 0, 1, 1, 0];
            const b = state.q18.b;
            const andRes = a.map((v, i) => v & b[i]);
            const orRes = a.map((v, i) => v | b[i]);
            const andTarget = [0, 0, 1, 1, 0];
            const orTarget = [1, 1, 1, 1, 0];
            const andPass = JSON.stringify(andRes) === JSON.stringify(andTarget);
            const orPass = JSON.stringify(orRes) === JSON.stringify(orTarget);

            let html = `<div class="question-header"><div class="question-number">Advanced • Programming, Mathematics</div>
                <div class="question-title">Q18: Binary Operations</div></div>
                <div class="question-description">Set bits of b so both AND and OR conditions are satisfied independently.</div>
                <div class="code-block"><code>a = 10110
a & b = 01110
a | b = 11110</code></div>
                <div class="interactive-area">
                    <div style="display: grid; grid-template-columns: repeat(5, 60px); gap: 8px; margin: 20px 0;">
                        <strong style="grid-column: 1/-1;">Set bits of b:</strong>
                        ${b.map((bit, i) => `<button onclick="state.q18.b[${i}] = 1 - state.q18.b[${i}]; render();" style="padding: 12px; background: ${bit ? '#3844FF' : 'white'}; color: ${bit ? 'white' : '#1d1d1f'}; border: 2px solid #3844FF; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 14px;">${bit}</button>`).join('')}
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 10px; margin: 20px 0;">
                        <div style="text-align: center;">
                            <strong style="font-size: 12px;">a</strong><br>
                            <div style="font-family: monospace; font-weight: 600;">
                                ${a.join('')}
                            </div>
                        </div>
                        <div style="text-align: center;">
                            <strong style="font-size: 12px;">b</strong><br>
                            <div style="font-family: monospace; font-weight: 600;">
                                ${b.join('')}
                            </div>
                        </div>
                        <div style="text-align: center;">
                            <strong style="font-size: 12px;">a & b</strong><br>
                            <div style="font-family: monospace; font-weight: 600; color: ${andPass ? '#34C759' : '#ff4444'};">
                                ${andRes.join('')}
                            </div>
                        </div>
                        <div style="text-align: center;">
                            <strong style="font-size: 12px;">a | b</strong><br>
                            <div style="font-family: monospace; font-weight: 600; color: ${orPass ? '#34C759' : '#ff4444'};">
                                ${orRes.join('')}
                            </div>
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                        <div style="padding: 12px; background: ${andPass ? '#d4edda' : '#f8d7da'}; border-radius: 6px; color: ${andPass ? '#155724' : '#721c24'}; font-weight: 600; font-family: monospace;">
                            a & b = ${andRes.join('')} ${andPass ? '✓' : '✗'}
                        </div>
                        <div style="padding: 12px; background: ${orPass ? '#d4edda' : '#f8d7da'}; border-radius: 6px; color: ${orPass ? '#155724' : '#721c24'}; font-weight: 600; font-family: monospace;">
                            a | b = ${orRes.join('')} ${orPass ? '✓' : '✗'}
                        </div>
                    </div>`;

            if (andPass && orPass) {
                html += `<div class="completion show">✓ Both conditions satisfied!</div>`;
                markCompleted(18);
            }

            html += `<button onclick="resetQuestion(18)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        // ====== Q19: Operations inside 4 nested loops (hidden law n³ + 2n + 1) ======
        function renderQ19() {
            if (!state.q19.ops || state.q19.ops.length !== 4) state.q19 = { ops: [0, 0, 0, 0] };
            const ops = state.q19.ops;                       // depth 0..3 → ×1, ×n, ×n², ×n³
            const count = (n) => ops.reduce((s, c, d) => s + c * Math.pow(n, d), 0);
            const target = (n) => n * n * n + 2 * n + 1;     // скрытый закон
            const visible = [1, 2, 3, 4];
            const hidden = [5, 6];
            const allPass = [...visible, ...hidden].every(n => count(n) === target(n));

            const dot = (lvl) => `<span onclick="state.q19.ops[${lvl}]=Math.max(0,state.q19.ops[${lvl}]-1);render();" title="click to remove" style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;background:#3844FF;color:white;font-size:11px;cursor:pointer;margin:2px;">●</span>`;
            const addBtn = (lvl) => `<button onclick="state.q19.ops[${lvl}]++;render();" style="padding:4px 10px;background:white;border:1px dashed #3844FF;color:#3844FF;border-radius:6px;cursor:pointer;font-weight:600;font-size:12px;margin-left:6px;vertical-align:middle;">＋ op</button>`;
            const dots = (lvl) => Array.from({length: ops[lvl]}, () => dot(lvl)).join('');

            const box = (lvl, codeLabel, mult, color, bg, inner) => `
                <div style="border:2px solid ${color};border-radius:8px;padding:10px;background:${bg};">
                    <div style="font-family:monospace;font-weight:600;font-size:13px;margin-bottom:6px;">${codeLabel} <span style="color:${color};font-family:inherit;">— each op runs ${mult}</span></div>
                    <div style="margin-bottom:${inner ? '10px' : '0'};">${dots(lvl)}${addBtn(lvl)}</div>
                    ${inner || ''}
                </div>`;

            const lvl3 = box(3, 'for k in range(n):', 'n³ times', '#2a2fbf', '#e6e8ff', '');
            const lvl2 = box(2, 'for j in range(n):', 'n² times', '#3844FF', '#eef0ff', lvl3);
            const lvl1 = box(1, 'for i in range(n):', 'n times', '#6b73ff', '#f4f5ff', lvl2);
            const lvl0 = box(0, 'top level', '1 time', '#bbb', 'white', lvl1);

            const tableCells = visible.map(n => {
                const c = count(n), t = target(n), ok = c === t;
                return `<div style="padding:12px;background:${ok ? '#d4edda' : '#f8d7da'};border-radius:6px;color:${ok ? '#155724' : '#721c24'};font-weight:600;text-align:center;">
                    n=${n}<br>need ${t}<br>you ${c} ${ok ? '✓' : '✗'}
                </div>`;
            }).join('');

            let html = `<div class="question-header"><div class="question-number">Advanced • Programming, Reasoning</div>
                <div class="question-title">Q19: Build the Growth</div></div>
                <div class="question-description">Place operations inside (or outside) the nested loops so the total operation count matches the target for every n. The deeper an op sits, the more often it runs. The target is given only as numbers — work out which loops to fill. Careful: you may not need every level. Click ＋ op to add, click a dot to remove.</div>
                <div class="code-block"><code>op at top level   → runs 1 time
op inside 1 loop  → runs n times
op inside 2 loops → runs n² times
op inside 3 loops → runs n³ times
Target counts:  n=1 → 4,  n=2 → 13,  n=3 → 34,  n=4 → 73</code></div>
                <div class="interactive-area">
                    ${lvl0}
                    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:20px 0;">
                        ${tableCells}
                    </div>`;

            if (allPass) {
                html += `<div class="completion show">✓ Your structure matches the target for every n (the hidden law was n³ + 2n + 1).</div>`;
                markCompleted(19);
            }

            html += `<button onclick="resetQuestion(19)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        // ====== Q20: Divisibility-by-3 Automaton (binary) ======
        function renderQ20() {
            if (!state.q20.trans) state.q20 = { trans: { r0_0: '', r0_1: '', r1_0: '', r1_1: '', r2_0: '', r2_1: '' }, traceNum: 6 };
            if (state.q20.traceNum === undefined) state.q20.traceNum = 6;
            const T = state.q20.trans;

            // Прогон числа по текущей машине. Возвращает шаги, завершённость и вердикт.
            const runMachine = (n) => {
                const bin = n.toString(2);
                let s = 'r0';
                const steps = [];
                for (const bit of bin) {
                    const nxt = T[s + '_' + bit];
                    steps.push({ bit, from: s, to: nxt || null });
                    if (!nxt) return { complete: false, steps, accept: false, final: null };
                    s = nxt;
                }
                return { complete: true, steps, accept: s === 'r0', final: s };
            };

            const visible = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
            const hidden = [21, 33, 45, 100, 17, 19];
            const verdict = (n) => { const r = runMachine(n); return r.complete ? r.accept : null; };
            const matches = (n) => verdict(n) === (n % 3 === 0);
            const all = [...visible, ...hidden];
            const pass = all.filter(matches).length;
            const allPass = pass === all.length;

            // --- карточки состояний с выпадающими переходами ---
            const opt = (key, val, label) => `<option value="${val}" ${T[key] === val ? 'selected' : ''}>${label}</option>`;
            const sel = (key) => `<select onchange="state.q20.trans['${key}']=this.value;render();" style="padding:5px;border-radius:4px;border:1px solid #ddd;font-size:13px;">
                <option value="" ${T[key] === '' ? 'selected' : ''}>—</option>
                ${opt(key, 'r0', 'rem 0')}${opt(key, 'r1', 'rem 1')}${opt(key, 'r2', 'rem 2')}
            </select>`;
            const stateCard = (st, idx) => `<div style="padding:12px;background:#e7f3ff;border-radius:8px;border:2px solid #3844FF;">
                <strong>rem ${idx}</strong> ${idx === 0 ? '<span style="font-size:11px;color:#155724;font-weight:600;">(start &amp; accept)</span>' : ''}
                <div style="margin-top:10px;font-size:13px;display:flex;flex-direction:column;gap:8px;">
                    <div>read bit <b>0</b> → ${sel(st + '_0')}</div>
                    <div>read bit <b>1</b> → ${sel(st + '_1')}</div>
                </div>
            </div>`;

            // --- тест-сетка (клик задаёт число для трассировки) ---
            const cell = (n) => {
                const v = verdict(n), ok = matches(n);
                const bg = v === null ? '#f1f1f4' : (ok ? '#d4edda' : '#f8d7da');
                const col = v === null ? '#555' : (ok ? '#155724' : '#721c24');
                const selBorder = state.q20.traceNum === n ? '2px solid #3844FF' : '1px solid transparent';
                return `<div onclick="state.q20.traceNum=${n};render();" style="cursor:pointer;padding:8px 4px;background:${bg};color:${col};border-radius:6px;text-align:center;border:${selBorder};">
                    <div style="font-weight:700;">${n}</div>
                    <div style="font-family:monospace;font-size:11px;">${n.toString(2)}</div>
                    <div style="font-size:12px;">${v === null ? '?' : (ok ? '✓' : '✗')}</div>
                </div>`;
            };

            // --- трассировка выбранного числа ---
            const tn = state.q20.traceNum;
            const tr = runMachine(tn);
            const chip = (label) => `<span style="display:inline-block;padding:3px 9px;border-radius:12px;background:#3844FF;color:white;font-size:12px;font-weight:700;">${label}</span>`;
            let flow = chip('rem 0');
            tr.steps.forEach(s => {
                flow += ` <span style="color:#999;font-size:12px;">—${s.bit}→</span> `;
                flow += s.to ? chip('rem ' + s.to[1]) : `<span style="color:#cc0000;font-weight:700;">(not set)</span>`;
            });
            const divis = tn % 3 === 0;
            const traceVerdict = tr.complete
                ? `Ends at <b>rem ${tr.final[1]}</b> → machine says <b>${tr.accept ? 'divisible' : 'not divisible'}</b>. ${tn} is ${divis ? '' : 'not '}divisible by 3 → ${tr.accept === divis ? '<span style="color:#155724;font-weight:700;">match ✓</span>' : '<span style="color:#cc0000;font-weight:700;">mismatch ✗</span>'}`
                : `<span style="color:#cc0000;">The path reaches an unset transition (—). Fill it in to continue.</span>`;

            let html = `<div class="question-header"><div class="question-number">Olympiad • Programming, Mathematics</div>
                <div class="question-title">Q20: Divisibility Automaton</div></div>
                <div class="question-description">Build a machine that reads a number's binary digits left-to-right and decides whether it is divisible by 3. Each <b>state</b> is the current remainder mod 3. Set where every arrow goes.</div>
                <div class="code-block"><code>A binary number grows bit by bit:  value → value*2 + bit
So its remainder mod 3 grows the same way:
        new remainder = (old remainder * 2 + bit) mod 3
Start at rem 0. If you END at rem 0, the number is divisible by 3.</code></div>
                <div style="padding:12px;background:#fff8e6;border:1px solid #ffe39e;border-radius:8px;margin-bottom:16px;font-size:13px;">
                    <b>Worked example (one arrow):</b> you are in <b>rem 1</b> and read bit <b>0</b>.
                    new = (1*2 + 0) mod 3 = 2. So the arrow <b>rem 1, bit 0 → rem 2</b>. Fill the other five arrows the same way.
                </div>
                <div class="interactive-area">
                    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:18px;">
                        ${['r0', 'r1', 'r2'].map((st, i) => stateCard(st, i)).join('')}
                    </div>

                    <div style="padding:14px;background:#f6f8ff;border-radius:8px;border:1px solid #dfe4ff;margin-bottom:18px;">
                        <div style="font-weight:600;font-size:13px;margin-bottom:8px;">Trace a number (click any number below):
                            <span style="color:#3844FF;">${tn}</span> = <span style="font-family:monospace;">${tn.toString(2)}</span></div>
                        <div style="line-height:2;">${flow}</div>
                        <div style="margin-top:8px;font-size:13px;">${traceVerdict}</div>
                    </div>

                    <div style="font-weight:600;font-size:13px;margin-bottom:8px;">Test numbers (green = your machine agrees with "divisible by 3"):</div>
                    <div style="display:grid;grid-template-columns:repeat(8,1fr);gap:6px;margin-bottom:14px;">
                        ${visible.map(cell).join('')}
                    </div>
                    <div style="padding:12px;background:${allPass ? '#d4edda' : '#f0f7ff'};border-radius:6px;text-align:center;font-weight:700;color:${allPass ? '#155724' : '#1d1d1f'};">
                        Pass: ${pass} / ${all.length} <span style="font-weight:400;font-size:12px;color:#777;">(includes hidden numbers)</span>
                    </div>`;

            if (allPass) {
                html += `<div class="completion show">✓ Your automaton recognizes divisibility by 3 in binary — on every number, including the hidden ones.</div>`;
                markCompleted(20);
            }

            html += `<button onclick="resetQuestion(20)" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
            return html;
        }

        function countInversions(arr) {
            let count = 0;
            for (let i = 0; i < arr.length; i++) {
                for (let j = i + 1; j < arr.length; j++) {
                    if (arr[i] > arr[j]) count++;
                }
            }
            return count;
        }

        function markCompleted(n) {
            state.completed.add(n);
            const btns = document.querySelectorAll('.question-btn');
            btns[n - 1].classList.add('completed');
        }

        function resetQuestion(newN) {
            // Маппинг новый номер → старый номер
            const mapping = [null, 9, 8, 16, 11, 7, 15, 12, 13, 1, 2, 3, 10, 5, 6, 14, 4, 17, 18, 19, 20];
            const oldN = mapping[newN];

            switch(oldN) {
                case 1: state.q1 = { clicked: [], verified: false }; break;
                case 2: state.q2 = { boundaries: [30, 60, 90] }; break;
                case 3: state.q3 = { a: 2, b: 0, c: 0 }; break;
                case 4: state.q4 = { nodes: [], outSource: null }; break;
                case 5: state.q5 = { probes: {}, pipeline: [] }; break;
                case 6: state.q6 = { grid: [['+2', '×2', '+1', '−1'], ['×3', '+4', '×2', '+5'], ['+1', '−2', '+6', '×2'], ['×2', '+3', '−1', '+4']], current: 3, path: [[0,0]], target: 48 }; break;
                case 7: state.q7 = { expr: '' }; break;
                case 8: state.q8 = { a: 1, b: 0 }; break;
                case 9: state.q9 = { placed: {}, selected: null }; break;
                case 10: state.q10 = { chain: [] }; break;
                case 11: state.q11 = { start: null, stop: null, step: null }; break;
                case 12: state.q12 = { pairs: [] }; break;
                case 13: state.q13 = { c2: 0, c1: 0, c0: 0 }; break;
                case 14: state.q14 = { chain: [] }; break;
                case 15: state.q15 = { arr: [8, 2, 6, 1, 7, 3, 5, 4], swaps: 0, minSwaps: undefined }; break;
                case 16: state.q16 = { w: 3, h: 8 }; break;
                case 17: state.q17 = { p: 2, q: 3, r: 4 }; break;
                case 18: state.q18 = { b: [0, 0, 0, 0, 0] }; break;
                case 19: state.q19 = { ops: [0, 0, 0, 0] }; break;
                case 20: state.q20 = { trans: { r0_0:'', r0_1:'', r1_0:'', r1_1:'', r2_0:'', r2_1:'' }, traceNum: 6 }; break;
            }
            render();
        }

        render();
    </script>
</body>
</html>
