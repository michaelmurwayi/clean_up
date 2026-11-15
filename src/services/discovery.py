import os
import pwd
from pathlib import Path
from src.schema.directory import DirectoryMetaData
from datetime import datetime


class FolderDiscovery():
    def __init__(self, path) -> None:
        self.path = path

    def clean_path(self):
        prefix = "/home/skull-walla"
        clean_path = f"{prefix}{self.path}"
        return clean_path

    def get_all_folders(self):
        #  Filter for items in the directory
        directory = Path(self.clean_path())
        folders = []
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_dir():
                    stat_info = entry.stat()
                    creation_timestamp = getattr(stat_info, "st_birthtime", stat_info.st_ctime)
                    creation_time = datetime.fromtimestamp(creation_timestamp)
                    owner = pwd.getpwuid(stat_info.st_uid).pw_name
                    

                    folders.append(DirectoryMetaData(
                        name=entry.name,
                        path= entry.path,
                        owner_permission= owner,
                        size= stat_info.st_size,
                        number_of_sub_directories= 1,
                        created_at= creation_time,
                        modified_at=creation_time
                        )
                        )
        directory = {
            "path": self.path,
            "folders": folders
        }
        
        return directory