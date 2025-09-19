# Root dir is the parent of the parent of this current directory:

import os
from lab import HOME_DIR, dirs
from transformerlab.db.db import experiment_get

from werkzeug.utils import secure_filename

"""
TFL_HOME_DIR is the directory that is the parent of the src and workspace directories.
By default, it is set to ~/.transformerlab

TFL_WORKSPACE_DIR is the directory where all the experiments, plugins, and models are stored.
By default, it is set to TFL_HOME_DIR/workspace

TFL_SOURCE_CODE_DIR is the directory where the source code is stored.
By default, it is set to TFL_HOME_DIR/src
This directory stores code but shouldn't store any data because it is erased and replaced
on updates.

You can set any of the above using environment parameters and it will override the defaults.

ROOT_DIR is a legacy variable that we should replace with the above, eventually.
"""

# TFL_SOURCE_CODE_DIR
api_py_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if api_py_dir != os.path.join(HOME_DIR, "src"):
    print(f"We are working from {api_py_dir} which is not {os.path.join(HOME_DIR, 'src')}")
    print(
        "That means you are probably developing in a different location so we will set source dir to the current directory"
    )
    TFL_SOURCE_CODE_DIR = api_py_dir
else:
    print(f"Source code directory is set to: {os.path.join(HOME_DIR, 'src')}")
    TFL_SOURCE_CODE_DIR = os.path.join(HOME_DIR, "src")

# ROOT_DIR (deprecate later)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


async def experiment_dir_by_id(experiment_id: int) -> str:
    if experiment_id is not None:
        experiment = await experiment_get(experiment_id)
    else:
        print("Error: experiment_id is None")
        return os.path.join(EXPERIMENTS_DIR, "error")

    experiment_name = experiment["name"]
    return os.path.join(dirs.EXPERIMENTS_DIR, experiment_name)


# PLUGIN_PRELOADED_GALLERY
PLUGIN_PRELOADED_GALLERY = os.path.join(TFL_SOURCE_CODE_DIR, "transformerlab", "plugins")

PLUGIN_SDK_DIR = os.path.join(TFL_SOURCE_CODE_DIR, "transformerlab", "plugin_sdk")
PLUGIN_HARNESS = os.path.join(PLUGIN_SDK_DIR, "plugin_harness.py")


# Galleries cache directory
GALLERIES_LOCAL_FALLBACK_DIR = os.path.join(TFL_SOURCE_CODE_DIR, "transformerlab/galleries/")
