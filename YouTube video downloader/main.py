import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("800x500")  # Set window size
        self.root.configure(bg='#ed4b23')  # Background color

        # Frame for the main content
        self.main_frame = tk.Frame(root, bg='#5a97ee', padx=100, pady=20)
        self.main_frame.pack(expand=True, fill='both')

        # Title label
        self.title_label = tk.Label(self.main_frame, text="YouTube Video Downloader", font=("Arial", 24, "bold"), bg='#ffffff')
        self.title_label.pack(pady=(0, 20))

        # URL entry
        self.url_label = tk.Label(self.main_frame, text="YouTube URL:", font=("Arial", 14), bg='#ffffff')
        self.url_label.pack(pady=(0, 10))
        self.url_entry = tk.Entry(self.main_frame, width=70, font=("Arial", 12))
        self.url_entry.pack(pady=(0, 20))

        # Save location button
        self.save_button = tk.Button(self.main_frame, text="Select Save Location", command=self.open_file_dialog, 
                                     font=("Arial", 12), bg='#4CAF50', fg='#ffffff', padx=10, pady=5)
        self.save_button.pack(pady=(0, 20))

        # Download button
        self.download_button = tk.Button(self.main_frame, text="Download Video", command=self.download_video, 
                                         font=("Arial", 12), bg='#2196F3', fg='#ffffff', padx=10, pady=5)
        self.download_button.pack()

        self.save_dir = ""

    def open_file_dialog(self):
        self.save_dir = filedialog.askdirectory()
        if self.save_dir:
            messagebox.showinfo("Selected Folder", f"Selected folder: {self.save_dir}")

    def download_video(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Input Error", "Please enter a YouTube URL.")
            return
        if not self.save_dir:
            messagebox.showerror("Save Location Error", "Please select a save location.")
            return

        try:
            ydl_opts = {
                'outtmpl': f'{self.save_dir}/%(title)s.%(ext)s',
                'format': 'best',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Download Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()
