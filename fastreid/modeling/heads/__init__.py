# encoding: utf-8
"""
@author:  liaoxingyu
@contact: sherlockliao01@gmail.com
"""

from .build import REID_HEADS_REGISTRY, build_reid_heads

# import all the meta_arch, so they will be registered
from .standard_head import StandardHead
from .arcface import ArcfaceHead
