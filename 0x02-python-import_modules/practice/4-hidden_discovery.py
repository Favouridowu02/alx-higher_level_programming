#!/usr/bin/python3
if __name__ == "__main__":
    """
        Prints all the names contained in hidden_4 expect the ones starting with __
    """
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
