const canvas = document.getElementById("c");
const ctx = canvas.getContext("2d");
const w = canvas.width, h = canvas.height;
const size = w * h;

let u = new Float32Array(size);
let v = new Float32Array(size);
let u2 = new Float32Array(size);
let v2 = new Float32Array(size);

const Du = 0.16, Dv = 0.08;
let F = 0.030, k = 0.062;

function idx(x, y) {
    return ((y + h) % h) * w + ((x + w) % w);
}

function seed() {
    u.fill(1);
    v.fill(0);
    for (let n = 0; n < 40; n++) {
        const cx = (Math.random() * (w - 20) + 10) | 0;
        const cy = (Math.random() * (h - 20) + 10) | 0;
        for (let dy = -4; dy <= 4; dy++) {
            for (let dx = -4; dx <= 4; dx++) {
                const i = idx(cx + dx, cy + dy);
                u[i] = 0.5 + (Math.random() - 0.5) * 0.1;
                v[i] = 0.25 + (Math.random() - 0.5) * 0.05;
            }
        }
    }
}

function lap(arr, x, y) {
    return (
        -arr[idx(x, y)] +
        0.2  * (arr[idx(x-1, y)] + arr[idx(x+1, y)] + arr[idx(x, y-1)] + arr[idx(x, y+1)]) +
        0.05 * (arr[idx(x-1, y-1)] + arr[idx(x+1, y-1)] + arr[idx(x-1, y+1)] + arr[idx(x+1, y+1)])
    );
}

function step() {
    for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
            const i = idx(x, y);
            const uvv = u[i] * v[i] * v[i];
            u2[i] = u[i] + Du * lap(u, x, y) - uvv + F * (1 - u[i]);
            v2[i] = v[i] + Dv * lap(v, x, y) + uvv - (F + k) * v[i];
        }
    }
    [u, u2] = [u2, u];
    [v, v2] = [v2, v];
}

function draw() {
    const img = ctx.createImageData(w, h);
    for (let i = 0; i < size; i++) {
        const c = Math.floor(v[i] * 255 * 4);
        img.data[i * 4 + 0] = c;
        img.data[i * 4 + 1] = c;
        img.data[i * 4 + 2] = c;
        img.data[i * 4 + 3] = 255;
    }
    ctx.putImageData(img, 0, 0);
}

function reset(newF, newK) {
    F = newF;
    k = newK;
    seed();
}

function animate() {
    for (let i = 0; i < 10; i++) step();
    draw();
    requestAnimationFrame(animate);
}

seed();
animate();
