from utils import get_line, gen_from_pil, gen_from_xkcd, gen_from_rand
import io
from PIL import Image

def test(color=None):
    for func in [gen_from_pil, gen_from_xkcd, gen_from_rand]:
        try:
            img = func(color)
            break
        except:
            continue

    with io.BytesIO() as image_binary:
        img.save(image_binary, 'PNG')
        image_binary.seek(0)
        print("Nice")
        # await ctx.send(file=discord.File(fp=image_binary, filename=f'{color}.png'))

test('blue')
test('red')
test('green')
test('poop')
test()

