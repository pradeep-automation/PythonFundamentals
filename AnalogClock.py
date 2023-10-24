import tkinter as tk
import time
import math

def update_time():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Calculate angles for clock hands
    second_angle = math.radians((second - 15) * 6)
    minute_angle = math.radians((minute - 15) * 6 + (second / 10))
    hour_angle = math.radians((hour - 3) * 30 + (minute / 2))

    # Clear previous clock hands
    canvas.delete("clock_hand")

    # Draw clock hands
    draw_hand(100, second_angle, "red")
    draw_hand(80, minute_angle, "blue")
    draw_hand(50, hour_angle, "green")

    root.after(1000, update_time)  # Update every 1000ms (1 second)

def draw_hand(length, angle, color):
    x = 150 + length * math.cos(angle)
    y = 150 + length * math.sin(angle)
    canvas.create_line(150, 150, x, y, width=2, fill=color, tag="clock_hand")

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

clock_face = canvas.create_oval(50, 50, 250, 250, width=2)

update_time()  # Start the clock update loop

root.mainloop()
