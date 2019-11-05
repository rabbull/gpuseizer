import os
import sys

if __name__ == '__main__':
    assert len(sys.argv) >= 3
    need = int(sys.argv[1])
    script = ' '.join(sys.argv[2:])
    os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
    while True:
        available = [i for i, value in enumerate([len(s.split('| ')) == 3 for s in os.popen('gpustat').readlines()[1:]])
                     if value]
        if need <= len(available):
            os.environ['CUDA_VISIBLE_DEVICE'] = str(available)[1:-1]
            output = os.popen(script).readlines()
            [print(line) for line in output]
            exit(0)
