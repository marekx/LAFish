import wandb
import os
from subprocess import Popen

Popen('python yolov5/train.py --img 640 --batch 16 --epochs 30 --data data.yaml --weights yolov5s.pt --cache')
