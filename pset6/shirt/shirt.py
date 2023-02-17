from PIL import Image, ImageOps
import sys

SUPPORTED_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png"]


def main():
    check_argv()

    shirt = Image.open("shirt.png")
    photo = open_input_image()
    cropped_photo = ImageOps.fit(photo, size=(600, 600))

    cropped_photo.paste(shirt, mask=shirt)
    cropped_photo.save(sys.argv[2])


def open_input_image() -> Image:
    try:
        return Image.open(sys.argv[1])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)


def is_extension_supported(filename: str) -> bool:
    for extension in SUPPORTED_IMAGE_EXTENSIONS:
        if filename.endswith(extension):
            return True
    return False


def are_file_extensions_matching(input_filename: str, output_filename: str) -> bool:
    input_extension = input_filename[input_filename.rindex("."):]
    output_extension = output_filename[output_filename.rindex("."):]
    return False if input_extension != output_extension else True


def check_argv():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
    elif not is_extension_supported(sys.argv[1]):
        print("Invalid input")
    elif not is_extension_supported(sys.argv[2]):
        print("Invalid output")
    elif not are_file_extensions_matching(sys.argv[1], sys.argv[2]):
        print("Input and output have different extensions")
    else:
        return
    sys.exit(1)


if __name__ == '__main__':
    main()
