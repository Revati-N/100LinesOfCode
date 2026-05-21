# 🍅 Pomodoro Timer

A terminal-based Pomodoro Timer that helps you stay focused using the [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique).

## 📸 Preview

```
╔══════════════════════════════════════╗
║        🍅  POMODORO TIMER  🍅         ║
╚══════════════════════════════════════╝

  Phase  : 🔴  FOCUS — Work Session
  Cycle  : 1 / 4

  Time   : 24:13

  [████████████░░░░░░░░░░░░░░░░░░] 40%

  Press Ctrl+C to quit.
```

## ⏱️ How It Works

The Pomodoro Technique breaks work into focused intervals:

| Phase        | Duration  |
|--------------|-----------|
| Work session | 25 minutes |
| Short break  | 5 minutes  |
| Long break   | 15 minutes (after every 4 cycles) |

## 🚀 Installation

No external libraries required — uses only Python's standard library.

```bash
git clone https://github.com/YOUR_USERNAME/100LinesOfCode.git
cd 100LinesOfCode/Pomodoro-Timer
```

## ▶️ Usage

```bash
python pomodoro.py
```

- Press **Enter** to start/continue each phase
- Press **Ctrl+C** at any time to quit

## ⚙️ Customization

Edit the config at the top of `pomodoro.py`:

```python
WORK_MINS            = 25   # Work session length
SHORT_BREAK          = 5    # Short break length
LONG_BREAK           = 15   # Long break length
CYCLES_BEFORE_LONG   = 4    # Cycles before a long break
```

## 🛠️ Technologies

- Python 3.x
- Standard library only (`time`, `sys`, `os`)

## 📏 Lines of Code

**81 lines** (excluding comments and blank lines)