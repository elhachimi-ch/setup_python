import setup as sp


def main():
    setup = sp.Setup(pip='pip3.6')
    print(setup.get_commandes())


if __name__ == '__main__':
    main()
