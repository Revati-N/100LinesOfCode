import time
import sys
import os

WORK_MINS   = 25
SHORT_BREAK = 5
LONG_BREAK  = 15
CYCLES_BEFORE_LONG = 4

def beep(times=3):
    for _ in range(times):
        print("\a", end="", flush=True)
        time.sleep(0.3)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def format_time(seconds):
    m, s = divmod(seconds, 60)
    return f"{m:02d}:{s:02d}"

def countdown(label, duration_mins, cycle_info=""):
    total = duration_mins * 60
    bar_width = 30

    for remaining in range(total, -1, -1):
        elapsed = total - remaining
        filled  = int(bar_width * elapsed / total)
        bar     = "█" * filled + "░" * (bar_width - filled)
        pct     = int(100 * elapsed / total)

        clear()
        print("╔══════════════════════════════════════╗")
        print("║        🍅  POMODORO TIMER  🍅         ║")
        print("╚══════════════════════════════════════╝")
        print(f"\n  Phase  : {label}")
        if cycle_info:
            print(f"  Cycle  : {cycle_info}")
        print(f"\n  Time   : {format_time(remaining)}")
        print(f"\n  [{bar}] {pct}%\n")
        print("  Press Ctrl+C to quit.\n")

        if remaining > 0:
            time.sleep(1)

    beep(3)

def run():
    cycle = 0
    print("\n  Welcome to Pomodoro Timer!")
    print(f"  Work: {WORK_MINS}m  |  Short break: {SHORT_BREAK}m  |  Long break: {LONG_BREAK}m\n")
    input("  Press Enter to start your first session...")

    while True:
        cycle += 1
        info = f"{cycle} / {CYCLES_BEFORE_LONG}"
        countdown("🔴  FOCUS — Work Session", WORK_MINS, info)
        print("\n  ✅  Work session complete!\n")

        
        if cycle % CYCLES_BEFORE_LONG == 0:
            print(f"  🎉  {CYCLES_BEFORE_LONG} cycles done! Time for a long break.\n")
            input("  Press Enter to start your long break...")
            countdown("🟢  LONG BREAK", LONG_BREAK)
        else:
            input("  Press Enter to start your short break...")
            countdown("🟡  SHORT BREAK", SHORT_BREAK)

        print("\n  Break over! Ready for the next session?\n")
        input("  Press Enter to continue...\n")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\n  👋  Session ended. Great work!\n")
        sys.exit(0)