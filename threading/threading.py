import threading

def do_first():
    print('do_first, running first block of code.1')
    print('do_first, running second block of code.2')
    print('do_first, running third block of code.3')


def do_second():
    print('do_second, running first block of code.1')
    print('do_second, running second block of code.2')
    print('do_second, running third block of code.3')


def main():
    t1 = threading.Thread(target=do_first)
    t2 = threading.Thread(target=do_second)

    # Start thread
    t1.start(), t2.start()
    
    # wait thread to complete
    t1.join(), t2.join()


if __name__ == '__main__':
    main()

