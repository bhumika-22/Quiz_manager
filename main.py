import tkinter as tk
from questions import python_questions, daa_questions
from quiz_app import QuizApp



def start_python_quiz():
    root.destroy()

    quiz_window = tk.Tk()
    QuizApp(quiz_window, "Python", python_questions)
    quiz_window.mainloop()



def start_daa_quiz():
    root.destroy()

    quiz_window = tk.Tk()
    QuizApp(quiz_window, "DAA", daa_questions)
    quiz_window.mainloop()


root = tk.Tk()

root.title("MCA Quiz Portal")
root.geometry("700x500")
root.resizable(False, False)


root.configure(bg="#EDE7F6")



title = tk.Label(
    root,
    text="MCA QUIZ PORTAL",
    font=("Arial", 26, "bold"),
    bg="#EDE7F6",
    fg="#4A4063"
)
title.pack(pady=45)


subtitle = tk.Label(
    root,
    text="Choose a subject to begin your quiz",
    font=("Arial", 14),
    bg="#EDE7F6",
    fg="#5F5874"
)
subtitle.pack(pady=10)



python_button = tk.Button(
    root,
    text="Python Quiz",
    command=start_python_quiz,
    font=("Arial", 14, "bold"),
    width=20,
    height=2,
    bg="#BDE0FE",
    fg="#263238",
    activebackground="#A9D6F5",
    relief="flat",
    cursor="hand2"
)
python_button.pack(pady=15)



daa_button = tk.Button(
    root,
    text="DAA Quiz",
    command=start_daa_quiz,
    font=("Arial", 14, "bold"),
    width=20,
    height=2,
    bg="#CDEAC0",
    fg="#263238",
    activebackground="#B8DDAA",
    relief="flat",
    cursor="hand2"
)
daa_button.pack(pady=10)


exit_button = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    font=("Arial", 11),
    width=12,
    bg="#FFCAD4",
    fg="#4A3038",
    activebackground="#F5B7C3",
    relief="flat",
    cursor="hand2"
)
exit_button.pack(pady=20)


root.mainloop()