from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)        #Its an entity as it will help to create your own custom return type
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


