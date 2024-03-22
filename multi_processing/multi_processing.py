import multiprocessing

def do_first():
    print("Running do_first line 1")
    print("Running do_first line 2")
    print("Running do_first line 3")
    ...

def do_second():
    print("Running do_second line 1")
    print("Running do_second line 2")
    print("Running do_second line 3")
    ...

def main():
    t1 = multiprocessing.Process(target=do_first)
    t2 = multiprocessing.Process(target=do_second)

    # Start processes
    t1.start(), t2.start()

    # Wait processes to complete
    t1.join(), t2.join()

if __name__ == "__main__":
    main()