import sys
sys.path.append('../')
from pycore.tikzeng import *
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    to_input('121_red.png', to='(-9,0,0)', width=12, height=12, name="input"),
    to_input('121_green.png', to='(-8,0,0)', width=12, height=12, name="input"),
    to_input('121_blue.png', to='(-7,0,0)', width=12, height=12, name="input"),
    to_input('121_rgb.png', to='(-3,0,0)', width=12, height=12, name="input"),

    to_Conv("conv1", s_filer=112, n_filer=64, offset="(0,0,0)", to="(0,0,0)", height=56, depth=56, width=10),
    #to_connection("input", "conv1"),

    # MaxPool Layer (MaxPool2d-4)
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", height=14, depth=14, width=2),

    # Conv Layer 2 (Conv2d-5), BatchNorm2d-6, ReLU-7
    to_Conv("conv2", s_filer=28, n_filer=128, offset="(2.5,0,0)", to="(pool1-east)", height=14, depth=14, width=16),
    to_connection("pool1", "conv2"),

    # Conv Layer 3 (Conv2d-8), BatchNorm2d-9, ReLU-10
    to_Conv("conv3", s_filer=14, n_filer=256, offset="(2,0,0)", to="(conv2-east)", height=7, depth=7, width=24),
    to_connection("conv2", "conv3"),

    # Conv Layer 4 (Conv2d-12), BatchNorm2d-13, ReLU-14
    to_Conv("conv4", s_filer=7, n_filer=512, offset="(1.5,0,0)", to="(conv3-east)", height=3, depth=3, width=32),
    to_connection("conv3", "conv4"),

    # AdaptiveAvgPool Layer
    to_Pool("adaptive_pool", offset="(0,0,0)", to="(conv4-east)", height=1, depth=1, width=2),

    # Fully Connected Layers (Linear-20, Linear-22)
    to_Conv("fc1", s_filer=256, n_filer='', offset="(2,0,0)", to="(adaptive_pool-east)", height=1, depth=30, width=1),
    to_Conv("fc2", s_filer=128, n_filer='', offset="(1,0,0)", to="(fc1-east)", height=1, depth=15, width=1),
    to_connection("adaptive_pool", "fc1"),
    to_connection("fc1", "fc2"),
    to_Conv("fc3", s_filer=6, n_filer='', offset="(1,0,0)", to="(fc2-east)", height=1, depth=3, width=1),
    to_connection("fc2", "fc3"),


    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
    main()

