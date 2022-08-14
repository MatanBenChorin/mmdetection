"""
python tools/test.py \
    configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py \
    checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth \
    --show-dir my_dir/results/faster_rcnn_r50_fpn_1x_results
"""

import tools.test as test
import sys
import os

def main():
    os.chdir("../../")
    sys.argv.append("configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py") # CONFIG_FILE
    sys.argv.append("checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth") # CHECKPOINT_FILE
    sys.argv.append("--show-dir=my_dir/results/faster_rcnn_r50_fpn_1x_results/imgs")
    sys.argv.append("--show-dir=my_dir/results/faster_rcnn_r50_fpn_1x_results/imgs")
    sys.argv.append("--show")
    test.main()


if __name__ == '__main__':
    main()
