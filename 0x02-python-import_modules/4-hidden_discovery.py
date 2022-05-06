#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    atributes = dir(hidden_4)
    for atribut in atributes:
        if atribut[:2] != "__":
            print(atribut)
