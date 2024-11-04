import os

def extract_jpegs_from_raw(raw_file_path, output_folder="camera_images"):
    os.makedirs(output_folder, exist_ok=True)

    with open(raw_file_path, "rb") as raw_file:
        data = raw_file.read()

    start_marker = b'\xff\xd8'
    end_marker = b'\xff\xd9'
    start = 0
    file_count = 0

    while True:
        start = data.find(start_marker, start)
        if start == -1:
            break
        end = data.find(end_marker, start) + 2
        if end == -1:
            break

        jpeg_data = data[start:end]
        jpeg_file_path = os.path.join(output_folder, f"image_{file_count:03d}.jpg")

        with open(jpeg_file_path, "wb") as jpeg_file:
            jpeg_file.write(jpeg_data)
        
        print(f"Extracted {jpeg_file_path}")

        start = end
        file_count += 1

# Dateipfad zur .txt Datei angeben
extract_jpegs_from_raw("camera_udp_stream.txt")
