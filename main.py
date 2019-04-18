import setup as sp
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mac', type=int, help='What is OS?', default=0)
    parser.add_argument('-u', '--update', type=int, default=0,
                        help='Did you need to update commandes file after finish?')
    parser.add_argument('-g', '--gpu', type=int, default=1,
                        help='Did you want to install gpu version?')
    args = parser.parse_args()
    setup = sp.Setup(gpu=args.gpu)
    print(args.gpu)
    setup.start(mac=args.mac, updtae=args.update)


if __name__ == '__main__':
    main()
