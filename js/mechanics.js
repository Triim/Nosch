/**
 * MECHANICS - Interactive question handlers for projekt1
 */

window.MECHANICS = window.MECHANICS || {};

// Q1: loopOrder
window.MECHANICS.loopOrder = function(container, data, onState) {
    let localState = { clicked: [], verified: false, attemptCount: 0 };
    const grid = [[7, 4, 9], [2, 5, 8], [3, 6, 1]];
    const correct = [[2,0], [2,2], [1,1], [0,0], [0,2]];

    function renderQ1() {
        let html = `<div class="code-block"><span class="keyword">for</span> i <span class="keyword">in</span> <span class="keyword">range</span>(<span class="number">2</span>, <span class="number">-1</span>, <span class="number">-1</span>):
    <span class="keyword">for</span> j <span class="keyword">in</span> <span class="keyword">range</span>(<span class="number">3</span>):
        <span class="keyword">if</span> (i + j) % <span class="number">2</span> == <span class="number">0</span>:
            <span class="keyword">paint</span>(grid[i][j])</div>
        <div class="interactive-area"><div class="grid-3x3">`;

        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                const clickIndex = localState.clicked.findIndex(c => c[0] === i && c[1] === j);
                const isSelected = clickIndex !== -1;
                html += `<div class="grid-cell ${isSelected ? 'clicked' : ''}" data-i="${i}" data-j="${j}">
                    ${grid[i][j]}<span class="cell-label">${isSelected ? clickIndex + 1 : '[' + i + ',' + j + ']'}</span>
                </div>`;
            }
        }

        html += `</div>
            <div class="progress">Selected: ${localState.clicked.length} / 5</div>
            <div style="margin-top: 20px;">`;

        if (localState.clicked.length > 0) {
            html += `<button class="undo-btn" style="margin-right: 12px; padding: 8px 12px; background: #ccc; color: #333; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">← Undo</button>`;
        }

        if (localState.clicked.length === 5) {
            html += `<button class="check-btn" style="padding: 8px 24px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">Check Answer</button>`;
        }

        html += `</div>`;

        if (localState.verified) {
            html += `<div class="completion show">✓ Correct! You traced the nested loops correctly.</div>`;
        } else if (localState.attemptCount > 0 && localState.clicked.length === 0) {
            html += `<div style="padding: 16px; background: #f8d7da; border: 2px solid #f5c6cb; border-radius: 8px; color: #721c24; font-weight: 600; margin-top: 20px; text-align: center;">✗ Not quite right. Try again!</div>`;
        }

        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function toggleCell(i, j) {
        if (localState.clicked.length >= 5 && !localState.clicked.find(c => c[0] === i && c[1] === j)) return;
        const idx = localState.clicked.findIndex(c => c[0] === i && c[1] === j);
        if (idx === -1) {
            localState.clicked.push([i, j]);
        } else {
            localState.clicked.splice(idx, 1);
        }
        update();
    }

    function undo() {
        if (localState.clicked.length > 0) {
            localState.clicked.pop();
            update();
        }
    }

    function checkAnswer() {
        const isCorrect = localState.clicked.length === correct.length &&
            correct.every((c, i) => JSON.stringify(localState.clicked[i]) === JSON.stringify(c));

        localState.attemptCount++;

        if (isCorrect) {
            localState.verified = true;
        } else {
            localState.clicked = [];
            localState.verified = false;
        }
        update();
    }

    function reset() {
        localState = { clicked: [], verified: false, attemptCount: 0 };
        update();
    }

    function update() {
        container.innerHTML = renderQ1();
        setTimeout(() => {
            container.querySelectorAll('.grid-cell').forEach(cell => {
                cell.onclick = () => toggleCell(+cell.dataset.i, +cell.dataset.j);
            });
            const undoBtn = container.querySelector('.undo-btn');
            if (undoBtn) undoBtn.onclick = undo;
            const checkBtn = container.querySelector('.check-btn');
            if (checkBtn) checkBtn.onclick = checkAnswer;
            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = reset;
        }, 0);
        onState(localState.verified);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q11: Extract Fragment (Slice notation)
window.MECHANICS.sliceBuilder = function(container, data, onState) {
    let localState = { start: null, stop: null, step: null };

    function renderQ11() {
        const arr = [5, 10, 15, 20, 25, 30, 35];
        const target = [30, 20, 10];

        let result = [];
        if (localState.start !== null && localState.stop !== null && localState.step !== null) {
            const s = localState.start < 0 ? 7 + localState.start : localState.start;
            const e = localState.stop < 0 ? 7 + localState.stop : localState.stop;
            if (localState.step > 0) {
                for (let i = s; i < e; i += localState.step) result.push(arr[i]);
            } else if (localState.step < 0) {
                for (let i = s; i > e; i += localState.step) result.push(arr[i]);
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
                    arr[<input type="number" class="q11-start" style="width: 40px; padding: 4px; border: 1px solid #ddd; border-radius: 4px;" value="${localState.start ?? ''}">
                    :<input type="number" class="q11-stop" style="width: 40px; padding: 4px; border: 1px solid #ddd; border-radius: 4px;" value="${localState.stop ?? ''}">
                    :<input type="number" class="q11-step" style="width: 40px; padding: 4px; border: 1px solid #ddd; border-radius: 4px;" value="${localState.step ?? ''}">]
                </div>
                <div style="padding: 12px; background: #f0f7ff; border-radius: 6px; margin: 15px 0; font-family: monospace;">
                    Result: ${JSON.stringify(result)}
                </div>
                <div style="padding: 12px; background: #e7f3ff; border-radius: 6px; font-family: monospace;">
                    Target: ${JSON.stringify(target)}
                </div>`;

        if (isCorrect) {
            html += `<div class="completion show">✓ Slice extracts correct fragment!</div>`;
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ11();
        setTimeout(() => {
            const startInput = container.querySelector('.q11-start');
            const stopInput = container.querySelector('.q11-stop');
            const stepInput = container.querySelector('.q11-step');
            const resetBtn = container.querySelector('.reset-btn');

            if (startInput) startInput.onchange = () => {
                localState.start = startInput.value === '' ? null : parseInt(startInput.value);
                update();
            };
            if (stopInput) stopInput.onchange = () => {
                localState.stop = stopInput.value === '' ? null : parseInt(stopInput.value);
                update();
            };
            if (stepInput) stepInput.onchange = () => {
                localState.step = stepInput.value === '' ? null : parseInt(stepInput.value);
                update();
            };
            if (resetBtn) resetBtn.onclick = () => {
                localState = { start: null, stop: null, step: null };
                update();
            };
        }, 0);

        const isCorrect = localState.start !== null && localState.stop !== null && localState.step !== null &&
            JSON.stringify(result()) === JSON.stringify([30, 20, 10]);
        onState(isCorrect);
    }

    function result() {
        const arr = [5, 10, 15, 20, 25, 30, 35];
        let result = [];
        if (localState.start !== null && localState.stop !== null && localState.step !== null) {
            const s = localState.start < 0 ? 7 + localState.start : localState.start;
            const e = localState.stop < 0 ? 7 + localState.stop : localState.stop;
            if (localState.step > 0) {
                for (let i = s; i < e; i += localState.step) result.push(arr[i]);
            } else if (localState.step < 0) {
                for (let i = s; i > e; i += localState.step) result.push(arr[i]);
            }
        }
        return result;
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q12: Build Dictionary
window.MECHANICS.dictContract = function(container, data, onState) {
    let localState = { pairs: [] };

    function renderQ12() {
        const keys = ['a', 'b', 'c'];
        const d = {};
        localState.pairs.forEach(p => d[p[0]] = p[1]);

        const checks = [
            {expr: `d["a"] == 2`, value: d['a'] === 2},
            {expr: `d.get("b", 0) == 0`, value: d['b'] === undefined},
            {expr: `d["c"] == d["a"] + 3`, value: d['c'] === d['a'] + 3},
            {expr: `len(d) == 2`, value: Object.keys(d).length === 2}
        ];

        const allPass = checks.every(c => c.value);

        let html = `<div class="question-header"><div class="question-number">Advanced • Programming</div>
            <div class="question-title">Q12: Build Dictionary</div></div>
            <div class="question-description">Build a dictionary that satisfies all four requirements simultaneously.</div>
            <div class="code-block"><code>${checks.map(c => c.value ? `✓ ${c.expr}` : `✗ ${c.expr}`).join('\n')}</code></div>
            <div class="interactive-area">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div>
                        <strong>Add Pairs:</strong>
                        <div style="margin-top: 10px;">
                            <select id="q12-keySelect" style="padding: 6px; border: 1px solid #ddd; border-radius: 4px;">
                                ${keys.map(k => `<option value="${k}">${k}</option>`).join('')}
                            </select>
                            <input type="number" id="q12-valInput" style="padding: 6px; border: 1px solid #ddd; border-radius: 4px; margin: 0 4px; width: 60px;" placeholder="value">
                            <button class="q12-add-btn" style="padding: 6px 12px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Add</button>
                        </div>
                        <div style="margin-top: 15px;">
                            <strong style="font-size: 12px;">Current Dictionary:</strong>
                            <div style="font-family: monospace; background: white; padding: 10px; border: 1px solid #ddd; border-radius: 6px; margin-top: 8px;">
                                ${Object.entries(d).length === 0 ? '{}' : '{' + Object.entries(d).map((e, i) => `<div style="display: flex; justify-content: space-between; align-items: center;"><span>"${e[0]}": ${e[1]}</span><button class="q12-remove-btn" data-key="${e[0]}" style="background: #ff4444; color: white; border: none; padding: 2px 6px; border-radius: 3px; cursor: pointer; font-size: 10px; margin-left: 10px;">Remove</button></div>`).join('') + '}'}
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
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ12();
        setTimeout(() => {
            const addBtn = container.querySelector('.q12-add-btn');
            if (addBtn) {
                addBtn.onclick = () => {
                    const key = document.getElementById('q12-keySelect').value;
                    const val = parseInt(document.getElementById('q12-valInput').value);
                    if (isNaN(val)) return;
                    const existing = localState.pairs.findIndex(p => p[0] === key);
                    if (existing >= 0) localState.pairs[existing] = [key, val];
                    else localState.pairs.push([key, val]);
                    document.getElementById('q12-valInput').value = '';
                    update();
                };
            }

            container.querySelectorAll('.q12-remove-btn').forEach(btn => {
                btn.onclick = () => {
                    const key = btn.dataset.key;
                    localState.pairs = localState.pairs.filter(p => p[0] !== key);
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { pairs: [] };
                update();
            };
        }, 0);

        const d = {};
        localState.pairs.forEach(p => d[p[0]] = p[1]);
        const isCorrect = d['a'] === 2 && d['b'] === undefined && d['c'] === d['a'] + 3 && Object.keys(d).length === 2;
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q13: Sequence Law (Polynomial)
window.MECHANICS.sequenceRule = function(container, data, onState) {
    let localState = { c2: 0, c1: 0, c0: 0 };

    function renderQ13() {
        const target = [2, 6, 12, 20, 30, 42, 56];
        const c2 = localState.c2, c1 = localState.c1, c0 = localState.c0;
        const generated = Array.from({length: 7}, (_, i) => c2 * (i+1) * (i+1) + c1 * (i+1) + c0);
        const allPass = generated.every((v, i) => v === target[i]);

        let html = `<div class="question-header"><div class="question-number">Advanced • Mathematics</div>
            <div class="question-title">Q13: Sequence Law</div></div>
            <div class="question-description">Adjust coefficients to generate the exact sequence, including hidden test cases.</div>
            <div class="code-block"><code>a(n) = c2·n² + c1·n + c0
Visible: n=1..5: [2, 6, 12, 20, 30]
(More hidden tests will check your solution)</code></div>
            <div class="interactive-area">
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0;">
                    <div><label>c2 (n²)</label><input type="number" class="q13-c2" value="${c2}" style="width: 100%; padding: 6px; border: 1px solid #ddd; border-radius: 4px;"></div>
                    <div><label>c1 (n)</label><input type="number" class="q13-c1" value="${c1}" style="width: 100%; padding: 6px; border: 1px solid #ddd; border-radius: 4px;"></div>
                    <div><label>c0 (const)</label><input type="number" class="q13-c0" value="${c0}" style="width: 100%; padding: 6px; border: 1px solid #ddd; border-radius: 4px;"></div>
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
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ13();
        setTimeout(() => {
            const c2Input = container.querySelector('.q13-c2');
            const c1Input = container.querySelector('.q13-c1');
            const c0Input = container.querySelector('.q13-c0');
            const resetBtn = container.querySelector('.reset-btn');

            if (c2Input) c2Input.onchange = () => { localState.c2 = parseInt(c2Input.value); update(); };
            if (c1Input) c1Input.onchange = () => { localState.c1 = parseInt(c1Input.value); update(); };
            if (c0Input) c0Input.onchange = () => { localState.c0 = parseInt(c0Input.value); update(); };
            if (resetBtn) resetBtn.onclick = () => {
                localState = { c2: 0, c1: 0, c0: 0 };
                update();
            };
        }, 0);

        const target = [2, 6, 12, 20, 30, 42, 56];
        const generated = Array.from({length: 7}, (_, i) => localState.c2 * (i+1) * (i+1) + localState.c1 * (i+1) + localState.c0);
        const isCorrect = generated.every((v, i) => v === target[i]);
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q14: String Operations
window.MECHANICS.stringEqualize = function(container, data, onState) {
    let localState = { chain: [] };

    function renderQ14() {
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
        localState.chain.forEach(opId => {
            const op = ops.find(o => o.id === opId);
            if (op) current = op.fn(current);
        });

        const isCorrect = current === target;

        let html = `<div class="question-header"><div class="question-number">Intermediate • Programming</div>
            <div class="question-title">Q14: String Transform</div></div>
            <div class="question-description">Chain operations in the correct order to match the target.</div>
            <div class="code-block"><code>Start:  "${start}"
Target: "${target}"</code></div>
            <div class="interactive-area">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div>
                        <strong>Available Operations:</strong>
                        <div style="display: grid; grid-template-columns: 1fr; gap: 6px; margin-top: 10px;">
                            ${ops.map(op => `<button class="q14-op-btn" data-op="${op.id}" style="padding: 8px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">${op.label}</button>`).join('')}
                        </div>
                    </div>
                    <div>
                        <strong>Transformation Chain:</strong>
                        <div style="background: white; padding: 10px; border: 1px solid #ddd; border-radius: 6px; font-family: monospace; font-size: 11px; min-height: 60px; margin-bottom: 10px;">
                            <div style="color: #666; margin-bottom: 8px;">0. "${start}"</div>
                            ${localState.chain.length === 0 ? '<div style="color: #999;">[add operations →]</div>' : localState.chain.map((opId, i) => {
                                const op = ops.find(o => o.id === opId);
                                let stepResult = start;
                                for (let j = 0; j <= i; j++) {
                                    const stepOp = ops.find(o => o.id === localState.chain[j]);
                                    if (stepOp) stepResult = stepOp.fn(stepResult);
                                }
                                return `<div style="display: flex; justify-content: space-between; margin: 4px 0; padding: 4px 0; border-bottom: 1px solid #eee;">
                                    <span>${i+1}. ${op ? op.label : opId}</span>
                                    <button class="q14-remove-btn" data-idx="${i}" style="font-size: 10px; padding: 0 4px; background: #ff4444; color: white; border: none; border-radius: 2px; cursor: pointer;">×</button>
                                </div>
                                <div style="color: #3844FF; font-weight: 600; margin: 2px 0 8px 0;">"${stepResult}"</div>`;
                            }).join('')}
                        </div>
                        <div style="padding: 10px; background: ${isCorrect ? '#d4edda' : '#e7f3ff'}; border-radius: 6px; border: 1px solid ${isCorrect ? '#28a745' : '#3844FF'};">
                            <div style="font-size: 10px; color: #666; margin-bottom: 4px;">Result:</div>
                            <div style="font-family: monospace; font-weight: 600; font-size: 12px; color: ${isCorrect ? '#155724' : '#1d1d1f'};">"${current}"</div>
                        </div>
                    </div>
                </div>`;

        if (isCorrect) {
            html += `<div class="completion show">✓ String transformation successful!</div>`;
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ14();
        setTimeout(() => {
            container.querySelectorAll('.q14-op-btn').forEach(btn => {
                btn.onclick = () => {
                    const opId = btn.dataset.op;
                    localState.chain.push(opId);
                    update();
                };
            });

            container.querySelectorAll('.q14-remove-btn').forEach(btn => {
                btn.onclick = () => {
                    const idx = parseInt(btn.dataset.idx);
                    localState.chain.splice(idx, 1);
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { chain: [] };
                update();
            };
        }, 0);

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
        localState.chain.forEach(opId => {
            const op = ops.find(o => o.id === opId);
            if (op) current = op.fn(current);
        });
        const isCorrect = current === target;
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q15: Bubble Sort / Minimum Swaps
window.MECHANICS.handSort = function(container, data, onState) {
    let localState = { arr: [8, 2, 6, 1, 7, 3, 5, 4], swaps: 0, minSwaps: null };

    function countInversions(arr) {
        let count = 0;
        for (let i = 0; i < arr.length; i++) {
            for (let j = i + 1; j < arr.length; j++) {
                if (arr[i] > arr[j]) count++;
            }
        }
        return count;
    }

    function renderQ15() {
        if (localState.minSwaps === null) {
            localState.minSwaps = countInversions([8, 2, 6, 1, 7, 3, 5, 4]);
        }

        const arr = localState.arr;
        const sorted = [...arr].sort((a, b) => a - b);
        const isSorted = JSON.stringify(arr) === JSON.stringify(sorted);
        const minSwaps = localState.minSwaps;

        let html = `<div class="question-header"><div class="question-number">Advanced • Programming</div>
            <div class="question-title">Q15: Sort with Minimum Swaps</div></div>
            <div class="question-description">Sort the array using ONLY adjacent swaps, in minimum moves.</div>
            <div class="code-block"><code>Array: [${arr.join(', ')}]
Only swap neighbors!
Target: minimum ${minSwaps} swaps</code></div>
            <div class="interactive-area">
                <div style="display: flex; gap: 8px; align-items: flex-end; margin: 20px 0; height: 200px;">
                    ${arr.map((val, i) => `<div style="width: 40px; height: ${val * 30}px; background: #3844FF; border-radius: 4px; position: relative;">
                        ${i < arr.length - 1 ? `<button class="q15-swap-btn" data-idx="${i}" style="position: absolute; bottom: -25px; left: 50%; transform: translateX(-50%); padding: 4px 8px; background: #999; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 11px; font-weight: 600;">⇄</button>` : ''}
                    </div>`).join('')}
                </div>
                <div style="text-align: center; font-weight: 600; padding: 12px; background: #f0f7ff; border-radius: 6px;">
                    Swaps: ${localState.swaps} ${localState.swaps === minSwaps && isSorted ? '✓' : (isSorted ? `(need minimum ${minSwaps})` : '')}
                </div>`;

        if (isSorted && localState.swaps === minSwaps) {
            html += `<div class="completion show">✓ Sorted in minimum swaps!</div>`;
        } else if (isSorted && localState.swaps > minSwaps) {
            html += `<div style="padding: 12px; background: #fff3cd; border: 1px solid #ffc107; border-radius: 6px; color: #856404; margin-top: 15px; font-weight: 600;">⚠ Sorted, but used ${localState.swaps} swaps instead of ${minSwaps}. Try again!</div>`;
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ15();
        setTimeout(() => {
            container.querySelectorAll('.q15-swap-btn').forEach(btn => {
                btn.onclick = () => {
                    const i = parseInt(btn.dataset.idx);
                    [localState.arr[i], localState.arr[i+1]] = [localState.arr[i+1], localState.arr[i]];
                    localState.swaps++;
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { arr: [8, 2, 6, 1, 7, 3, 5, 4], swaps: 0, minSwaps: localState.minSwaps };
                update();
            };
        }, 0);

        const arr = localState.arr;
        const sorted = [...arr].sort((a, b) => a - b);
        const isSorted = JSON.stringify(arr) === JSON.stringify(sorted);
        const isCorrect = isSorted && localState.swaps === localState.minSwaps;
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q16: Shape with Constraints (Rectangle)
window.MECHANICS.shapeArea = function(container, data, onState) {
    let localState = { w: 3, h: 8 };

    function renderQ16() {
        const w = localState.w, h = localState.h;
        const area = w * h, perim = 2 * (w + h);
        const areaMatch = area === 24, perimMatch = perim === 20;

        let html = `<div class="question-header"><div class="question-number">Introductory • Mathematics</div>
            <div class="question-title">Q16: Rectangle Constraints</div></div>
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
                        <input type="number" class="q16-w" value="${w}" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; margin-top: 6px;">
                    </div>
                    <div>
                        <label style="font-weight: 600;">Height (h)</label>
                        <input type="number" class="q16-h" value="${h}" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; margin-top: 6px;">
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
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ16();
        setTimeout(() => {
            const wInput = container.querySelector('.q16-w');
            const hInput = container.querySelector('.q16-h');
            const resetBtn = container.querySelector('.reset-btn');

            if (wInput) wInput.onchange = () => { localState.w = parseInt(wInput.value); update(); };
            if (hInput) hInput.onchange = () => { localState.h = parseInt(hInput.value); update(); };
            if (resetBtn) resetBtn.onclick = () => {
                localState = { w: 3, h: 8 };
                update();
            };
        }, 0);

        const area = localState.w * localState.h;
        const perim = 2 * (localState.w + localState.h);
        const isCorrect = area === 24 && perim === 20;
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q17: Orbit on Circle (Three Planets)
window.MECHANICS.threePlanets = function(container, data, onState) {
    let localState = { p: 2, q: 3, r: 4 };

    function renderQ17() {
        const p = localState.p, q = localState.q, r = localState.r;
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
                    <button class="q17-dec-btn" data-key="${pl.key}" style="padding:8px 12px;background:#999;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:600;">−</button>
                    <span style="font-size:24px;font-weight:700;min-width:40px;text-align:center;color:${pl.color};">${pl.val}</span>
                    <button class="q17-inc-btn" data-key="${pl.key}" style="padding:8px 12px;background:${pl.color};color:white;border:none;border-radius:4px;cursor:pointer;font-weight:600;">+</button>
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
            html += `<div class="completion show">✓ All three planets reunite at exactly tick 105 and are pairwise coprime!</div>`;
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ17();
        setTimeout(() => {
            container.querySelectorAll('.q17-dec-btn').forEach(btn => {
                btn.onclick = () => {
                    const key = btn.dataset.key;
                    localState[key] = Math.max(2, localState[key] - 1);
                    update();
                };
            });

            container.querySelectorAll('.q17-inc-btn').forEach(btn => {
                btn.onclick = () => {
                    const key = btn.dataset.key;
                    localState[key] = Math.min(9, localState[key] + 1);
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { p: 2, q: 3, r: 4 };
                update();
            };
        }, 0);

        const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);
        const lcm2 = (a, b) => a * b / gcd(a, b);
        const lcm = lcm2(lcm2(localState.p, localState.q), localState.r);
        const pairwiseCoprime = gcd(localState.p, localState.q) === 1 && gcd(localState.q, localState.r) === 1 && gcd(localState.p, localState.r) === 1;
        const isCorrect = (lcm === 105 && pairwiseCoprime);
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q18: Bits (Binary Operations)
window.MECHANICS.catchBits = function(container, data, onState) {
    let localState = { b: [0, 0, 0, 0, 0] };

    function renderQ18() {
        const a = [1, 0, 1, 1, 0];
        const b = localState.b;
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
                    ${b.map((bit, i) => `<button class="q18-bit-btn" data-idx="${i}" style="padding: 12px; background: ${bit ? '#3844FF' : 'white'}; color: ${bit ? 'white' : '#1d1d1f'}; border: 2px solid #3844FF; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 14px;">${bit}</button>`).join('')}
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
            html += `<div class="completion show">✓ Both binary operations satisfied!</div>`;
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ18();
        setTimeout(() => {
            container.querySelectorAll('.q18-bit-btn').forEach(btn => {
                btn.onclick = () => {
                    const idx = parseInt(btn.dataset.idx);
                    localState.b[idx] = 1 - localState.b[idx];
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { b: [0, 0, 0, 0, 0] };
                update();
            };
        }, 0);

        const a = [1, 0, 1, 1, 0];
        const andRes = a.map((v, i) => v & localState.b[i]);
        const orRes = a.map((v, i) => v | localState.b[i]);
        const andTarget = [0, 0, 1, 1, 0];
        const orTarget = [1, 1, 1, 1, 0];
        const andPass = JSON.stringify(andRes) === JSON.stringify(andTarget);
        const orPass = JSON.stringify(orRes) === JSON.stringify(orTarget);
        onState(andPass && orPass);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q19: Operations inside 4 nested loops
window.MECHANICS.growthBuilder = function(container, data, onState) {
    let localState = { ops: [0, 0, 0, 0] };

    function renderQ19() {
        const ops = localState.ops;
        const count = (n) => ops.reduce((s, c, d) => s + c * Math.pow(n, d), 0);
        const target = (n) => n * n * n + 2 * n + 1;
        const visible = [1, 2, 3, 4];
        const hidden = [5, 6];
        const allPass = [...visible, ...hidden].every(n => count(n) === target(n));

        const dot = (lvl) => `<span class="q19-dot" data-lvl="${lvl}" title="click to remove" style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;background:#3844FF;color:white;font-size:11px;cursor:pointer;margin:2px;">●</span>`;
        const addBtn = (lvl) => `<button class="q19-add-btn" data-lvl="${lvl}" style="padding:4px 10px;background:white;border:1px dashed #3844FF;color:#3844FF;border-radius:6px;cursor:pointer;font-weight:600;font-size:12px;margin-left:6px;vertical-align:middle;">＋ op</button>`;
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
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ19();
        setTimeout(() => {
            container.querySelectorAll('.q19-dot').forEach(dot => {
                dot.onclick = () => {
                    const lvl = parseInt(dot.dataset.lvl);
                    localState.ops[lvl] = Math.max(0, localState.ops[lvl] - 1);
                    update();
                };
            });

            container.querySelectorAll('.q19-add-btn').forEach(btn => {
                btn.onclick = () => {
                    const lvl = parseInt(btn.dataset.lvl);
                    localState.ops[lvl]++;
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { ops: [0, 0, 0, 0] };
                update();
            };
        }, 0);

        const count = (n) => localState.ops.reduce((s, c, d) => s + c * Math.pow(n, d), 0);
        const target = (n) => n * n * n + 2 * n + 1;
        const isCorrect = [1, 2, 3, 4, 5, 6].every(n => count(n) === target(n));
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q20: Divisibility-by-3 Automaton
window.MECHANICS.divAutomaton = function(container, data, onState) {
    let localState = { trans: { r0_0: '', r0_1: '', r1_0: '', r1_1: '', r2_0: '', r2_1: '' }, traceNum: 6 };

    function renderQ20() {
        const T = localState.trans;

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

        const opt = (key, val, label) => `<option value="${val}" ${T[key] === val ? 'selected' : ''}>${label}</option>`;
        const sel = (key) => `<select class="q20-select" data-key="${key}" style="padding:5px;border-radius:4px;border:1px solid #ddd;font-size:13px;">
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

        const cell = (n) => {
            const v = verdict(n), ok = matches(n);
            const bg = v === null ? '#f1f1f4' : (ok ? '#d4edda' : '#f8d7da');
            const col = v === null ? '#555' : (ok ? '#155724' : '#721c24');
            const selBorder = localState.traceNum === n ? '2px solid #3844FF' : '1px solid transparent';
            return `<div class="q20-cell" data-n="${n}" style="cursor:pointer;padding:8px 4px;background:${bg};color:${col};border-radius:6px;text-align:center;border:${selBorder};">
                <div style="font-weight:700;">${n}</div>
                <div style="font-family:monospace;font-size:11px;">${n.toString(2)}</div>
                <div style="font-size:12px;">${v === null ? '?' : (ok ? '✓' : '✗')}</div>
            </div>`;
        };

        const tn = localState.traceNum;
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
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ20();
        setTimeout(() => {
            container.querySelectorAll('.q20-select').forEach(sel => {
                sel.onchange = () => {
                    localState.trans[sel.dataset.key] = sel.value;
                    update();
                };
            });

            container.querySelectorAll('.q20-cell').forEach(cell => {
                cell.onclick = () => {
                    localState.traceNum = parseInt(cell.dataset.n);
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { trans: { r0_0: '', r0_1: '', r1_0: '', r1_1: '', r2_0: '', r2_1: '' }, traceNum: 6 };
                update();
            };
        }, 0);

        const runMachine = (n) => {
            const bin = n.toString(2);
            let s = 'r0';
            for (const bit of bin) {
                const nxt = localState.trans[s + '_' + bit];
                if (!nxt) return { complete: false, accept: false };
                s = nxt;
            }
            return { complete: true, accept: s === 'r0' };
        };

        const all = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 21, 33, 45, 100, 17, 19];
        const allPass = all.every(n => {
            const r = runMachine(n);
            return r.complete && r.accept === (n % 3 === 0);
        });
        onState(allPass);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q2: Grade Thresholds (Number Line with Draggable Markers)
window.MECHANICS.gradeThresholds = function(container, data, onState) {
    let localState = { boundaries: [30, 60, 90] };

    function getGrade(score, a, b, c) {
        if (score < a) return 'F';
        if (score < b) return 'C';
        if (score < c) return 'B';
        return 'A';
    }

    function renderQ2() {
        const testCases = [
            {val: 49, expected: 'F'}, {val: 50, expected: 'C'},
            {val: 69, expected: 'C'}, {val: 70, expected: 'B'},
            {val: 84, expected: 'B'}, {val: 85, expected: 'A'}
        ];
        const [a, b, c] = localState.boundaries;
        const allPass = testCases.every(tc => getGrade(tc.val, a, b, c) === tc.expected);

        let html = `<div class="question-header"><div class="question-number">Intermediate • Programming, Reasoning</div>
            <div class="question-title">Q2: Grade Boundaries</div></div>
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
                <div class="marker" style="left: ${a}%" data-idx="0">A</div>
                <div class="marker" style="left: ${b}%" data-idx="1">B</div>
                <div class="marker" style="left: ${c}%" data-idx="2">C</div>
            </div><div class="test-case-list">`;
        testCases.forEach(tc => {
            const grade = getGrade(tc.val, a, b, c);
            const pass = grade === tc.expected;
            html += `<div class="test-case ${pass ? 'pass' : 'fail'}">${tc.val} → ${grade}</div>`;
        });
        html += `</div>`;
        if (allPass && a === 50 && b === 70 && c === 85) {
            html += `<div class="completion show">✓ Correct! All test cases pass.</div>`;
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function dragMarker(e, idx) {
        const line = e.target.parentElement;
        const rect = line.getBoundingClientRect();
        const startX = e.clientX;
        const startVal = localState.boundaries[idx];

        function move(me) {
            const delta = me.clientX - startX;
            const newVal = Math.max(0, Math.min(100, startVal + (delta / rect.width) * 100));
            localState.boundaries[idx] = Math.round(newVal);
            update();
        }

        function stop() {
            document.removeEventListener('mousemove', move);
            document.removeEventListener('mouseup', stop);
        }

        document.addEventListener('mousemove', move);
        document.addEventListener('mouseup', stop);
    }

    function update() {
        container.innerHTML = renderQ2();
        setTimeout(() => {
            container.querySelectorAll('.marker').forEach(marker => {
                marker.onmousedown = (e) => dragMarker(e, parseInt(marker.dataset.idx));
            });
            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { boundaries: [30, 60, 90] };
                update();
            };
        }, 0);

        const [a, b, c] = localState.boundaries;
        const testCases = [
            {val: 49, expected: 'F'}, {val: 50, expected: 'C'},
            {val: 69, expected: 'C'}, {val: 70, expected: 'B'},
            {val: 84, expected: 'B'}, {val: 85, expected: 'A'}
        ];
        const allPass = testCases.every(tc => getGrade(tc.val, a, b, c) === tc.expected) && a === 50 && b === 70 && c === 85;
        onState(allPass);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q3: Quadratic Through Points (Parabola with Sliders)
window.MECHANICS.quadraticThroughPts = function(container, data, onState) {
    let localState = { a: 2, b: 0, c: 0 };

    function checkParabola(a, b, c, points) {
        const tol = 0.05;
        return points.every(p => Math.abs(a * p[0] * p[0] + b * p[0] + c - p[1]) < tol);
    }

    function drawParabola() {
        const canvas = document.getElementById('q3-canvas');
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
            const py = localState.a * px * px + localState.b * px + localState.c;
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

    function renderQ3() {
        const {a, b, c} = localState;
        const points = [[0, 3], [1, 0], [3, 0]];
        const check3 = checkParabola(a, b, c, points);

        let html = `<div class="question-header"><div class="question-number">Intermediate • Mathematics</div>
            <div class="question-title">Q3: Parabola</div></div>
            <div class="question-description">Adjust a, b, c so the parabola passes through all three rings.</div>
            <div class="code-block">y = a·x² + b·x + c</div>
            <div class="interactive-area"><canvas id="q3-canvas" width="500" height="400"></canvas>
            <div class="slider-row">
                <div class="slider-label">a:</div>
                <input type="range" class="q3-a-slider" min="-5" max="5" step="0.1" value="${a}" style="width: 100%; height: 6px; border-radius: 3px; background: #ddd; outline: none; -webkit-appearance: none; appearance: none;">
                <input type="number" class="q3-a-input" step="0.01" value="${a.toFixed(2)}" style="width: 70px; padding: 4px; border: 1px solid #ddd; border-radius: 4px; margin-left: 10px;">
            </div>
            <div class="slider-row">
                <div class="slider-label">b:</div>
                <input type="range" class="q3-b-slider" min="-10" max="10" step="0.1" value="${b}" style="width: 100%; height: 6px; border-radius: 3px; background: #ddd; outline: none; -webkit-appearance: none; appearance: none;">
                <input type="number" class="q3-b-input" step="0.01" value="${b.toFixed(2)}" style="width: 70px; padding: 4px; border: 1px solid #ddd; border-radius: 4px; margin-left: 10px;">
            </div>
            <div class="slider-row">
                <div class="slider-label">c:</div>
                <input type="range" class="q3-c-slider" min="-5" max="10" step="0.1" value="${c}" style="width: 100%; height: 6px; border-radius: 3px; background: #ddd; outline: none; -webkit-appearance: none; appearance: none;">
                <input type="number" class="q3-c-input" step="0.01" value="${c.toFixed(2)}" style="width: 70px; padding: 4px; border: 1px solid #ddd; border-radius: 4px; margin-left: 10px;">
            </div>`;
        if (check3) {
            html += `<div class="completion show">✓ Correct! Parabola passes through all points.</div>`;
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ3();
        setTimeout(() => {
            const aSlider = container.querySelector('.q3-a-slider');
            const aInput = container.querySelector('.q3-a-input');
            const bSlider = container.querySelector('.q3-b-slider');
            const bInput = container.querySelector('.q3-b-input');
            const cSlider = container.querySelector('.q3-c-slider');
            const cInput = container.querySelector('.q3-c-input');
            const resetBtn = container.querySelector('.reset-btn');

            if (aSlider) aSlider.oninput = () => { localState.a = parseFloat(aSlider.value); update(); };
            if (aInput) aInput.onchange = () => { localState.a = parseFloat(aInput.value); update(); };
            if (bSlider) bSlider.oninput = () => { localState.b = parseFloat(bSlider.value); update(); };
            if (bInput) bInput.onchange = () => { localState.b = parseFloat(bInput.value); update(); };
            if (cSlider) cSlider.oninput = () => { localState.c = parseFloat(cSlider.value); update(); };
            if (cInput) cInput.onchange = () => { localState.c = parseFloat(cInput.value); update(); };
            if (resetBtn) resetBtn.onclick = () => {
                localState = { a: 2, b: 0, c: 0 };
                update();
            };
            drawParabola();
        }, 0);

        const points = [[0, 3], [1, 0], [3, 0]];
        const isCorrect = checkParabola(localState.a, localState.b, localState.c, points);
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q4: XOR Circuit (Logic Gates)
window.MECHANICS.xorCircuit = function(container, data, onState) {
    let localState = { nodes: [], outSource: null };

    function evalGate(sourceId, a, b) {
        if (sourceId === 'A') return a;
        if (sourceId === 'B') return b;
        const node = localState.nodes.find(n => n.id === sourceId);
        if (!node) return null;
        const in1 = evalGate(node.in1, a, b);
        const in2 = evalGate(node.in2, a, b);
        if (in1 === null || (node.type !== 'NOT' && in2 === null)) return null;
        if (node.type === 'AND') return (in1 && in2) ? 1 : 0;
        if (node.type === 'OR') return (in1 || in2) ? 1 : 0;
        if (node.type === 'NOT') return in1 ? 0 : 1;
        return null;
    }

    function q4AddGate(type) {
        const idx = localState.nodes.length + 1;
        localState.nodes.push({ id: 'G' + idx, type, in1: null, in2: null });
        update();
    }

    function q4RemoveGate(idx) {
        const gateId = 'G' + (idx + 1);
        localState.nodes.splice(idx, 1);
        if (localState.outSource === gateId) localState.outSource = null;
        localState.nodes.forEach((g, i) => {
            if (g.in1 === gateId) g.in1 = null;
            if (g.in2 === gateId) g.in2 = null;
        });
        update();
    }

    function q4SetInput(gateId, inputIdx, value) {
        const gate = localState.nodes.find(g => g.id === gateId);
        if (gate) {
            if (inputIdx === 0) gate.in1 = value || null;
            else gate.in2 = value || null;
            update();
        }
    }

    function q4SetOutput(value) {
        localState.outSource = value || null;
        update();
    }

    function q4Draw() {
        const canvas = document.getElementById('q4Canvas');
        if (!canvas) return;
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

        const gateY = 40, gateSpacingX = 110, gateW = 50, gateH = 40;

        localState.nodes.forEach((gate, idx) => {
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

        if (localState.outSource) {
            const [sx, sy] = q4GetSourcePos(localState.outSource);
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

    function renderQ4() {
        let html = `<div class="question-header"><div class="question-number">Advanced • Programming, Reasoning</div>
            <div class="question-title">Q4: XOR Circuit</div></div>
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
                        <button class="q4-add-and" style="width: 100%; margin-bottom: 6px; padding: 6px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">+ AND</button>
                        <button class="q4-add-or" style="width: 100%; margin-bottom: 6px; padding: 6px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">+ OR</button>
                        <button class="q4-add-not" style="width: 100%; margin-bottom: 12px; padding: 6px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">+ NOT</button>
                        <div id="q4GateList" style="background: #f9f9fb; padding: 8px; border-radius: 6px; font-size: 11px;"></div>
                    </div>
                    <canvas id="q4Canvas" width="400" height="280" style="background: white; border: 1px solid #ddd; border-radius: 8px;"></canvas>
                    <div>
                        <strong style="display: block; margin-bottom: 8px; font-size: 12px;">📊 Output</strong>
                        <div id="q4TruthTable" style="font-family: monospace; font-size: 10px; background: white; padding: 8px; border: 1px solid #ddd; border-radius: 6px; line-height: 1.4;"></div>
                        <div id="q4OutputSelector" style="margin-top: 12px; padding: 8px; background: #e7f3ff; border-radius: 6px; border: 1px solid #3844FF;">
                            <label style="display: block; font-size: 10px; color: #666; margin-bottom: 4px;">Final output:</label>
                            <select id="q4OutputSelect" class="q4-output-select" style="width: 100%; padding: 4px; font-size: 11px; border: 1px solid #3844FF; border-radius: 4px;">
                                <option value="">— Select —</option>
                            </select>
                        </div>
                    </div>
                </div>
                <button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button>
            </div>`;

        return html;
    }

    function q4RenderGateList() {
        const list = document.getElementById('q4GateList');
        if (!list) return;

        let html = '';
        localState.nodes.forEach((gate, idx) => {
            const num = idx + 1;
            html += `<div style="background: white; padding: 8px; border-radius: 4px; margin-bottom: 6px; border: 1px solid #ddd;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <strong style="font-size: 11px;">G${num}: ${gate.type}</strong>
                    <button class="q4-remove-gate" data-idx="${idx}" style="background: #ff4444; color: white; border: none; border-radius: 3px; padding: 2px 6px; cursor: pointer; font-size: 9px;">✕</button>
                </div>
                ${gate.type !== 'NOT' ? `<select class="q4-input" data-gate="${gate.id}" data-input="0" style="width: 100%; padding: 3px; font-size: 10px; border: 1px solid #ddd; border-radius: 3px; margin-bottom: 3px;">
                    <option value="">In1: —</option>
                    <option value="A" ${gate.in1 === 'A' ? 'selected' : ''}>In1: A</option>
                    <option value="B" ${gate.in1 === 'B' ? 'selected' : ''}>In1: B</option>
                    ${localState.nodes.slice(0, idx).map((g, i) => `<option value="G${i+1}" ${gate.in1 === 'G' + (i+1) ? 'selected' : ''}>In1: G${i+1}</option>`).join('')}
                </select>` : ''}
                ${gate.type !== 'NOT' ? `<select class="q4-input" data-gate="${gate.id}" data-input="1" style="width: 100%; padding: 3px; font-size: 10px; border: 1px solid #ddd; border-radius: 3px;">
                    <option value="">In2: —</option>
                    <option value="A" ${gate.in2 === 'A' ? 'selected' : ''}>In2: A</option>
                    <option value="B" ${gate.in2 === 'B' ? 'selected' : ''}>In2: B</option>
                    ${localState.nodes.slice(0, idx).map((g, i) => `<option value="G${i+1}" ${gate.in2 === 'G' + (i+1) ? 'selected' : ''}>In2: G${i+1}</option>`).join('')}
                </select>` : `<select class="q4-input" data-gate="${gate.id}" data-input="0" style="width: 100%; padding: 3px; font-size: 10px; border: 1px solid #ddd; border-radius: 3px;">
                    <option value="">Input: —</option>
                    <option value="A" ${gate.in1 === 'A' ? 'selected' : ''}>Input: A</option>
                    <option value="B" ${gate.in1 === 'B' ? 'selected' : ''}>Input: B</option>
                    ${localState.nodes.slice(0, idx).map((g, i) => `<option value="G${i+1}" ${gate.in1 === 'G' + (i+1) ? 'selected' : ''}>Input: G${i+1}</option>`).join('')}
                </select>`}
            </div>`;
        });

        if (localState.nodes.length === 0) {
            html = `<div style="color: #999; font-size: 10px;">Add gates →</div>`;
        }

        list.innerHTML = html;

        const select = document.getElementById('q4OutputSelect');
        if (select) {
            let options = `<option value="">— Select —</option>
                <option value="A" ${localState.outSource === 'A' ? 'selected' : ''}>A</option>
                <option value="B" ${localState.outSource === 'B' ? 'selected' : ''}>B</option>`;
            if (localState.nodes) {
                localState.nodes.forEach((g, i) => {
                    options += `<option value="G${i+1}" ${localState.outSource === 'G' + (i+1) ? 'selected' : ''}>G${i+1}</option>`;
                });
            }
            select.innerHTML = options;
        }
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
            const actual = evalGate(localState.outSource, a, b);
            const match = actual === expected;
            if (!match) allPass = false;
            const color = actual === null ? '#999' : (match ? '#34C759' : '#ff4444');
            const display = actual === null ? '?' : actual;
            html += `<span style="color: ${color};">${a} ${b} ${display}</span><br>`;
        });

        if (allPass && localState.outSource) {
            html += `<div style="margin-top: 8px; padding: 6px; background: #d4edda; border: 1px solid #28a745; border-radius: 4px; color: #155724; font-weight: 600; font-size: 10px; text-align: center;">✓ Correct!</div>`;
        }

        area.innerHTML = html;
    }

    function update() {
        container.innerHTML = renderQ4();
        setTimeout(() => {
            const addAnd = container.querySelector('.q4-add-and');
            const addOr = container.querySelector('.q4-add-or');
            const addNot = container.querySelector('.q4-add-not');
            const resetBtn = container.querySelector('.reset-btn');

            if (addAnd) addAnd.onclick = () => { q4AddGate('AND'); };
            if (addOr) addOr.onclick = () => { q4AddGate('OR'); };
            if (addNot) addNot.onclick = () => { q4AddGate('NOT'); };

            container.querySelectorAll('.q4-remove-gate').forEach(btn => {
                btn.onclick = () => q4RemoveGate(parseInt(btn.dataset.idx));
            });

            container.querySelectorAll('.q4-input').forEach(sel => {
                sel.onchange = () => {
                    const gateId = sel.dataset.gate;
                    const inputIdx = parseInt(sel.dataset.input);
                    q4SetInput(gateId, inputIdx, sel.value);
                };
            });

            const outputSelect = container.querySelector('.q4-output-select');
            if (outputSelect) outputSelect.onchange = () => q4SetOutput(outputSelect.value);

            if (resetBtn) resetBtn.onclick = () => {
                localState = { nodes: [], outSource: null };
                update();
            };

            q4RenderGateList();
            q4Draw();
            q4UpdateTruthTable();
        }, 0);

        const xorTable = [[0,0,0], [0,1,1], [1,0,1], [1,1,0]];
        const allPass = xorTable.every(row => {
            const actual = evalGate(localState.outSource, row[0], row[1]);
            return actual === row[2];
        }) && localState.outSource;
        onState(allPass);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q5: Black Box Pipeline (Function Probing)
window.MECHANICS.blackBoxPipeline = function(container, data, onState) {
    let localState = { probes: {}, pipeline: [] };

    function probeFunction(input) {
        if (isNaN(input) || input < 0 || input > 20) return null;
        const result = (input * 3 + 1) % 7;
        localState.probes[input] = result;
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

    function renderQ5() {
        let html = `<div class="question-header"><div class="question-number">Advanced • Programming, Reasoning</div>
            <div class="question-title">Q5: Black Box</div></div>
            <div class="question-description">Discover a hidden function by probing it, then build a pipeline that replicates its behavior on all test inputs.</div>
            <div class="code-block"><code>Test range: x = 0..20 (21 test cases)
Probe any value to learn the pattern.
Assemble pipeline to match on ALL inputs.</code></div>
            <div class="interactive-area">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div>
                        <strong>🔬 Probe Function</strong>
                        <div style="margin: 10px 0;">
                            <input type="number" class="q5-probe-input" min="0" max="20" value="0" style="padding: 8px; width: 60px; border: 1px solid #ddd; border-radius: 4px;">
                            <button class="q5-probe-btn" style="padding: 8px 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Get f(x)</button>
                        </div>
                        <div id="probeLog" style="background: white; padding: 10px; border: 1px solid #ddd; border-radius: 6px; min-height: 150px; font-family: monospace; font-size: 11px; overflow-y: auto;"></div>
                    </div>
                    <div>
                        <strong>⚙️ Build Pipeline</strong>
                        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin: 10px 0;">
                            <button class="q5-op-btn" data-op="×2" style="padding: 8px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">×2</button>
                            <button class="q5-op-btn" data-op="×3" style="padding: 8px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">×3</button>
                            <button class="q5-op-btn" data-op="+1" style="padding: 8px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">+1</button>
                            <button class="q5-op-btn" data-op="+2" style="padding: 8px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">+2</button>
                            <button class="q5-op-btn" data-op="−1" style="padding: 8px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">−1</button>
                            <button class="q5-op-btn" data-op="mod 5" style="padding: 8px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">mod 5</button>
                            <button class="q5-op-btn" data-op="mod 7" style="padding: 8px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">mod 7</button>
                            <button class="q5-op-btn" data-op="x²" style="padding: 8px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">x²</button>
                        </div>
                        <div id="pipeline" style="background: white; padding: 10px; border: 1px solid #ddd; border-radius: 6px; min-height: 60px; display: flex; flex-wrap: wrap; gap: 6px; align-items: center;"></div>
                        <div id="resultQ5" style="margin-top: 10px; padding: 8px; background: #e7f3ff; border-radius: 6px; font-family: monospace; font-size: 12px; font-weight: 600;">Result for x=0: —</div>
                        <div id="matchCount" style="margin-top: 10px; text-align: center; font-weight: 600; padding: 8px; background: #f0f7ff; border-radius: 6px;">Match: 0 / 21</div>
                        <button id="submitQ5" class="q5-submit" style="margin-top: 12px; width: 100%; padding: 10px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px; display: none;">✓ Submit Pipeline</button>
                        <div id="q5TestResults" style="margin-top: 12px; max-height: 150px; overflow-y: auto; font-family: monospace; font-size: 10px; background: white; padding: 8px; border: 1px solid #ddd; border-radius: 6px;"></div>
                    </div>
                </div>
                <button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button>
            </div>`;

        return html;
    }

    function checkQ5Pipeline() {
        const counter = document.getElementById('matchCount');
        const area = document.getElementById('pipeline');
        const resultArea = document.getElementById('resultQ5');
        const testResults = document.getElementById('q5TestResults');
        if (!counter || !area) return;

        if (!localState.pipeline || localState.pipeline.length === 0) {
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
            const actual = applyQ5Pipeline(localState.pipeline, x);
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
            const actual = applyQ5Pipeline(localState.pipeline, x);
            const expected = (x * 3 + 1) % 7;
            if (actual !== expected) allMatch = false;
        });

        let pipeDisplay = localState.pipeline.map((p, i) =>
            `<span style="background: #3844FF; color: white; padding: 6px 10px; border-radius: 4px; display: inline-flex; align-items: center; gap: 6px; font-size: 12px;">
                ${p}
                <button class="q5-remove-block" data-idx="${i}" style="background: rgba(255,255,255,0.3); border: none; color: white; padding: 2px 4px; border-radius: 2px; cursor: pointer; font-weight: 600; font-size: 11px;">×</button>
            </span>`
        ).join(' ');
        area.innerHTML = pipeDisplay;

        const result0 = applyQ5Pipeline(localState.pipeline, 0);
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

    function updateQ5Probes() {
        const log = document.getElementById('probeLog');
        if (!log) return;
        if (!localState.probes || Object.keys(localState.probes).length === 0) {
            log.innerHTML = '[No probes yet]';
            return;
        }
        let html = Object.keys(localState.probes).sort((a,b) => parseInt(a) - parseInt(b)).map(x => `x=${x} → ${localState.probes[x]}`).join('<br>');
        log.innerHTML = html;
    }

    function update() {
        container.innerHTML = renderQ5();
        setTimeout(() => {
            const probeBtn = container.querySelector('.q5-probe-btn');
            const probeInput = container.querySelector('.q5-probe-input');
            if (probeBtn) {
                probeBtn.onclick = () => {
                    const input = parseInt(probeInput.value);
                    probeFunction(input);
                    updateQ5Probes();
                    checkQ5Pipeline();
                };
            }

            container.querySelectorAll('.q5-op-btn').forEach(btn => {
                btn.onclick = () => {
                    localState.pipeline.push(btn.dataset.op);
                    checkQ5Pipeline();
                };
            });

            container.querySelectorAll('.q5-remove-block').forEach(btn => {
                btn.onclick = () => {
                    localState.pipeline.splice(parseInt(btn.dataset.idx), 1);
                    checkQ5Pipeline();
                };
            });

            const submitBtn = container.querySelector('.q5-submit');
            if (submitBtn) {
                submitBtn.onclick = () => {
                    const area = document.getElementById('pipeline');
                    if (area) {
                        area.innerHTML += `<div class="completion show" style="margin-top: 10px; width: 100%; text-align: center;">✓ Pipeline submitted successfully!</div>`;
                    }
                    submitBtn.style.display = 'none';
                };
            }

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { probes: {}, pipeline: [] };
                update();
            };

            updateQ5Probes();
            checkQ5Pipeline();
        }, 0);

        let allMatch = true;
        for (let x = 0; x <= 20; x++) {
            const actual = applyQ5Pipeline(localState.pipeline, x);
            const expected = (x * 3 + 1) % 7;
            if (actual !== expected) { allMatch = false; break; }
        }
        onState(allMatch && localState.pipeline.length > 0);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q6: Number Route (Pathfinding)
window.MECHANICS.numberRoute = function(container, data, onState) {
    let localState = {
        grid: [
            ['+2', '×2', '×2', '×2'],
            ['+1', '+2', '+2', '+2'],
            ['+1', '+2', '+2', '+2'],
            ['+1', '+2', '+2', '+2']
        ],
        current: 3,
        path: [[0,0]],
        target: 48
    };

    function renderQ6() {
        let html = `<div class="question-header"><div class="question-number">Intermediate • Mathematics, Reasoning</div>
            <div class="question-title">Q6: Route</div></div>
            <div class="question-description">Navigate right or down from start to reach the target number.</div>
            <div class="code-block"><code>Start: 3 | Current: ${localState.current} | Goal: ${localState.target}
Only move RIGHT or DOWN!</code></div>
            <div class="interactive-area">
                <div style="display: grid; grid-template-columns: repeat(4, 85px); gap: 10px; margin: 20px 0;">`;

        localState.grid.forEach((row, i) => {
            row.forEach((op, j) => {
                const isPath = localState.path.some(p => p[0] === i && p[1] === j);
                const last = localState.path[localState.path.length-1];
                const canMove = (i === last[0] && j === last[1] + 1) || (j === last[1] && i === last[0] + 1);
                html += `<div class="q6-cell" data-i="${i}" data-j="${j}" style="padding: 12px; background: ${isPath ? '#3844FF' : '#f0f7ff'}; color: ${isPath ? 'white' : '#1d1d1f'}; border-radius: 8px; text-align: center; cursor: ${canMove ? 'pointer' : 'default'}; border: 2px solid ${isPath ? '#3844FF' : '#ddd'}; font-size: 14px; font-weight: 600;">
                    ${op}</div>`;
            });
        });

        html += `</div>`;
        if (localState.current === localState.target && localState.path[localState.path.length-1][0] === 3 && localState.path[localState.path.length-1][1] === 3) {
            html += `<div class="completion show">✓ Reached target!</div>`;
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function moveQ6(i, j) {
        const last = localState.path[localState.path.length - 1];
        if (!((i === last[0] && j === last[1] + 1) || (j === last[1] && i === last[0] + 1))) return;

        const op = localState.grid[i][j];
        if (op[0] === '+') localState.current += parseInt(op.substr(1));
        else if (op[0] === '−') localState.current -= parseInt(op.substr(1));
        else if (op[0] === '×') localState.current *= parseInt(op.substr(1));

        localState.path.push([i, j]);
        update();
    }

    function update() {
        container.innerHTML = renderQ6();
        setTimeout(() => {
            container.querySelectorAll('.q6-cell').forEach(cell => {
                const i = parseInt(cell.dataset.i);
                const j = parseInt(cell.dataset.j);
                const last = localState.path[localState.path.length-1];
                const canMove = (i === last[0] && j === last[1] + 1) || (j === last[1] && i === last[0] + 1);
                if (canMove) cell.onclick = () => moveQ6(i, j);
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = {
                    grid: [
                        ['+2', '×2', '+1', '−1'],
                        ['×3', '+4', '×2', '+5'],
                        ['+1', '−2', '+6', '×2'],
                        ['×2', '+3', '−1', '+4']
                    ],
                    current: 3,
                    path: [[0,0]],
                    target: 48
                };
                update();
            };
        }, 0);

        const isCorrect = localState.current === localState.target && localState.path[localState.path.length-1][0] === 3 && localState.path[localState.path.length-1][1] === 3;
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q7: Sequence Pairs (Dictionary Builder)
window.MECHANICS.sequencePairs = function(container, data, onState) {
    let localState = { pairs: [] };

    function renderQ7() {
        const keys = ['a', 'b', 'c'];
        const d = {};
        localState.pairs.forEach(p => d[p[0]] = p[1]);

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
                            <select class="q7-key-select" style="padding: 6px; border: 1px solid #ddd; border-radius: 4px;">
                                ${keys.map(k => `<option value="${k}">${k}</option>`).join('')}
                            </select>
                            <input type="number" class="q7-val-input" style="padding: 6px; border: 1px solid #ddd; border-radius: 4px; margin: 0 4px; width: 60px;" placeholder="value">
                            <button class="q7-add-btn" style="padding: 6px 12px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Add</button>
                        </div>
                        <div style="margin-top: 15px;">
                            <strong style="font-size: 12px;">Current Dictionary:</strong>
                            <div style="font-family: monospace; background: white; padding: 10px; border: 1px solid #ddd; border-radius: 6px; margin-top: 8px;">
                                ${Object.entries(d).length === 0 ? '{}' : '{' + Object.entries(d).map((e, i) => `<div style="display: flex; justify-content: space-between; align-items: center;"><span>"${e[0]}": ${e[1]}</span><button class="q7-remove-btn" data-key="${e[0]}" style="background: #ff4444; color: white; border: none; padding: 2px 6px; border-radius: 3px; cursor: pointer; font-size: 10px; margin-left: 10px;">Remove</button></div>`).join('') + '}'}
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
        }

        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ7();
        setTimeout(() => {
            const addBtn = container.querySelector('.q7-add-btn');
            if (addBtn) {
                addBtn.onclick = () => {
                    const key = container.querySelector('.q7-key-select').value;
                    const val = parseInt(container.querySelector('.q7-val-input').value);
                    if (isNaN(val)) return;
                    const existing = localState.pairs.findIndex(p => p[0] === key);
                    if (existing >= 0) localState.pairs[existing] = [key, val];
                    else localState.pairs.push([key, val]);
                    container.querySelector('.q7-val-input').value = '';
                    update();
                };
            }

            container.querySelectorAll('.q7-remove-btn').forEach(btn => {
                btn.onclick = () => {
                    const key = btn.dataset.key;
                    localState.pairs = localState.pairs.filter(p => p[0] !== key);
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { pairs: [] };
                update();
            };
        }, 0);

        const d = {};
        localState.pairs.forEach(p => d[p[0]] = p[1]);
        const isCorrect = d['a'] === 2 && d['b'] === undefined && d['c'] === d['a'] + 3 && Object.keys(d).length === 2;
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q8: Line Through Points
window.MECHANICS.lineThroughPts = function(container, data, onState) {
    let localState = { a: 1, b: 0 };

    function drawLine8() {
        const canvas = document.getElementById('q8-canvas');
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
            const y = localState.a * x + localState.b;
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

    function renderQ8() {
        const a = localState.a, b = localState.b;
        const tol = 0.15;
        const p1 = [0, -1], p2 = [2, 3];
        const pass1 = Math.abs(a * p1[0] + b - p1[1]) < tol;
        const pass2 = Math.abs(a * p2[0] + b - p2[1]) < tol;

        let html = `<div class="question-header"><div class="question-number">Introductory • Mathematics</div>
            <div class="question-title">Q8: Line</div></div>
            <div class="question-description">Adjust slope (a) and intercept (b) so the line passes through both target points.</div>
            <div class="code-block"><code>y = a·x + b
Points: (0, -1) and (2, 3)</code></div>
            <div class="interactive-area">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div>
                        <strong>Slope (a):</strong>
                        <div style="display: flex; gap: 10px; margin: 12px 0; align-items: center;">
                            <button class="q8-a-dec" style="padding: 8px 12px; background: #999; color: white; border: none; border-radius: 4px; cursor: pointer;">−</button>
                            <span style="font-weight: 600; font-size: 18px; min-width: 40px; text-align: center;">${a.toFixed(1)}</span>
                            <button class="q8-a-inc" style="padding: 8px 12px; background: #3844FF; color: white; border: none; border-radius: 4px; cursor: pointer;">+</button>
                        </div>
                    </div>
                    <div>
                        <strong>Intercept (b):</strong>
                        <div style="display: flex; gap: 10px; margin: 12px 0; align-items: center;">
                            <button class="q8-b-dec" style="padding: 8px 12px; background: #999; color: white; border: none; border-radius: 4px; cursor: pointer;">−</button>
                            <span style="font-weight: 600; font-size: 18px; min-width: 40px; text-align: center;">${b.toFixed(1)}</span>
                            <button class="q8-b-inc" style="padding: 8px 12px; background: #3844FF; color: white; border: none; border-radius: 4px; cursor: pointer;">+</button>
                        </div>
                    </div>
                </div>
                <canvas id="q8-canvas" width="500" height="400" style="border: 1px solid #ddd; border-radius: 8px; background: white; margin-top: 20px; display: block;"></canvas>
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
        }
        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ8();
        setTimeout(() => {
            const aDec = container.querySelector('.q8-a-dec');
            const aInc = container.querySelector('.q8-a-inc');
            const bDec = container.querySelector('.q8-b-dec');
            const bInc = container.querySelector('.q8-b-inc');
            const resetBtn = container.querySelector('.reset-btn');

            if (aDec) aDec.onclick = () => { localState.a = Math.max(-5, localState.a - 0.5); update(); };
            if (aInc) aInc.onclick = () => { localState.a = Math.min(5, localState.a + 0.5); update(); };
            if (bDec) bDec.onclick = () => { localState.b = Math.max(-5, localState.b - 0.5); update(); };
            if (bInc) bInc.onclick = () => { localState.b = Math.min(5, localState.b + 0.5); update(); };
            if (resetBtn) resetBtn.onclick = () => {
                localState = { a: 1, b: 0 };
                update();
            };
            drawLine8();
        }, 0);

        const tol = 0.15;
        const p1 = [0, -1], p2 = [2, 3];
        const pass1 = Math.abs(localState.a * p1[0] + localState.b - p1[1]) < tol;
        const pass2 = Math.abs(localState.a * p2[0] + localState.b - p2[1]) < tol;
        onState(pass1 && pass2);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q9: Number Bins (Classification)
window.MECHANICS.numberBins = function(container, data, onState) {
    let localState = { placed: {}, selected: null };

    function renderQ9() {
        const numbers = [1, 7, 12, 15, 18, 23, 30, 49, 51, 64];
        const bins = {
            prime: [7, 23],
            div3: [12, 15, 18, 30, 51],
            neither: [1, 49, 64]
        };

        let placed = 0, correct = 0;
        numbers.forEach(n => {
            if (localState.placed[n]) {
                placed++;
                Object.keys(bins).forEach(bName => {
                    if (bins[bName].includes(n) && localState.placed[n] === bName) correct++;
                });
            }
        });

        let html = `<div class="question-header"><div class="question-number">Introductory • Mathematics</div>
            <div class="question-title">Q9: Number Bins</div></div>
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
                            `<button class="q9-num-btn" data-n="${n}" style="padding: 10px 16px; background: ${localState.placed[n] ? '#ddd' : (localState.selected === n ? '#3844FF' : '#fff')}; color: ${localState.placed[n] || localState.selected === n ? 'white' : '#1d1d1f'}; border: 2px solid ${localState.placed[n] ? '#999' : (localState.selected === n ? '#3844FF' : '#ddd')}; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 14px; opacity: ${localState.placed[n] ? '0.6' : '1'}; text-decoration: ${localState.placed[n] ? 'line-through' : 'none'};">${n}</button>`
                        ).join('')}
                    </div>
                    ${localState.selected ? `<div style="margin-top: 15px; padding: 12px; background: #e7f3ff; border-radius: 6px; font-weight: 600;">
                        Selected: ${localState.selected} — Click a bin to place, or click number again to cancel
                    </div>` : ''}
                </div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">
                    ${['prime', 'div3', 'neither'].map(binName => {
                        const binLabel = binName === 'prime' ? 'Prime' : binName === 'div3' ? 'Div by 3' : 'Neither';
                        return `<div class="q9-bin" data-bin="${binName}" style="padding: 15px; background: #f9f9fb; border: 3px dashed ${localState.selected ? '#3844FF' : '#ddd'}; border-radius: 8px; min-height: 150px; cursor: ${localState.selected ? 'pointer' : 'default'};">
                            <strong style="display: block; margin-bottom: 12px;">${binLabel}</strong>
                            <div style="min-height: 100px;">
                                ${numbers.filter(n => localState.placed[n] === binName).map(n => `<div class="q9-placed-num" data-n="${n}" style="background: #3844FF; color: white; padding: 8px; border-radius: 4px; margin: 4px 0; font-weight: 600; cursor: pointer;">${n} ✕</div>`).join('')}
                            </div>
                        </div>`;
                    }).join('')}
                </div>
                <div style="margin-top: 20px; text-align: center; font-weight: 600; padding: 12px; background: #f0f7ff; border-radius: 6px;">
                    Classified: ${placed} / 10 | Correct: ${correct} / 10
                </div>`;

        if (correct === 10) {
            html += `<div class="completion show">✓ All numbers classified correctly!</div>`;
        }

        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ9();
        setTimeout(() => {
            container.querySelectorAll('.q9-num-btn').forEach(btn => {
                btn.onclick = () => {
                    const n = parseInt(btn.dataset.n);
                    if (localState.placed[n]) {
                        delete localState.placed[n];
                    } else {
                        localState.selected = n;
                    }
                    update();
                };
            });

            container.querySelectorAll('.q9-bin').forEach(bin => {
                bin.onclick = () => {
                    if (localState.selected) {
                        localState.placed[localState.selected] = bin.dataset.bin;
                        localState.selected = null;
                        update();
                    }
                };
            });

            container.querySelectorAll('.q9-placed-num').forEach(num => {
                num.onclick = () => {
                    const n = parseInt(num.dataset.n);
                    delete localState.placed[n];
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { placed: {}, selected: null };
                update();
            };
        }, 0);

        const numbers = [1, 7, 12, 15, 18, 23, 30, 49, 51, 64];
        const bins = {
            prime: [7, 23],
            div3: [12, 15, 18, 30, 51],
            neither: [1, 49, 64]
        };
        let correct = 0;
        numbers.forEach(n => {
            if (localState.placed[n]) {
                Object.keys(bins).forEach(bName => {
                    if (bins[bName].includes(n) && localState.placed[n] === bName) correct++;
                });
            }
        });
        onState(correct === 10);
    }

    update();
    return () => { container.innerHTML = ''; };
};

// Q10: List Transform
window.MECHANICS.listTransform = function(container, data, onState) {
    let localState = { chain: [] };

    function renderQ10() {
        const start = [1, 2, 3, 4, 5];
        const target = [8, 6, 4];
        const cards = ['×2', '+1', 'remove odd', 'reverse', 'pop', 'keep first 3'];

        let current = [...start];
        localState.chain.forEach(op => {
            if (op === '×2') current = current.map(x => x * 2);
            else if (op === '+1') current = current.map(x => x + 1);
            else if (op === 'remove odd') current = current.filter(x => x % 2 === 0);
            else if (op === 'reverse') current = current.reverse();
            else if (op === 'pop') current.pop();
            else if (op === 'keep first 3') current = current.slice(0, 3);
        });

        const isCorrect = JSON.stringify(current) === JSON.stringify(target);

        let html = `<div class="question-header"><div class="question-number">Intermediate • Programming</div>
            <div class="question-title">Q10: List Transform</div></div>
            <div class="question-description">Build a chain of operations to transform the start list into the target.</div>
            <div class="code-block"><code>Start:  ${JSON.stringify(start)}
Target: ${JSON.stringify(target)}
Chain operations to reach target!</code></div>
            <div class="interactive-area">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div>
                        <strong>Available Operations:</strong>
                        <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 10px;">
                            ${cards.map(card => `<button class="q10-op-btn" data-op="${card}" style="padding: 10px; font-size: 12px; background: #3844FF; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">${card}</button>`).join('')}
                        </div>
                    </div>
                    <div>
                        <strong>Chain:</strong>
                        <div style="background: white; padding: 12px; border: 1px solid #ddd; border-radius: 6px; min-height: 150px; font-family: monospace; font-size: 12px;">
                            ${localState.chain.length === 0 ? '[empty]' : localState.chain.map((op, i) => `<div style="padding: 6px; background: #e7f3ff; border-radius: 4px; margin: 4px 0;">
                                ${i + 1}. ${op} <button class="q10-remove-op" data-idx="${i}" style="float: right; background: #ff4444; color: white; border: none; padding: 2px 6px; border-radius: 3px; cursor: pointer; font-size: 10px;">×</button>
                            </div>`).join('')}
                        </div>
                        <div style="margin-top: 10px; padding: 10px; background: #f0f7ff; border-radius: 6px; font-family: monospace;">
                            Result: ${JSON.stringify(current)}
                        </div>
                    </div>
                </div>`;

        if (isCorrect) {
            html += `<div class="completion show">✓ List transformed correctly!</div>`;
        }

        html += `<button class="reset-btn" style="margin-top: 15px; padding: 8px 16px; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px;">↻ Reset</button></div>`;
        return html;
    }

    function update() {
        container.innerHTML = renderQ10();
        setTimeout(() => {
            container.querySelectorAll('.q10-op-btn').forEach(btn => {
                btn.onclick = () => {
                    localState.chain.push(btn.dataset.op);
                    update();
                };
            });

            container.querySelectorAll('.q10-remove-op').forEach(btn => {
                btn.onclick = () => {
                    localState.chain.splice(parseInt(btn.dataset.idx), 1);
                    update();
                };
            });

            const resetBtn = container.querySelector('.reset-btn');
            if (resetBtn) resetBtn.onclick = () => {
                localState = { chain: [] };
                update();
            };
        }, 0);

        const start = [1, 2, 3, 4, 5];
        const target = [8, 6, 4];
        let current = [...start];
        localState.chain.forEach(op => {
            if (op === '×2') current = current.map(x => x * 2);
            else if (op === '+1') current = current.map(x => x + 1);
            else if (op === 'remove odd') current = current.filter(x => x % 2 === 0);
            else if (op === 'reverse') current = current.reverse();
            else if (op === 'pop') current.pop();
            else if (op === 'keep first 3') current = current.slice(0, 3);
        });
        const isCorrect = JSON.stringify(current) === JSON.stringify(target);
        onState(isCorrect);
    }

    update();
    return () => { container.innerHTML = ''; };
};

console.log('✓ mechanics.js loaded with ' + Object.keys(window.MECHANICS).length + ' mechanics');
