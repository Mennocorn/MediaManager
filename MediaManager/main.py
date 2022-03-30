import os
import glob
from errors import NotValidDirectory


class FileMaker:
    def __init__(self, path: str):
        if os.path.exists(path):
            self.file = path
        else:
            raise NotValidDirectory(f'"{path}" is not a valid file')

    def name(self):
        arg1 = self.file.split('/')
        return arg1[len(arg1) - 1].split('.')[0]

    def created_at(self):
        return os.path.getctime(self.file)

    def modified_at(self):
        return os.path.getmtime(self.file)

    def accessed_at(self):
        return os.path.getatime(self.file)

    def is_json(self):
        if self.file.endswith('.json'):
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.file


class MediaManager:
    def __init__(self, directory: str):
        if os.path.exists(directory):
            self.directory = directory
        else:
            raise NotValidDirectory(f'"{directory}" is not a valid directory')
        self.formats_video = ['.m1v', '.mpeg', '.mov', '.qt', '.mpa', '.mpg', '.mpe', '.avi', '.movie', '.mp4']
        self.formats_audio = ['.ra', '.aif', '.aiff', '.aifc', '.wav', '.au', '.snd', '.mp3', '.mp2']
        self.formats_pictures = ['.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg', '.xpm', '.ief', '.pbm', '.tif', '.gif', '.ppm', '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm']
        self.formats_all = self.formats_video + self.formats_audio + self.formats_pictures

    def all_media(self):
        glob_all = []
        for globs_all in glob.glob(f'{self.directory}/*{self.formats_all}'):
            glob_all.append(globs_all.split(f'{self.directory}\\')[1])

        return glob_all

    def all_video(self):
        glob_video = []
        for globs_video in glob.glob(f'{self.directory}/*{self.formats_video}'):
            glob_video.append(globs_video.split(f'{self.directory}\\')[1])

        return glob_video

    def all_audio(self):
        glob_audio = []
        for globs_audio in glob.glob(f'{self.directory}/*{self.formats_audio}'):
            glob_audio.append(globs_audio.split(f'{self.directory}\\')[1])

        return glob_audio

    def all_pictures(self):
        glob_pictures = []
        for globs_picture in glob.glob(f'{self.directory}/*{self.formats_pictures}'):
            glob_pictures.append(globs_picture.split(f'{self.directory}\\')[1])

        return glob_pictures

    @staticmethod
    def remove_media(media: FileMaker):
        os.remove(str(media))





