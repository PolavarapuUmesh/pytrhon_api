import base64

def decode_base64_to_file(encoded_file, output_file):
    with open(encoded_file, "rb") as file:
        encoded_data = file.read()
        decoded_data = base64.b64decode(encoded_data)
        with open(output_file, "wb") as decoded_file:
            decoded_file.write(decoded_data)
    print(f"File {encoded_file} has been decoded and saved as {output_file}")
decode_base64_to_file("encoded_file.txt", "decoded_example.txt")
