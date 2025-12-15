from ascii_magic import AsciiArt

def image_to_ascii(image_path: str, columns: int = 80) -> str:
    """
    Chuyển ảnh sang Ascii 
    :param image_path: đg dẫn ảnh
    : param coloumn: độ phân giải ảnh
    :retun: chuỗi ascii
    """
    art = AsciiArt.from_image(image_path)
    ascii_text = art.to_ascii(columns=columns)
    return ascii_text