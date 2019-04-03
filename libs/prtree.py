#!/usr/bin/python3

from graphviz import Digraph, nohtml
import imageio
import os
import glob


class prtree(object):
    dots = []

    def node(self, dot, node):
        if node.color:
            # 红黑
            dot.node(
                '%s' % (node.key),
                nohtml('<f0> |<f1> %s|<f2>' % (node.value)),
                color='%s' % (node.color))
        else:
            # 普通
            dot.node('%s' % (node.key),
                     nohtml('<f0> |<f1> %s|<f2>' % (node.value)))

    def tree(self, dot, root):
        if root:
            self.node(dot, root)
        if root and root.lchild:
            # 链接左子树
            dot.edge('%s:f0:sw' % (root.key), '%s:f1' % (root.lchild.key))
            self.tree(dot, root.lchild)
        if root and root.rchild:
            # 链接右子树
            dot.edge('%s:f2:se' % (root.key), '%s:f1' % (root.rchild.key))
            self.tree(dot, root.rchild)

    def dot(self, root):
        dots = Digraph(
            name='terr',
            comment='Tree',
            node_attr={
                'shape': 'record',
                'style': 'filled',
                'color': 'black',  # 默认为黑色
                'fontcolor': 'white'  # 字体颜色
            })
        self.tree(dots, root)
        return dots

    def jpg(self):
        pass

    def pdf(self):
        pass

    def gif(self):
        tmp = 'tmp'

        def mk_dir(tmp):
            try:
                os.mkdir(tmp)
            except FileExistsError as e:
                e
            # 进入子目录
            os.chdir(tmp)

        def cr_png():
            for i in range(0, len(self.dots)):
                self.dots[i].attr(size='5,5')
                self.dots[i].format = 'png'
                self.dots[i].render(
                    filename='%s' % (str(i)),
                    directory=None,
                    view=False,
                    cleanup=True)

        def find_all_png():
            pngs = glob.glob(r"./*.png")
            buf = []
            for png in pngs:
                buf.append(png)
            return buf

        def cr_gif(image_list, gif_name):
            frames = []
            for image_name in image_list:
                frames.append(imageio.imread(image_name))
                # Save them as frames into a gif
            imageio.mimsave(gif_name, frames, 'GIF', duration=0.8)

        mk_dir(tmp)
        cr_png()
        buf = find_all_png()
        cr_gif(buf, 'test')
        pass
