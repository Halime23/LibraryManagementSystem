import tkinter as tk
from library_qui import LoginGUI

if __name__ == "__main__":
    login_root = tk.Tk()
    login_app = LoginGUI(login_root)
    login_root.mainloop()