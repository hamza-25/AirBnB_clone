#!/usr/bin/python3
"""Define package-level initialization file
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
