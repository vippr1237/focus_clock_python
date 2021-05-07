import tkinter as tk
from playsound import playsound

class Countdown(tk.Frame):
    '''A Frame with label to show the time left, an entry
       to input the seconds to count down from, and a
       start button to start counting down.'''
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.min_left = 0
        self._timer_on = False

    def show_widgets(self):

        self.label.pack()
        self.entry.pack()
        self.start.pack()

    def create_widgets(self):

        self.label = tk.Label(self, text="00:40:00", font=("Courier", 50))
        self.entry = tk.Entry(self, justify='center')
        self.entry.focus_set()
        self.entry.insert(0, 40)
        self.start = tk.Button(self, text="Start",
                               command=self.start_button)

    def countdown(self):
        '''Update label based on the time left.'''
        self.label['text'] = self.convert_seconds_left_to_time()

        if self.min_left:
            self.min_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False
            playsound("C:/Users/HP/Music/za_warudo.mp3")

    def start_button(self):
        '''Start counting down.'''
        # 1. to fetch the seconds
        self.min_left = int(self.entry.get())*60
        # 2. to prevent having multiple
        self.stop_timer()
        #    timers at once
        self.countdown()

    def stop_timer(self):
        '''Stops after schedule from executing.'''
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):
        m, s = divmod(self.min_left, 60)
        h, m = divmod(m, 60)
        return str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("400x150")

    countdown = Countdown(root)
    countdown.pack()

    root.mainloop()