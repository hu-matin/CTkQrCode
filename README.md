# CTkQrCode

**A module to generate and display QR codes using CustomTkinter.**

![Screenshot](https://github.com/user-attachments/assets/895a3b61-8083-47f7-8e5d-1252d890440e)

## Features:
- Generates customizable QR codes
- Sets QR version (size/complexity)
- Adjusts box size of QR modules
- Changes border thickness
- Customizes fill color
- Changes background color
- Auto-updates QR image on changes
- Easy access to generated QR image
- Built as a CustomTkinter widget
- Uses qrcode and Pillow libraries
  
## Installation
```
pip install CTkQrCode
```

### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/hu-matin/CTkQrCode?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/hu-matin/CTkQrCode/archive/refs/heads/main.zip)

_Dont forget to leave a ⭐_

## Usage
```python
import customtkinter
from CTkQrCode import CTkQrCode

root = customtkinter.CTk()

table = CTkQrCode(master=root, qr_data = 'CTkQrCode')
table.pack(padx=20, pady=20)

root.mainloop()
```
## Arguments


| Parameter       | Description                                            |
| --------------- | ------------------------------------------------------ |
| master          | parent widget                                          |
| qr_data        | data/content encoded in the QR code (string)         |
| qr_version     | QR code version (controls size and complexity)       |
| qr_box_size   | size of each box / module in the QR code (int)         |
| qr_border      | thickness of the border around QR code (int)         |
| qr_fill_color | color of the QR code modules (fill color) (string) |
| qr_back_color | background color of the QR code (string)             |
| qr_size        | display size of the QR code image (int, pixels)      |
| corner_radius  | radius for rounded corners of QR image (int)         |
| padx            | internal horizontal padding inside the widget (int)  |
| pady            | internal vertical padding inside the widget (int)    |




## Methods
- **.generate_qr_code():** generate and display the QR code image based on current settings  
- <b>.configure(*args, **kwargs):</b> update widget configuration; supports QR-specific options and regenerates QR image on change  
- **.cget(option):** get the value of a configuration option, including QR-specific ones  
- **.set_qr_size(qr_size: int):** set QR code image size and regenerate the QR code
- **.get_qr_size():** return current QR code size
- **.set_corner_radius(corner_radius: int):** set rounded corner radius and regenerate QR code
- **.get_corner_radius():** return current corner radius value
- **.set_qr_data(qr_data: str):** update the data encoded in the QR code and regenerate
- **.set_qr_version(qr_version: int):** set QR version (complexity/size) and regenerate
- **.set_qr_box_size(qr_box_size: int):** set size of QR code boxes/modules and regenerate
- **.set_qr_border(qr_border: int):** set border width around QR code and regenerate
- **.set_qr_fill_color(qr_fill_color: str):** set fill color of QR pattern and regenerate
- **.set_qr_back_color(qr_back_color: str):** set background color behind QR code and regenerate
- **.get_qr_image():** get the current generated QR code image object
- **.get_qr_data():** get the current QR code data string
- **.get_qr_version():** get current QR version
- **.get_qr_box_size():** get current size of QR boxes
- **.get_qr_border():** get current border width
- **.get_qr_fill_color():** get current fill color
- **.get_qr_back_color():** get current background color

### Thanks for visiting! Hope it will help :)
