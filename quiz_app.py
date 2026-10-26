
import tkinter as tk
from tkinter import messagebox
import random


class QuizApp:

    def __init__(self, root, subject, question_bank):

        self.root = root
        self.subject = subject

        # Select 5 random questions from 15
        self.questions = random.sample(question_bank, 5)

        self.question_number = 0
        self.score = 0

        self.selected_answer = tk.StringVar()

        self.create_quiz_screen()
        self.show_question()


    def create_quiz_screen(self):

        self.root.title(self.subject + " Quiz")
        self.root.geometry("750x500")
        self.root.resizable(False, False)

        # Pastel peach background
        self.root.configure(bg="#FFF1E6")


        # Heading
        self.heading = tk.Label(
            self.root,
            text=self.subject + " QUIZ",
            font=("Arial", 24, "bold"),
            bg="#FFF1E6",
            fg="#5D4057"
        )
        self.heading.pack(pady=25)


        # Question number
        self.number_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold"),
            bg="#FFF1E6",
            fg="#6D597A"
        )
        self.number_label.pack()


        # Question text
        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 15),
            wraplength=650,
            bg="#FFF1E6",
            fg="#403D39"
        )
        self.question_label.pack(pady=25)


        # Four answer options
        self.option_buttons = []

        for i in range(4):

            button = tk.Radiobutton(
                self.root,
                text="",
                variable=self.selected_answer,
                value="",
                font=("Arial", 12),
                width=50,
                anchor="w",
                bg="#FFF1E6",
                fg="#403D39",
                activebackground="#FFE5D9",
                selectcolor="#FFD6BA"
            )

            button.pack(pady=5)

            self.option_buttons.append(button)


        # Next / Submit button
        self.next_button = tk.Button(
            self.root,
            text="Next",
            command=self.next_question,
            font=("Arial", 12, "bold"),
            width=15,
            bg="#CDB4DB",
            fg="#3E3047",
            activebackground="#B99AC8",
            relief="flat",
            cursor="hand2"
        )

        self.next_button.pack(pady=25)


    def show_question(self):

        current_question = self.questions[self.question_number]


        # Question number
        self.number_label.config(
            text=f"Question {self.question_number + 1} of 5"
        )


        # Question
        self.question_label.config(
            text=current_question["question"]
        )


        # Remove previous selection
        self.selected_answer.set("")


        # Display options
        for i in range(4):

            option = current_question["options"][i]

            self.option_buttons[i].config(
                text=option,
                value=option
            )


        # Change button text on last question
        if self.question_number == 4:

            self.next_button.config(
                text="Submit",
                bg="#FFCAD4"
            )

        else:

            self.next_button.config(
                text="Next",
                bg="#CDB4DB"
            )


    def next_question(self):

        user_answer = self.selected_answer.get()


        # Check whether an option is selected
        if user_answer == "":

            messagebox.showwarning(
                "Answer Required",
                "Please select an option before continuing."
            )

            return


        correct_answer = self.questions[
            self.question_number
        ]["answer"]


        # Check answer
        if user_answer == correct_answer:

            self.score += 1


        # Move to next question
        if self.question_number < 4:

            self.question_number += 1

            self.show_question()

        else:

            self.show_result()


    def show_result(self):

        percentage = (self.score / 5) * 100


        # Result message
        if percentage >= 80:

            result_message = "Excellent Performance!"

        elif percentage >= 60:

            result_message = "Good Performance!"

        elif percentage >= 40:

            result_message = "Average Performance!"

        else:

            result_message = "Keep Practicing!"


        # Show result
        messagebox.showinfo(
            "Quiz Result",

            f"Subject: {self.subject}\n\n"
            f"Score: {self.score} / 5\n"
            f"Percentage: {percentage:.0f}%\n\n"
            f"{result_message}"
        )


        # Close quiz
        self.root.destroy()