from ocr.src import Ocr


def main():
    ocr = Ocr()
    ocr.read_image()
    ocr.save_image()
    ocr.process_image()


if __name__ == '__main__':
    main()
