import tkinter


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My First Tkinter App")
        self.root.geometry("400x300")

        self.label = tkinter.Label(root, text="Hello, Tkinter!")
        self.label.pack(pady=20)

        self.button = tkinter.Button(root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyApp(root)
    root.mainloop()
