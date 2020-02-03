# -*- coding: utf-8 -*-

import os, time, shutil, zipfile
from abc import abstractmethod, ABCMeta

'''Программа для сортировки файлов/фотографий по дате создания'''

SOURCE_PATH = 'сюда вносим путь до папки, где лежат файлы, требующие сортировки'
ZIP_SOURCE_PATH = 'путь до zip-файла, если сортировка требуется для заархивированных фалов'
TARGET_PATH = 'путь до папки, где в результате появятся отсортированные файлы'


class MainFileArranger(metaclass=ABCMeta):

    def __init__(self, path, target_path):
        self.path = os.path.normpath(path)
        self.target_path = os.path.normpath(target_path)
        self.stat = {}
        self.pathes = []

    def start_all_operations(self) -> None:
        self._get_stat()
        self._create_pathes()
        self._copy_file()

    @abstractmethod
    def _get_stat(self) -> None:
        pass

    def _create_pathes(self):
        '''создаем директории, по которым будут рассортированы файлы'''
        for year_of_creation, month_of_creation in self.stat.items():
            for month in month_of_creation:
                new_folder_path = os.path.join(self.target_path, str(year_of_creation), str(month))
                if os.path.exists(new_folder_path):
                    pass
                else:
                    os.makedirs(new_folder_path)
                    self.pathes.append(new_folder_path)

    def _copy_file(self):
        '''копируем файлы в созданные директории'''
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                path_to_file = os.path.join(dirpath, file)
                secs = os.path.getmtime(path_to_file)
                file_full_time = time.gmtime(secs)
                file_path = os.path.join(self.target_path, str(file_full_time[0]), str(file_full_time[1]))
                if file_path in self.pathes:
                    shutil.copy2(src=path_to_file, dst=file_path)


class FileArranger(MainFileArranger):
    '''используем этот класс, если отсортировать нужно файлы находящиеся в одной конкретной директории'''
    def _get_stat(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                path_to_file = os.path.join(dirpath, file)
                secs = os.path.getmtime(path_to_file)
                file_full_time = time.gmtime(secs)
                year_of_creation = file_full_time[0]
                month_of_creation = file_full_time[1]
                if year_of_creation in self.stat:
                    if month_of_creation not in self.stat[year_of_creation]:
                        self.stat[year_of_creation].append(month_of_creation)
                else:
                    self.stat[year_of_creation] = []


class ZipFileArranger(MainFileArranger):
    '''используем этот класс, если работаем с zip-архивом с файлами'''
    def _get_stat(self):
        if zipfile.is_zipfile(self.path):
            zip_file = zipfile.ZipFile(self.path, 'r')
            for file in zip_file.namelist():
                file_full_time = zip_file.getinfo(file).date_time
                year_of_creation = file_full_time[0]
                month_of_creation = file_full_time[1]
                if year_of_creation in self.stat:
                    if month_of_creation not in self.stat[year_of_creation]:
                        self.stat[year_of_creation].append(month_of_creation)
                else:
                    self.stat[year_of_creation] = []
        else:
            print("Это не zip-file!")

test = FileArranger(path=SOURCE_PATH, target_path=TARGET_PATH)
test.start_all_operations()
