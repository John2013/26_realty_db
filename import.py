from argparse import ArgumentParser
from os.path import exists
from typing import List

from flask import json


def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        '-f',
        '--filepath',
        type=str,
        help="путь до файла c данными",
        default='ads.json'
    )
    args = parser.parse_args()
    return args


def is_valid(args) -> bool:
    if not exists(args.filepath):
        print("Файл {} не найден".format(args.filepath))
        return False

    return True


def get_data(filepath: str) -> list:
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_outer_id_list(apartments_list) -> List[int]:
    return list(apartment['id'] for apartment in apartments_list)


# def get_saved_outer_ids(outer_id_list: List[int]) -> List[int]:
#     session = Session()
#     query = Apartment.query.filter(
#         Apartment.outer_id.in_(outer_id_list)
#     )
#     return query.all()


# def save_apartments(apartments_list):
#     outer_ids = get_outer_id_list(apartments_list)
#     old_apartments = filter(
#         lambda apartment: apartment['id'] in outer_ids,
#         apartments_list
#     )
#     new_apartments = filter(
#         lambda apartment: apartment['id'] not in outer_ids,
#         apartments_list
#     )
#
#
#
#     old_apartments = get_old_apartments(outer_ids)
#
#     for


if __name__ == '__main__':
    args = get_args()
    if not is_valid(args):
        exit(1)

    apartments_list = get_data(args.filepath)
    outer_ids_list = get_outer_id_list(apartments_list)

