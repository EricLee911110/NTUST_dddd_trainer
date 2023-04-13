'''
不记得从哪套模型改的了，可能来自于部门mobildenetv2
'''
import torch
import torch.nn as nn

from torchsummary import summary


class DdddOcr(nn.Module):
    def __init__(self, nc=3, leakyRelu=False):
        super(DdddOcr, self).__init__()
        # assert imgH % 16 == 0, 'imgH has to be a multiple of 16'

        ks = [3, 3, 3, 3, 3, 3, 2]
        ps = [1, 1, 1, 1, 1, 1, 0]
        ss = [1, 1, 1, 1, 1, 1, 1]
        #nm = [16, 32, 64, 64, 128, 128, 128] # 2700 k

        #nm = [16, 32, 64, 64, 128, 128, 64] # 912 k
        #nm = [16, 32, 64, 64, 128, 64, 64] # 821 k
        #nm = [16, 32, 32, 32, 64, 64, 64] # 692 k

        #nm = [16, 32, 64, 64, 128, 128, 32] # 449 k
        #nm = [16, 32, 64, 64, 128, 64, 32] # 367 k
        #nm = [16, 32, 32, 32, 64, 64, 32] # 238 k

        nm = [16, 32, 32, 32, 64, 64, 16] # 121 k


        cnn = nn.Sequential()

        def convRelu(i, batchNormalization=False):
            nIn = nc if i == 0 else nm[i - 1]
            nOut = nm[i]
            cnn.add_module('conv{0}'.format(i),
                           nn.Conv2d(nIn, nOut, ks[i], ss[i], ps[i]))
            if batchNormalization:
                cnn.add_module('batchnorm{0}'.format(i), nn.BatchNorm2d(nOut))
            if leakyRelu:
                cnn.add_module('relu{0}'.format(i),
                               nn.LeakyReLU(0.2, inplace=True))
            else:
                cnn.add_module('relu{0}'.format(i), nn.ReLU(True))

        convRelu(0) # (3, 16, 3, 1, 1)
        cnn.add_module('pooling{0}'.format(0), nn.MaxPool2d(2, 2))  # 64x16x64
        convRelu(1) # (16, 32, 3, 1, 1)
        cnn.add_module('pooling{0}'.format(1), nn.MaxPool2d(2, 2))  # 128x8x32
        convRelu(2, True) # (32, 64, 3, 1, 1)
        convRelu(3) # (64, 64, 3, 1, 1)
        cnn.add_module('pooling{0}'.format(2),
                       nn.MaxPool2d((2, 2), (2, 1), (0, 1)))  # 256x4x16
        convRelu(4, True) # (128, 64, 3, 1, 1)
        convRelu(5) # (128, 128, 3, 1, 1)
        cnn.add_module('pooling{0}'.format(3),
                       nn.MaxPool2d((2, 2), (2, 1), (0, 1)))  # 512x2x16
        convRelu(6, True)  # 512x1x16 # (128, 128, 2, 0, 1)

        self.cnn = cnn

    def forward(self, input):
        return self.cnn(input)

def test():
    net = DdddOcr(1)
    x = torch.randn(1, 1, 128, 128)
    summary(net, (1,128,128))
    y = net(x)
    print(y.size())

if __name__ == '__main__':
    test()