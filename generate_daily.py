"""Daily project generator — creates a small creative program, commits, and pushes."""
import random, datetime, os, subprocess, math, textwrap

REPO = r"C:\Users\zatch\github\daily-projects"
today = datetime.date.today().strftime("%Y-%m-%d")
folder = os.path.join(REPO, today)
os.makedirs(folder, exist_ok=True)

# ---------------------------------------------------------------------------
# Mini-program generators — each returns (filename, content, commit_msg)
# ---------------------------------------------------------------------------

def ascii_clock():
    h = random.randint(1, 12)
    m = random.randint(0, 59)
    art = textwrap.dedent(f"""\
    # ASCII Clock — frozen at {h}:{m:02d}
    import math
    def draw():
        grid = [[' ']*41 for _ in range(21)]
        cx, cy = 20, 10
        for a in range(360):
            r = 9.5
            x = int(cx + r * math.cos(math.radians(a)))
            y = int(cy + r/2 * math.sin(math.radians(a)))
            if 0 <= x < 41 and 0 <= y < 21:
                grid[y][x] = '.'
        # hour hand
        ha = math.radians((({h} % 12) + {m}/60) * 30 - 90)
        for i in range(1, 6):
            x = int(cx + i * math.cos(ha))
            y = int(cy + i/2 * math.sin(ha))
            if 0 <= x < 41 and 0 <= y < 21:
                grid[y][x] = '#'
        # minute hand
        ma = math.radians({m} * 6 - 90)
        for i in range(1, 9):
            x = int(cx + i * math.cos(ma))
            y = int(cy + i/2 * math.sin(ma))
            if 0 <= x < 41 and 0 <= y < 21:
                grid[y][x] = '*'
        grid[cy][cx] = 'O'
        for row in grid:
            print(''.join(row))
        print(f"    {{:>2}}:{{:02d}}".format({h}, {m}))
    if __name__ == "__main__":
        draw()
    """)
    return "ascii_clock.py", art, f"ASCII clock frozen at {h}:{m:02d}"


def mandelbrot():
    w, h = random.choice([(80,30),(60,24),(100,35)])
    return "mandelbrot.py", textwrap.dedent(f"""\
    # Mandelbrot set — {w}x{h}
    W, H = {w}, {h}
    chars = " .:-=+*#%@"
    for row in range(H):
        line = ""
        for col in range(W):
            c = complex(-2.5 + col * 3.5/W, -1.25 + row * 2.5/H)
            z, n = 0j, 0
            while abs(z) < 2 and n < len(chars)-1:
                z = z*z + c
                n += 1
            line += chars[n]
        print(line)
    """), f"Mandelbrot set renderer {w}x{h}"


def maze_generator():
    size = random.choice([10, 15, 20])
    return "maze.py", textwrap.dedent(f"""\
    # Random maze generator — {size}x{size} using recursive backtracking
    import random
    N, S, E, W = 1, 2, 4, 8
    DX = {{E: 1, W: -1, N: 0, S: 0}}
    DY = {{E: 0, W: 0, N: -1, S: 1}}
    OPP = {{E: W, W: E, N: S, S: N}}
    sz = {size}
    grid = [[0]*sz for _ in range(sz)]
    def carve(cx, cy):
        dirs = [N, S, E, W]
        random.shuffle(dirs)
        for d in dirs:
            nx, ny = cx + DX[d], cy + DY[d]
            if 0 <= nx < sz and 0 <= ny < sz and grid[ny][nx] == 0:
                grid[cy][cx] |= d
                grid[ny][nx] |= OPP[d]
                carve(nx, ny)
    import sys; sys.setrecursionlimit(10000)
    carve(0, 0)
    top = "+" + "+".join("---" if not (grid[0][x] & N) else "   " for x in range(sz)) + "+"
    print(top)
    for y in range(sz):
        row = "|" if not (grid[y][0] & W) else " "
        for x in range(sz):
            row += "   "
            row += " " if (grid[y][x] & E) else "|"
        print(row)
        bot = "+"
        for x in range(sz):
            bot += "   " if (grid[y][x] & S) else "---"
            bot += "+"
        print(bot)
    """), f"Maze generator {size}x{size}"


def game_of_life():
    w, h = 40, 20
    density = random.randint(20, 45)
    gens = random.choice([30, 50, 80])
    return "game_of_life.py", textwrap.dedent(f"""\
    # Conway's Game of Life — {w}x{h}, {density}% density, {gens} generations
    import random, time, os
    W, H, GENS = {w}, {h}, {gens}
    grid = [[random.random() < {density/100:.2f} for _ in range(W)] for _ in range(H)]
    def step(g):
        new = [[False]*W for _ in range(H)]
        for y in range(H):
            for x in range(W):
                n = sum(g[(y+dy)%H][(x+dx)%W] for dy in (-1,0,1) for dx in (-1,0,1) if (dy,dx)!=(0,0))
                new[y][x] = n == 3 or (g[y][x] and n == 2)
        return new
    for gen in range(GENS):
        os.system('cls' if os.name=='nt' else 'clear')
        print(f"Generation {{gen+1}}/{gens}")
        for row in grid:
            print(''.join('█' if c else ' ' for c in row))
        grid = step(grid)
        time.sleep(0.1)
    """), f"Game of Life {density}% density"


def sorting_visualizer():
    algo = random.choice(["bubble", "insertion", "selection"])
    n = random.randint(15, 30)
    return "sort_viz.py", textwrap.dedent(f"""\
    # {algo.title()} sort visualizer — {n} elements
    import random, time, os
    arr = random.sample(range(1, {n+1}), {n})
    def show(arr, hi=[]):
        os.system('cls' if os.name=='nt' else 'clear')
        mx = max(arr)
        for level in range(mx, 0, -1):
            row = ""
            for i, v in enumerate(arr):
                if v >= level:
                    row += "██" if i in hi else "░░"
                else:
                    row += "  "
            print(row)
        print("".join(f"{{v:>2}}" for v in arr))
        time.sleep(0.05)
    """) + (
    {"bubble": textwrap.dedent(f"""\
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            show(arr, [j, j+1])
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    show(arr)
    print("Sorted!")
    """),
    "insertion": textwrap.dedent(f"""\
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            show(arr, [j, j+1])
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    show(arr)
    print("Sorted!")
    """),
    "selection": textwrap.dedent(f"""\
    for i in range(len(arr)):
        mn = i
        for j in range(i+1, len(arr)):
            show(arr, [mn, j])
            if arr[j] < arr[mn]:
                mn = j
        arr[i], arr[mn] = arr[mn], arr[i]
    show(arr)
    print("Sorted!")
    """)}[algo]), f"{algo.title()} sort visualizer with {n} elements"


def spiral_art():
    size = random.choice([21, 31, 41])
    chars = random.choice(["@#*+.", "█▓▒░ ", "●○◐◑ "])
    return "spiral.py", textwrap.dedent(f"""\
    # Spiral pattern — {size}x{size}
    import math
    size = {size}
    grid = [[' ']*size for _ in range(size)]
    cx, cy = size//2, size//2
    chars = "{chars}"
    for i in range(size * size):
        angle = i * 0.15
        r = i * 0.04
        x = int(cx + r * math.cos(angle))
        y = int(cy + r * math.sin(angle))
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = chars[i % len(chars)]
    for row in grid:
        print(''.join(row))
    """), f"Spiral art {size}x{size}"


def password_gen():
    length = random.choice([12, 16, 20, 24])
    return "password_gen.py", textwrap.dedent(f"""\
    # Secure password generator — {length} chars
    import secrets, string
    def generate(length={length}, count=5):
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        for i in range(count):
            pw = ''.join(secrets.choice(alphabet) for _ in range(length))
            strength = len(set(pw)) / length
            bar = '█' * int(strength * 20) + '░' * (20 - int(strength * 20))
            print(f"  {{i+1}}. {{pw}}  [{{bar}}] {{strength:.0%}} unique")
    if __name__ == "__main__":
        print(f"Generating 5 passwords ({{length}} chars each):\\n")
        generate()
    """), f"Password generator ({length} chars)"


def wave_animation():
    frames = random.choice([40, 60, 80])
    w = random.choice([60, 80])
    return "wave.py", textwrap.dedent(f"""\
    # Terminal wave animation — {frames} frames
    import math, time, os
    W, FRAMES = {w}, {frames}
    for f in range(FRAMES):
        os.system('cls' if os.name=='nt' else 'clear')
        for y in range(16):
            row = ""
            for x in range(W):
                v = math.sin(x*0.1 + f*0.2) + math.sin(y*0.2 + f*0.15)
                row += "░▒▓█"[int((v+2)/4 * 3.99)]
            print(row)
        time.sleep(0.05)
    """), f"Terminal wave animation"


def diamond_pattern():
    n = random.choice([5, 7, 9, 11])
    ch = random.choice(["*", "#", "♦", "◆"])
    return "diamond.py", textwrap.dedent(f"""\
    # Diamond pattern generator — size {n}
    n = {n}
    ch = "{ch}"
    for i in range(n):
        spaces = abs(n//2 - i)
        stars = n - 2 * spaces
        print(' ' * spaces + (ch + ' ') * stars)
    print()
    # Hollow variant
    for i in range(n):
        spaces = abs(n//2 - i)
        stars = n - 2 * spaces
        if stars <= 1:
            print(' ' * spaces + ch)
        else:
            print(' ' * spaces + ch + ' ' * (2*stars - 3) + ch)
    """), f"Diamond patterns size {n}"


def number_spiral():
    n = random.choice([5, 7, 9])
    return "number_spiral.py", textwrap.dedent(f"""\
    # Number spiral — {n}x{n}
    n = {n}
    grid = [[0]*n for _ in range(n)]
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    x = y = d = 0
    for i in range(1, n*n+1):
        grid[x][y] = i
        nx, ny = x+dx[d], y+dy[d]
        if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
            x, y = nx, ny
        else:
            d = (d+1) % 4
            x, y = x+dx[d], y+dy[d]
    w = len(str(n*n))
    for row in grid:
        print(' '.join(f'{{v:>{w}}}' for v in row))
    """), f"Number spiral {n}x{n}"


# ---------------------------------------------------------------------------

generators = [
    ascii_clock, mandelbrot, maze_generator, game_of_life,
    sorting_visualizer, spiral_art, password_gen, wave_animation,
    diamond_pattern, number_spiral,
]

pick = random.choice(generators)
filename, content, msg = pick()
filepath = os.path.join(folder, filename)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

# Git commit & push
os.chdir(REPO)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", f"{today}: {msg}"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)
print(f"Pushed: {today}/{filename} — {msg}")
