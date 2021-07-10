import json
import random

from argparse import ArgumentParser


def main():

    parser = ArgumentParser()

    parser.add_argument('-c', '--chapter', type=str, help='Select the chapter. Otherwise it will be randomly selected', default=None)
    parser.add_argument('-n', '--num_extractions', type=int, default=1, help='Select the number of extractions')
    parser.add_argument('-i', '--index', type=str, default='indices/index.json', help='Select the path to the index')
    parser.add_argument('-s', '--session', type=str, default=None, help='Select the path to the session')
    parsed_args = parser.parse_args()

    chapter = parsed_args.chapter
    num_extractions = parsed_args.num_extractions
    index = parsed_args.index
    session = parsed_args.session

    # read the index file
    with open(index) as handle:
        dict = json.loads(handle.read())

    chapters = dict.keys()

    # check if num_extractions is greater than 1
    num_extractions = max(1,num_extractions)



    # check the chapter
    # if it is still None (no input) it will be randomly chosen
    if not chapter:
        random_chapter_idx = random.randint(0,len(chapters)-1)
        chapter = list(chapters)[random_chapter_idx]

    if chapter in chapters:

        print(f"Tell me from chapter {chapter}" + " >> ", end="")

        for i in range(num_extractions):
            print(random.randint(1,dict[chapter]), end=" ")
    else:
        print("Wrong chapter")


if __name__ == '__main__':
    main()