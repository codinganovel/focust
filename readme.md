# focust
**focust** is a Matrix-themed Pomodoro timer for your terminal. It transforms your entire screen into animated digital rain while keeping you focused on your work sessions. Experience the aesthetic of falling katakana characters as your timer counts down.

> Free your mind. Focus your time.

---

## ✨ Features
- Animated Matrix digital rain fills your entire terminal  
- Simple focus → break → done timer cycle  
- Customizable focus and break durations  
- Clean terminal takeover with floating timer display  
- Minimal keyboard controls for distraction-free sessions  

---

## 📦 Installation

[get yanked](https://github.com/codinganovel/yanked)

---

## 🎯 Usage

### Basic Usage
```bash
focust                    # Default: 30min focus, 5min break
focust --focus 25         # 25min focus sessions
focust --break 10         # 10min break sessions
focust --focus 45 --break 15  # Custom focus and break times
```

### Available Commands During Timer

| Command    | Description                          |
|------------|--------------------------------------|
| `s` + Enter | Skip current timer (focus or break) |
| `q` + Enter | Quit the application                |

### CLI Arguments

| Argument       | Description                          |
|----------------|--------------------------------------|
| `--focus N`    | Set focus session length in minutes (default: 30) |
| `--break N`    | Set break length in minutes (default: 5) |

---

## 🖥️ Interface

**Focus Session:**
- Entire terminal fills with animated katakana characters (ｱｲｳｴｵｶｷｸ...)
- 🔴 FOCUS PROTOCOL indicator with countdown timer floats in center
- Matrix characters continuously shift and change

**Break Session:**  
- Same Matrix aesthetic with 🔵 BREAK PROTOCOL indicator
- Seamless transition between focus and break

---

## 🔧 Dependencies

**Required:**
- Python 3.6+
- Standard library only (no external dependencies)

**Cross-platform Support:**
- ✅ macOS - Full support  
- ✅ Linux - Full support  
- ✅ Windows - Full support

All platforms use simple "type and press Enter" keyboard input for reliable operation.

**Terminal Requirements:**
- ANSI color support (most modern terminals)
- Unicode support for katakana characters

---

## 🎨 Design Philosophy

focust follows the principle that productivity tools should be:
- **Distraction-free** - No complex interfaces or settings to fidget with
- **Aesthetically pleasing** - The Matrix theme makes focus sessions feel immersive
- **Minimal** - Just enough features to be useful, nothing more

The animated Matrix effect serves both form and function - it's visually engaging while providing clear visual feedback that the timer is active and running.

---

## 📄 License

under ☕️, check out [the-coffee-license](https://github.com/codinganovel/The-Coffee-License)

I've included both licenses with the repo, do what you know is right. The licensing works by assuming you're operating under good faith.
---

## ✍️ Created by Sam  
Welcome to the Matrix. Your productivity journey begins now.