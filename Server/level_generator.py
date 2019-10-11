from PIL import Image
import level_io as li

def get_block_type(pixel):
    brightness = pixel[0]

    if brightness == 255:
        return None
    elif brightness < 128:
        return "SquareSmall"
    else:
        return "TNT"


def get_block_position(x, y, baseline):
    # 0 <= x, y, baseline <= 19
    x_offset = 0
    y_offset = -3.3
    block_size = .445

    x = x * block_size + x_offset
    y = (baseline - y) * block_size + y_offset

    return x, y


def generate(path):
    paint = Image.open('temp.png', 'r')
    paint = paint.resize((20, 20))
    pix_data = paint.load()

    # -----------------
    # find baseline
    baseline = -1
    for y in range(19, -1, -1):
        for x in range(0, 20):
            if get_block_type(pix_data[x, y]) != None:
                baseline = y
                break
        if baseline != -1:
            break
    if baseline == -1:
        print("The input is blank.")
        exit(0)
    # -----------------

    new_level = li.level()
    new_level.add_birds("BirdRed", 1)

    for x in range(0, 20):
        # Confirm the column has blocks
        has_blocks = False
        for y in range(baseline, -1, -1):
            if get_block_type(pix_data[x, y]) != None:
                has_blocks = True
                final_block = y
        # ----------------------
        if has_blocks == True:
            for y in range(baseline, -1, -1):
                need_support = True
                block = get_block_type(pix_data[x, y])
                block_x, block_y = get_block_position(x, y, baseline)
                if block == None and final_block < y:
                    new_level.add_block(
                        type="SquareSmall", x=block_x, y=block_y, rotation="0", material="ice")
                else:
                    new_level.add_block(type=block, x=block_x,
                                        y=block_y, rotation="0", material="wood")

    new_level.export(path)


if __name__ == "__main__":
    generate("levels/level-1.xml")
