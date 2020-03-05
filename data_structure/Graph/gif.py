#!/usr/bin/python3

from GH import Graph, prgraph
# from test import randomGr
import functools, os, imageio, time, copy
import glob

test = prgraph()
gr = copy.deepcopy(Graph().load())
dot = test.graph(gr)


def dot_node(w: int):
    dot.node(str(w), color='red')
    dot.attr(size='20,20')
    dot.format = 'png'
    dot.render(filename='%s' % (str(time.time() * 1000 % 10000)),
               directory=None,
               view=False,
               cleanup=True)


def wrap_dot_node(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):

        dot.node(str(args[2]), color='red')
        dot.attr(size='20,20')
        dot.format = 'png'
        dot.render(filename='%s' % (str(time.time() * 1000 % 10000)),
                   directory=None,
                   view=False,
                   cleanup=True)
        return func(*args, **kw)

    return wrapper


def mk_dir(tmp: str = 'tmp'):
    try:
        os.mkdir(tmp)
    except FileExistsError as e:
        e
    # 进入子目录
    os.chdir(tmp)


def getGr():
    mk_dir()
    return gr


def gif():
    def find_all_png():
        pngs = glob.glob(r"./*.png")
        pngs.sort()
        buf = []
        for png in pngs:
            buf.append(png)
        return buf

    def cr_gif(image_list, gif_name):
        frames = []
        for image_name in image_list:
            frames.append(imageio.imread(image_name))
            # Save them as frames into a gif
        imageio.mimsave(gif_name, frames, 'GIF', duration=1)

    buf = find_all_png()
    cr_gif(buf, 'test.gif')


if __name__ == "__main__":
    mk_dir()
    gif()