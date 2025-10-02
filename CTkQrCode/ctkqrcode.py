'''
CTkQrCode Module
A CustomTkinter widget to generate and display QR codes.
author: Matin
license: MIT
github: https://github.com/hu_matin
'''

import customtkinter
import qrcode
from PIL import Image, ImageTk, ImageDraw

class CTkQrCode(customtkinter.CTkLabel):
    def __init__(
        self,
        master=None,
        qr_data: str = "https://github.com/hu-matin",
        qr_version: int = 1,
        qr_box_size: int = 10,
        qr_border: int = 4,
        qr_fill_color: str = "black",
        qr_back_color: str = "white",
        qr_size: int = 200,
        corner_radius: int = 0,
        padx: int = 0,
        pady: int = 0,
        **kwargs
    ):

        super().__init__(
            master=master,
            width=qr_size,
            height=qr_size,
            corner_radius=corner_radius,
            padx=padx,
            pady=pady,
            text="",
        )

        self.qr_data = qr_data
        self.qr_version = qr_version
        self.qr_box_size = qr_box_size
        self.qr_border = qr_border
        self.qr_fill_color = qr_fill_color
        self.qr_back_color = qr_back_color
        self._qr_size = qr_size
        self._corner_radius = corner_radius
        self.qr_image = None

        self.bind("<Configure>", self._on_resize)
        self.generate_qr_code()

    def _on_resize(self, event):
        self.generate_qr_code()

    def generate_qr_code(self):
        width = self.winfo_width()
        height = self.winfo_height()
        size = min(width, height)
        if size < 2:
            size = self._qr_size

        qr = qrcode.QRCode(
            version=self.qr_version,
            box_size=self.qr_box_size,
            border=self.qr_border
        )
        qr.add_data(self.qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.qr_fill_color, back_color=self.qr_back_color).convert("RGBA")
        img = img.resize((size, size), Image.LANCZOS)

        if self._corner_radius > 0:
            mask = Image.new("L", (size, size), 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle(
                [(0, 0), (size, size)],
                radius=self._corner_radius,
                fill=255
            )
            img.putalpha(mask)

        self.qr_image = ImageTk.PhotoImage(img)
        super().configure(image=self.qr_image, text="")

    def configure(self, *args, **kwargs):
        qr_related = False
        for key in [
            "qr_data", "qr_version", "qr_box_size", "qr_border",
            "qr_fill_color", "qr_back_color", "qr_size", "corner_radius"
        ]:
            if key in kwargs:
                if key == "qr_size":
                    self._qr_size = kwargs.pop(key)
                elif key == "corner_radius":
                    self._corner_radius = kwargs.pop(key)
                    super().configure(corner_radius=self._corner_radius)
                else:
                    setattr(self, key, kwargs.pop(key))
                qr_related = True
                
        kwargs["text"] = ""
        kwargs["anchor"] = "nw"
        super().configure(*args, **kwargs)
        if qr_related:
            self.generate_qr_code()

    def cget(self, option):
        if option in [
            "qr_data", "qr_version", "qr_box_size", "qr_border",
            "qr_fill_color", "qr_back_color", "qr_size", "corner_radius"
        ]:
            if option == "qr_size":
                return self._qr_size
            if option == "corner_radius":
                return self._corner_radius
            return getattr(self, option)
        return super().cget(option)

    def set_qr_size(self, qr_size: int):
        self._qr_size = qr_size
        super().configure(width=qr_size, height=qr_size)
        self.generate_qr_code()

    def get_qr_size(self):
        return self._qr_size

    def set_corner_radius(self, corner_radius: int):
        self._corner_radius = corner_radius
        super().configure(corner_radius=corner_radius)
        self.generate_qr_code()

    def get_corner_radius(self):
        return self._corner_radius

    def set_qr_data(self, qr_data: str):
        self.qr_data = qr_data
        self.generate_qr_code()

    def set_qr_version(self, qr_version: int):
        self.qr_version = qr_version
        self.generate_qr_code()

    def set_qr_box_size(self, qr_box_size: int):
        self.qr_box_size = qr_box_size
        self.generate_qr_code()

    def set_qr_border(self, qr_border: int):
        self.qr_border = qr_border
        self.generate_qr_code()

    def set_qr_fill_color(self, qr_fill_color: str):
        self.qr_fill_color = qr_fill_color
        self.generate_qr_code()

    def set_qr_back_color(self, qr_back_color: str):
        self.qr_back_color = qr_back_color
        self.generate_qr_code()

    def get_qr_image(self):
        return self.qr_image

    def get_qr_data(self):
        return self.qr_data

    def get_qr_version(self):
        return self.qr_version

    def get_qr_box_size(self):
        return self.qr_box_size

    def get_qr_border(self):
        return self.qr_border

    def get_qr_fill_color(self):
        return self.qr_fill_color

    def get_qr_back_color(self):
        return self.qr_back_color

# github : https://github.com/hu_matin/CTkQrCode