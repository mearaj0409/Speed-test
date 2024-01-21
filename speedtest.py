import tkinter as tk
import random
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("400x200")

        self.text_to_type = "Computer science"
        self.current_index = 0
        self.start_time = None

        self.label_instruction = tk.Label(root, text="Type the following:")
        self.label_instruction.pack(pady=5)

        self.label_text_to_type = tk.Label(root, text=self.text_to_type)
        self.label_text_to_type.pack(pady=10)

        self.entry_typing = tk.Entry(root, font=("Arial", 14))
        self.entry_typing.pack(pady=10)

        self.button_start = tk.Button(root, text="Start Typing Test", command=self.start_typing_test)
        self.button_start.pack(pady=10)

    def start_typing_test(self):
        self.current_index = 0
        self.start_time = time.time()
        self.label_instruction.config(text="Type the following:")

        # Disable the Start button
        self.button_start.config(state=tk.DISABLED)

        # Clear the entry field
        self.entry_typing.delete(0, tk.END)

        # Bind the entry to the on_typing function
        self.entry_typing.bind("<Key>", self.on_typing)

    def on_typing(self, event):
        typed_char = event.char
        if typed_char == self.text_to_type[self.current_index]:
            self.current_index += 1
            self.entry_typing.delete(0, tk.END)

            if self.current_index == len(self.text_to_type):
                self.end_typing_test()
        else:
            self.label_instruction.config(text="Incorrect! Keep typing.")

    def end_typing_test(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        words_per_minute = int((len(self.text_to_type) / 5) / (elapsed_time / 60))

        result_text = f"Typing test completed!\nWords per minute: {words_per_minute}"
        self.label_instruction.config(text=result_text)

        # Re-enable the Start button
        self.button_start.config(state=tk.NORMAL)

        # Unbind the entry field
        self.entry_typing.unbind("<Key>")

if __name__ == "__main__":
    root = tk.Tk()
    typing_speed_test = TypingSpeedTest(root)
    root.mainloop()
