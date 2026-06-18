# ⌨️ Typing Speed Tester CLI

A terminal-based typing speed tester that measures your WPM and accuracy — no browser, no setup, just Python.

## Features

- Randomly selects a sentence each round
- Measures **WPM** (words per minute) and **accuracy** (per word)
- Color-coded feedback — green for correct words, red for mistyped ones
- Session summary with averages and best score after multiple rounds

## Demo

```
⌨  Typing Speed Tester

Type the sentence below as fast and accurately as you can.

───────────────────────────────────────────────────────
coding is the closest thing we have to a superpower
───────────────────────────────────────────────────────

> coding is the closest thing we have to a superpower

  WPM      : 72
  Accuracy : 100% (9/9 words correct)
  Time     : 7.48s
```

## Requirements

Python 3.x — no external libraries needed.

## Usage

```bash
python typing_speed_tester.py
```

Type the displayed sentence and press Enter. Type `quit` to end the session.

## How It Works

- Timer starts when you press Enter to begin
- Each word in your input is compared against the original
- WPM is calculated as `(word_count / elapsed_seconds) * 60`
- Accuracy is `correct_words / total_words * 100`