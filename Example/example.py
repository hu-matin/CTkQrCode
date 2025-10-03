import customtkinter
from CTkQrCode import CTkQrCode


def main():
    app = customtkinter.CTk()
    app.geometry("400x400")
    app.title("CTkQrCode")

    frame = customtkinter.CTkFrame(master=app)
    frame.pack(pady=20)

    qr_code = CTkQrCode(
    master=frame,
    qr_data="CTkQrCode",
    qr_version=1,
    qr_border=4,
    qr_fill_color="cyan",
    qr_back_color="black",
    qr_size=400,
    corner_radius=10,
    padx=10,
    pady=10,
)
    qr_code.pack(pady=20)
    app.mainloop()
    
if __name__ == "__main__":

    main()
