#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict
from pytablewriter import UnicodeTableWriter

def main():
    bible_json = read_json('bible_jp.json')

    # 章数/節数を確認
    all_array_list = create_summary(bible_json)

    # テーブル作成
    show_table(all_array_list)


def read_json(path):
    """ json ファイルを読み込む """
    return json.load(open(path), object_pairs_hook=OrderedDict)


def create_summary(bible_json):
    """ 章数/節数を確認 """
    all_array_list = []
    for key, titles in bible_json.items():
        for title, chapters in titles.items():
            for chapter, sections in chapters.items():
                all_array_list.append([key, title, chapter, len(sections)])
 
    return all_array_list


def show_table(all_array_list):
    """ テーブルを表示 """
    writer = UnicodeTableWriter()
    writer.table_name = "聖書"
    writer.headers = ["旧約/新約", "書簡名", "章数", "節数"]
    writer.value_matrix = all_array_list
    writer.write_table()


if __name__ == '__main__':
    """ main function """
    main()
