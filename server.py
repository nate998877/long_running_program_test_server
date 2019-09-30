#!/usr/bin/env python3
import os
import random
import time


def get_words():
    """reads Alice.txt and finds 40ish random words
    
    Returns:
        list -- List of 40ish random words.
    """
    list_of_rand = []
    rand_word = []

    with open(os.path.join(os.path.dirname(__file__), 'alice.txt'), "r") as f:
        for _ in range(40):
            list_of_rand.append(random.randrange(0, sum(1 for line in f)))

        for i, line in enumerate(f.readlines()):
            if i in list_of_rand:
                w_list = line.split(" ")
                rand_word.append(
                    w_list[random.randrange(0, len(w_list))].rstrip())

    return [w for w in rand_word if w] #rand_word contains ""


def write_log(word_list):
    """Takes A list of random words and appends to a log in the parent dir
    
    Arguments:
        word_list {list} -- List of random words
    """
    with open("alice_log.txt", "a+") as f:
        for i in range(len(word_list)):
            if i % 4 == 0:
                f.write("\n")
            f.write(word_list[i] + " ")


def main():
    while True:
        word_list = get_words()
        write_log(word_list)
        time.sleep(10)


if __name__ == "__main__":
    main()
