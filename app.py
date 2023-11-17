import qrcode
from PIL import Image
import streamlit as st
import io

# Predefined color pairs as a dictionary
color_pairs = {
    "Black on White": ("#000000", "#FFFFFF"),
    "Purple on Gold": ("#800080", "#FFD700"),
    "Teal on Coral": ("#008080", "#FF6B6B"),
    "Orange on Navy": ("#FFA500", "#000080"),
    "Magenta on Lime": ("#FF00FF", "#00FF00"),
    "Turquoise on Salmon": ("#40E0D0", "#FA8072"),
    "Indigo on Peach": ("#4B0082", "#FFDAB9"),
    "Crimson on Lavender": ("#DC143C", "#E6E6FA"),
    "Olive on Slate": ("#808000", "#708090"),
    "Amber on Midnight": ("#FFBF00", "#191970"),
    "Plum on Khaki": ("#DDA0DD", "#F0E68C")
}

def generate_qr_code(url, fill_color, bg_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=bg_color)
    return img

st.title("QR Code Generator")

# Get the URL input from the user
url = st.text_input("Enter the URL to generate a QR code:")

# Allow the user to choose a color pair
color_pair = st.selectbox("Select a color pair:", list(color_pairs.keys()))

# Add a button to generate the QR code and download it
if st.button("Generate QR Code") and url:
    try:
        fill_color, bg_color = color_pairs[color_pair]
        qr_img = generate_qr_code(url, fill_color, bg_color)
        
        # Save the PIL Image to a BytesIO buffer and convert it to bytes
        img_buffer = io.BytesIO()
        qr_img.save(img_buffer, format="PNG")
        img_bytes = img_buffer.getvalue()
        
        # Add a download button
        st.download_button(
            label="Download QR Code",
            data=img_bytes,
            key="qr_code_download",
            file_name="qr_code.png",
            mime="image/png",
        )
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
