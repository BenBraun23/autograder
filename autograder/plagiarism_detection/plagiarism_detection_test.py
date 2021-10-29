from plagiarism_detection import compare
from pathlib import Path
import time


def main():
    paths = [
        Path("test/cpp/test1.cpp"),
        Path("test/cpp/test2.cpp"),
        Path("test/c/test1.c"),
        Path("test/c/test2.c"),
        Path("test/java/Test.java"),
        Path("test/java/Test2.java"),
        Path("test/java/Test3.java"),
        Path("test/java/Test4.java"),
        Path("test/java/Test5.java"),
        Path("test/java/CountPrimes1.java"),
        Path("test/java/CountPrimes2.java"),
        Path("test/java/CountPrimes3.java"),
        Path("test/java/CountPrimes4.java"),
        Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/cpp/test1.cpp"),
        # Path("test/cpp/test2.cpp"),
        # Path("test/c/test1.c"),
        # Path("test/c/test2.c"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/cpp/test1.cpp"),
        # Path("test/cpp/test2.cpp"),
        # Path("test/c/test1.c"),
        # Path("test/c/test2.c"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/cpp/test1.cpp"),
        # Path("test/cpp/test2.cpp"),
        # Path("test/c/test1.c"),
        # Path("test/c/test2.c"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/cpp/test1.cpp"),
        # Path("test/cpp/test2.cpp"),
        # Path("test/c/test1.c"),
        # Path("test/c/test2.c"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test.java"),
        # Path("test/java/Test2.java"),
        # Path("test/java/Test3.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/CountPrimes2.java"),
        # Path("test/java/CountPrimes3.java"),
        # Path("test/java/CountPrimes4.java"),
        # Path("test/java/CountPrimes1.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
        # Path("test/java/Test5.java"),
        # Path("test/java/Test4.java"),
    ]
    # files = []
    # f = open("test/cpp/test1.cpp", "r")
    # files += [f]
    # f = open("test/cpp/test2.cpp", "r")
    # files += [f]
    # files = []
    # f = open("test/c/test1.c", "r")
    # files += [f]
    # f = open("test/c/test2.c", "r")
    # files += [f]
    # files = []
    # f = open("test/java/CountPrimes1.java", "r")
    # files += [f]
    # f = open("test/java/CountPrimes2.java", "r")
    # files += [f]
    # f = open("test/java/CountPrimes3.java", "r")
    # files += [f]
    # f = open("test/java/CountPrimes4.java", "r")
    # files += [f]
    # for i in range(15):
    #     f = open("test/java/CountPrimes4.java", "r")
    #     files += [f]
    # f = open("test/java/Test.java", "r")
    # files += [f]
    # f = open("test/java/Test2.java", "r")
    # files += [f]
    # f = open("test/java/Test3.java", "r")
    # files += [f]
    # for i in range(1):
    #     f = open("test/java/Test4.java", "r")
    #     files += [f]
    # files += [f]
    # for i in range(50):
    # 	f = open("test2.py", "r")
    # 	files += [f]
    start = time.time()
    print(compare(paths))
    print(time.time() - start)


if __name__ == "__main__":
    main()
