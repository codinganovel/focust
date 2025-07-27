#!/usr/bin/env python3
"""
focust - Matrix-Themed Timer
"""

import os
import sys
import time
import random
import argparse
import threading

# Matrix characters
KATAKANA_CHARS = [
    'ｱ', 'ｲ', 'ｳ', 'ｴ', 'ｵ', 'ｶ', 'ｷ', 'ｸ', 'ｹ', 'ｺ', 'ｻ', 'ｼ', 'ｽ', 'ｾ', 'ｿ',
    'ﾀ', 'ﾁ', 'ﾂ', 'ﾃ', 'ﾄ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ', 'ﾉ', 'ﾊ', 'ﾋ', 'ﾌ', 'ﾍ', 'ﾎ', 'ﾏ',
    'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'ﾔ', 'ﾕ', 'ﾖ', 'ﾗ', 'ﾘ', 'ﾙ', 'ﾚ', 'ﾛ', 'ﾜ', 'ﾝ'
]

# Colors
GREEN = '\033[92m'
WHITE = '\033[97m'
GRAY = '\033[90m'
BOLD = '\033[1m'
RESET = '\033[0m'

class MatrixTimer:
    def __init__(self, focus_minutes=30, break_minutes=5):
        self.focus_minutes = focus_minutes
        self.break_minutes = break_minutes
        self.time_remaining = focus_minutes * 60
        self.is_focus = True
        self.running = True
        self.terminal_width = 60
        self.terminal_height = 20
        self.last_key = None
    
    def get_terminal_size(self):
        try:
            size = os.get_terminal_size()
            self.terminal_width = size.columns
            self.terminal_height = size.lines
        except:
            self.terminal_width = 60
            self.terminal_height = 20
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def render_screen(self):
        """Render animated Matrix screen"""
        self.clear_screen()
        self.get_terminal_size()
        
        # Fill entire terminal with random Matrix characters (animated!)
        for row in range(self.terminal_height):
            line = ''.join(random.choice(KATAKANA_CHARS) for _ in range(self.terminal_width))
            print(f"{GREEN}{line}{RESET}")
        
        # Timer info
        if self.is_focus:
            emoji = "🔴"
            mode_text = "FOCUS PROTOCOL"
        else:
            emoji = "🔵"
            mode_text = "BREAK PROTOCOL"
        
        time_str = self.format_time(self.time_remaining)
        
        # Center position
        center_row = self.terminal_height // 2
        center_col = self.terminal_width // 2
        
        # Overlay timer info using ANSI positioning
        print(f"\033[{center_row-2};{center_col-10}H{WHITE}{BOLD}{emoji} {mode_text}{RESET}")
        print(f"\033[{center_row};{center_col-5}H{WHITE}{BOLD}{time_str}{RESET}")
        print(f"\033[{center_row+1};{center_col-5}H{WHITE}REMAINING{RESET}")
        
        # Controls at bottom
        controls = "s:skip  q:quit"
        print(f"\033[{self.terminal_height};1H{GRAY}{controls}{RESET}")
        
        # Force output immediately
        sys.stdout.flush()
    
    def input_thread(self):
        """Handle keyboard input in separate thread"""
        while self.running:
            try:
                key = input().strip().lower()
                self.last_key = key
            except:
                break
    
    def check_input(self):
        """Check for recent key presses"""
        if self.last_key:
            key = self.last_key
            self.last_key = None  # Clear it
            
            if key == 'q':
                return False
            elif key == 's':
                # Skip current timer
                if self.is_focus:
                    # Skip to break
                    self.is_focus = False
                    self.time_remaining = self.break_minutes * 60
                else:
                    # Skip break, finish timer
                    return False
        
        return True
    
    def run(self):
        print(f"{GREEN}🔴 Matrix Protocol Initiating...{RESET}")
        print(f"{GRAY}Type 's' + Enter to skip, 'q' + Enter to quit{RESET}")
        time.sleep(2)
        
        # Start input thread
        input_thread = threading.Thread(target=self.input_thread, daemon=True)
        input_thread.start()
        
        while self.running:
            self.render_screen()
            
            # Check for input
            if not self.check_input():
                break
            
            # Update timer
            self.time_remaining -= 1
            
            if self.time_remaining <= 0:
                if self.is_focus:
                    # Switch to break
                    self.is_focus = False
                    self.time_remaining = self.break_minutes * 60
                    self.clear_screen()
                    print(f"\n{GREEN}🔵 Break time! Press Enter to continue...{RESET}")
                    input()  # Wait for user acknowledgment
                else:
                    # Timer complete
                    self.clear_screen()
                    print(f"\n{GREEN}🎊 Timer complete! Welcome back to reality, Neo.{RESET}")
                    break
            
            time.sleep(1)
        
        self.running = False

def main():
    parser = argparse.ArgumentParser(description='focust - Matrix-themed timer')
    parser.add_argument('--focus', type=int, default=30, help='Focus minutes (default: 30)')
    parser.add_argument('--break', type=int, default=5, help='Break minutes (default: 5)')
    
    args = parser.parse_args()
    
    try:
        timer = MatrixTimer(args.focus, getattr(args, 'break'))
        timer.run()
    except KeyboardInterrupt:
        print(f"\n{GREEN}👋 Disconnecting from the Matrix...{RESET}")

if __name__ == "__main__":
    main()