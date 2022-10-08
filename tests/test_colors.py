from utils.utils_colors import gen_from_pil, gen_from_xkcd, gen_from_rand, get_color_and_mode, rgb2hex, rgba2hex


### PIL Tests ###


def test_gen_from_pil_rgb():
    img, phrase = gen_from_pil("red", "RGB")
    assert img is not None
    assert phrase == "red"


def test_gen_from_pil_rgba():
    img, phrase = gen_from_pil("red", "RGBA")
    assert img is not None
    assert phrase == "red"


### XKCD Tests ###


def test_gen_from_xkcd():
    img, desc = gen_from_xkcd("cloudy blue")
    assert img is not None
    assert desc == "#acc2d9"


### Random Test ###


def test_gen_from_rand():
    # This should always generate an image
    img, phrase = gen_from_rand()
    assert img is not None
    assert phrase is not None


### Input Tests ###


def test_get_color_and_mode_color_name():
    color, mode = get_color_and_mode("red")
    assert color == "red"
    assert mode == "RGB"


def test_get_color_and_mode_hex_no_alpha():
    color, mode = get_color_and_mode("#ff0000")
    assert color == "#ff0000"
    assert mode == "RGB"


def test_get_color_and_mode_hex_alpha():
    color, mode = get_color_and_mode("#ff0000ff")
    assert color == "#ff0000ff"
    assert mode == "RGBA"


def test_get_color_and_mode_rgb_text():
    color, mode = get_color_and_mode("rgb(255, 0, 0)")
    assert color == (255, 0, 0)
    assert mode == "RGB"


def test_get_color_and_mode_rgba_text():
    color, mode = get_color_and_mode("rgba(255, 0, 0, 255)")
    assert color == (255, 0, 0, 255)
    assert mode == "RGBA"


def test_rgb2hex():
    assert rgb2hex(255, 0, 0) == "#ff0000"


def test_rgba2hex():
    assert rgba2hex(255, 0, 0, 255) == "#ff0000ff"