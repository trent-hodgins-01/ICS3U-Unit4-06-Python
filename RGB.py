# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/06/2021
# This is teh RGB program
# It goes through all the RGB clolors


def main():
    # this function does addition math

    # process and output
    counter1 = 0
    counter2 = 0
    counter3 = 0

    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("RGB({0},{1},{2}".format(counter1, counter2, counter3))

    print("\nDone")


if __name__ == "__main__":
    main()
