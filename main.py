import setup as sp
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mac', type=bool, help='What is OS?', default=False)
    parser.add_argument('-u', '--update', type=bool, default=False,
                        help='Did you need to update commandes file after finish?')
    parser.add_argument('-g', '--gpu', type=bool, default=False,
                        help='Did you want to install gpu version?')
    args = parser.parse_args()
    print(type(args.mac))
    setup = sp.Setup(gpu=args.gpu)
    setup.start(mac=args.mac, updtae=args.update)


if __name__ == '__main__':
    main()
