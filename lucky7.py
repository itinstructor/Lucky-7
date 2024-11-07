import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from random import randint


class Lucky7App:
    def __init__(self):
        ctk.set_appearance_mode("dark") # "light" or "dark"
        # Themes: "blue" (standard), "green", "dark-blue", "dark-green", "dark-red", "dark-purple"
        ctk.set_default_color_theme("dark-blue")
        self.root = ctk.CTk()
        self.root.title("Lucky 7")
        self.root.geometry("285x400")
        self.root.iconbitmap("slot_machine.ico")
        self.root.resizable(False, False)

        # Call method to create all the widgets
        self.load_images()
        self.create_widgets()

        # Start GUI
        self.root.mainloop()

# ------------------------ LOAD IMAGES ----------------------------------- #
    def load_images(self):
        # Create a dictionary to store the image file names and
        # associated Tkinter image objects
        self.num_images = {}

        # Load the images
        for i in range(1, 10):
            # Load the images from file
            img = Image.open(f"./assets/{i}.png")
            # Convert the images to CustomTkinter format, store in dictionary
            self.num_images[i] = ctk.CTkImage(img, size=(65, 65))

        img = Image.open("./assets/button.png")
        self.spin_img = ctk.CTkImage(img, size=(117, 50))

# ----------------------------- SPIN --------------------------------------#
    def spin(self, *args):
        # Spin 3 random numbers from 1-9
        spin_1 = randint(1, 9)
        spin_2 = randint(1, 9)
        spin_3 = randint(1, 9)

        # Update the images with random numbers from the dictionary
        self.lbl_1.configure(image=self.num_images.get(spin_1))
        self.lbl_2.configure(image=self.num_images.get(spin_2))
        self.lbl_3.configure(image=self.num_images.get(spin_3))

        if spin_1 == 7 and spin_2 == 7 and spin_3 == 7:
            self.lbl_score.configure(text="3-7's - $300")
        elif spin_1 == 7 or spin_2 == 7 or spin_3 == 7:
            self.lbl_score.configure(text="1-7 - $20")
        else:
            self.lbl_score.configure(text="")

# ------------------------ CREATE WIDGETS -------------------------------- #
    def create_widgets(self):
        self.main_frame = ctk.CTkFrame(
            self.root,
            border_width=2,
            corner_radius=10
        )

        self.score_frame = ctk.CTkFrame(
            self.root,
            border_width=2,
            corner_radius=10
        )

        # Fill the frame to the width of the window
        self.main_frame.pack(fill=tk.X, padx=20, pady=20)
        self.score_frame.pack(fill=tk.X, padx=20, pady=20)

        self.lbl_1 = ctk.CTkLabel(
            self.main_frame,
            width=65,
            text="",
            image=self.num_images[1]
        )

        self.lbl_2 = ctk.CTkLabel(
            self.main_frame,
            width=65,
            text="",
            image=self.num_images[2]
        )

        self.lbl_3 = ctk.CTkLabel(
            self.main_frame,
            width=65,
            text="",
            image=self.num_images.get(3)
        )

        self.lbl_spin = ctk.CTkLabel(
            self.main_frame,
            image=self.spin_img,
            text="",
            cursor="hand2"
        )
        self.lbl_spin.bind("<Button-1>", self.spin)

        self.lbl_score = ctk.CTkLabel(
            self.score_frame,
            text="",
            font=ctk.CTkFont(size=24)
        )

        # Grid Spin label
        self.lbl_1.grid(row=0, column=0, padx=5, pady=5)
        self.lbl_2.grid(row=0, column=1, padx=5, pady=5)
        self.lbl_3.grid(row=0, column=2, padx=5, pady=5)

        self.lbl_spin.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Grid Score label
        self.lbl_score.grid(row=0, column=0, padx=5, pady=5)

        # Bind both enter keys to the spin method.
        self.root.bind('<Return>', self.spin)
        self.root.bind('<KP_Enter>', self.spin)
        self.root.bind('<Escape>', self.quit)

# --------------------------- QUIT --------------------------------------- #
    def quit(self, *args):
        self.root.destroy()


# ------------------------- RUN PROGRAM -----------------------------------#
""" Create program object to start the program """
lucky7_app = Lucky7App()
