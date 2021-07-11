import json
import random

from argparse import ArgumentParser

from utils import get_dict_session




def main():

    parser = ArgumentParser()

    parser.add_argument('-c', '--chapter', type=str, help='Select the chapter. Otherwise it will be randomly selected', default=None)
    parser.add_argument('-n', '--num_extractions', type=int, default=1, help='Select the number of extractions')
    parser.add_argument('-i', '--index', type=str, default='indices/index.json', help='Select the path to the index')
    parser.add_argument('-s', '--session', type=str, default='progresses/session-index.json', help='Select the path to the session')
    parsed_args = parser.parse_args()

    chapter = parsed_args.chapter
    num_extractions = parsed_args.num_extractions
    index = parsed_args.index
    session = parsed_args.session

    # read the index file
    with open(index) as handle:
        dict_index = json.loads(handle.read())

    chapters = dict_index.keys()

    # check if num_extractions is greater than 1
    num_extractions = max(1,num_extractions)

    # get the exhisting session or create a new one
    dict_session = get_dict_session(session)


    # check the chapter
    # -- if it is still None (no input) it will be randomly chosen
    if not chapter:
        random_chapter_idx = random.randint(0,len(chapters)-1)
        chapter = list(chapters)[random_chapter_idx]

    if chapter in chapters:

        print(f"Tell me from chapter {chapter}" + " >> ", end="")

        for i in range(num_extractions):
            extracted = random.randint(1,dict_index[chapter])
            print(extracted, end=" ")

            if not extracted in dict_session[chapter].keys():
                dict_session[chapter][extracted] = 1
            else:
                dict_session[chapter][extracted] += 1

        with open(f"progresses/session-{index.split('/')[1]}", "w") as outfile:
            json.dump(dict_session, outfile, indent=2)

    else:
        print("Wrong chapter")


if __name__ == '__main__':
    main()
