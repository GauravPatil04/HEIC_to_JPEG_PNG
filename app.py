import streamlit as st
from PIL import Image
import pillow_heif
import io
import zipfile

# 1. Register HEIC opener
pillow_heif.register_heif_opener()

def convert_heic(uploaded_file, output_format):
    """
    Reads HEIC file and returns the image object and bytes in the selected format.
    """
    image = Image.open(uploaded_file)
    
    # Handle JPEG specific requirements (Transparency)
    if output_format == "JPEG":
        if image.mode in ("RGBA", "LA"):
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[-1])
            image = background
    
    img_buffer = io.BytesIO()
    
    # Save image
    image.save(img_buffer, format=output_format, quality=95, optimize=True)
    
    img_buffer.seek(0)
    return image, img_buffer

# --- UI Layout ---
st.set_page_config(page_title="HEIC Converter", layout="centered")

st.title("🔄 HEIC Converter Pro")

# --- Configuration Section ---
col1, col2 = st.columns(2)
with col1:
    # Format Selector
    format_label = st.radio(
        "Choose Output Format:",
        ("PNG", "JPEG / JPG"),
        horizontal=True
    )

# Map label to actual PIL format and extension
if format_label == "PNG":
    output_format = "PNG"
    ext = ".png"
    mime_type = "image/png"
else:
    output_format = "JPEG"
    ext = ".jpg"
    mime_type = "image/jpeg"

st.write("---")

# File Uploader
uploaded_files = st.file_uploader(
    f"Upload .heic files", 
    type=["heic", "HEIC"], 
    accept_multiple_files=True
)

if uploaded_files:
    # --- SCENARIO 1: SINGLE FILE ---
    if len(uploaded_files) == 1:
        file = uploaded_files[0]
        
        try:
            with st.spinner("Converting..."):
                image_obj, img_bytes = convert_heic(file, output_format)
                
                # Create new filename
                new_filename = file.name.rsplit('.', 1)[0] + ext
                
                # Show Preview
                st.image(image_obj, caption=f"Converted: {new_filename}", use_container_width=True)
                
                # Direct Download Button
                st.download_button(
                    label=f"⬇️ Download {new_filename}",
                    data=img_bytes,
                    file_name=new_filename,
                    mime=mime_type,
                    type="primary"
                )
        except Exception as e:
            st.error(f"Error converting file: {e}")

    # --- SCENARIO 2: MULTIPLE FILES ---
    else:
        total_files = len(uploaded_files)
        st.info(f"{total_files} files selected. Starting batch conversion...")
        
        # 1. Create a placeholder for text (This sits above the progress bar)
        status_text = st.empty()
        
        # 2. Create the progress bar
        progress_bar = st.progress(0)
        
        converted_images = {}
        
        # Process files
        for i, file in enumerate(uploaded_files):
            # Update the status text
            status_text.write(f"⏳ Processing file **{i+1}** of **{total_files}**...")
            
            try:
                # Convert
                _, img_bytes = convert_heic(file, output_format)
                
                # New Filename
                new_filename = file.name.rsplit('.', 1)[0] + ext
                converted_images[new_filename] = img_bytes
                
            except Exception as e:
                st.error(f"Error on {file.name}: {e}")
            
            # Update Progress Bar
            progress_bar.progress((i + 1) / total_files)
            
        # Update text when done
        status_text.success(f"✅ Finished! Processed {total_files} files.")
            
        # ZIP Creation
        if converted_images:
            zip_buffer = io.BytesIO()
            zip_filename = f"converted_photos_{output_format.lower()}.zip"
            
            with zipfile.ZipFile(zip_buffer, "w") as zf:
                for file_name, file_data in converted_images.items():
                    # Add to 'photos' folder inside zip
                    zf.writestr(f"photos/{file_name}", file_data.getvalue())
            
            zip_buffer.seek(0)
            
            # Batch Download Button
            st.download_button(
                label="⬇️ Download All as ZIP",
                data=zip_buffer,
                file_name=zip_filename,
                mime="application/zip",
                type="primary"
            )