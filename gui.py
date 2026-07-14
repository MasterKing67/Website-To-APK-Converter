import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from generator import generate_project


class ShinyCalcGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Shiny Calc Project Generator")
        self.root.geometry("600x420")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Shiny Calc Project Generator",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=15)

        frame = ttk.Frame(self.root, padding=15)
        frame.pack(fill="both", expand=True)

        # App Name
        ttk.Label(frame, text="App Name").grid(row=0, column=0, sticky="w", pady=5)

        self.app_name = ttk.Entry(frame, width=45)
        self.app_name.insert(0, "Shiny Calc")
        self.app_name.grid(row=0, column=1, pady=5)

        # Package Name
        ttk.Label(frame, text="Package Name").grid(row=1, column=0, sticky="w", pady=5)

        self.package_name = ttk.Entry(frame, width=45)
        self.package_name.insert(0, "com.shiny.calculator")
        self.package_name.grid(row=1, column=1, pady=5)

        # Website URL
        ttk.Label(frame, text="Website URL").grid(row=2, column=0, sticky="w", pady=5)

        self.website_url = ttk.Entry(frame, width=45)
        self.website_url.insert(0, "https://example.com")
        self.website_url.grid(row=2, column=1, pady=5)

        # Output Folder
        ttk.Label(frame, text="Output Folder").grid(row=3, column=0, sticky="w", pady=5)

        self.output_folder = ttk.Entry(frame, width=35)
        self.output_folder.grid(row=3, column=1, sticky="w")

        ttk.Button(
            frame,
            text="Browse",
            command=self.browse_folder
        ).grid(row=3, column=2, padx=5)

        # Generate Button
        ttk.Button(
            self.root,
            text="Generate Project",
            command=self.generate,
        ).pack(pady=20)

        self.status = tk.Label(
            self.root,
            text="Ready",
            fg="green"
        )
        self.status.pack()

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder.delete(0, tk.END)
            self.output_folder.insert(0, folder)

    def generate(self):
        app_name = self.app_name.get().strip()
        package = self.package_name.get().strip()
        url = self.website_url.get().strip()
        output = self.output_folder.get().strip()

        if not app_name:
            messagebox.showerror("Error", "Please enter an app name.")
            return

        if not package:
            messagebox.showerror("Error", "Please enter a package name.")
            return

        if not url:
            messagebox.showerror("Error", "Please enter a website URL.")
            return

        if not output:
            messagebox.showerror("Error", "Please choose an output folder.")
            return

        try:
            project = generate_project(
                app_name,
                package,
                url,
                output
            )

            self.status.config(
                text="Project created successfully!",
                fg="green"
            )

            messagebox.showinfo(
                "Success",
                f"Project created!\n\n{project}"
            )

        except Exception as e:
            self.status.config(
                text="Generation failed.",
                fg="red"
            )

            messagebox.showerror(
                "Error",
                str(e)
            )


def start_gui():
    root = tk.Tk()
    ShinyCalcGUI(root)
    root.mainloop()


if __name__ == "__main__":
    start_gui()
