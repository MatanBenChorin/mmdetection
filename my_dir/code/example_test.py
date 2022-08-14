"""
python tools/test.py \
    configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py \
    checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth \
    --show-dir my_dir/results/faster_rcnn_r50_fpn_1x_results
"""

import tools.test as test
import sys
import os


def run_test(config_file,checkpoint_file,imgs_result_dir):
    os.chdir("../../")
    sys.argv.append(config_file)  # CONFIG_FILE
    sys.argv.append(checkpoint_file)  # CHECKPOINT_FILE
    sys.argv.append("--show-dir="+imgs_result_dir)
    sys.argv.append("--show")
    test.main()

def main():
    # genuine_coco()
    slim_coco()

def genuine_coco():
    config_file = 'configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
    checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
    imgs_result_dir = 'my_dir/results/faster_rcnn_r50_fpn_1x_results/imgs'
    run_test(config_file, checkpoint_file, imgs_result_dir)

def slim_coco():
    config_file = 'my_dir/my_configs/faster_rcnn_r50_fpn_1x_coco_slim.py'
    checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
    imgs_result_dir = 'my_dir/results/faster_rcnn_r50_fpn_1x_results/imgs'
    run_test(config_file, checkpoint_file, imgs_result_dir)



if __name__ == '__main__':
    main()
