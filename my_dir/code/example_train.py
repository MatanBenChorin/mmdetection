"""
python tools/train.py \
    configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py \
    checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth \
    --show-dir my_dir/results/faster_rcnn_r50_fpn_1x_results
"""

import tools.train as train
import sys
import os


def run_train(config_file, checkpoint_file, imgs_result_dir, score_thresh=None, flag_deubg_show=False, result_file=None,
             eval_metrics=None):
    os.chdir("../../")
    sys.argv.append(config_file)  # CONFIG_FILE
    sys.argv.append(checkpoint_file)  # CHECKPOINT_FILE
    if (flag_deubg_show != False):
        sys.argv.append(
            "--show")  # detection results will be plotted on the images and shown in a new window. used for debugging and visualization please comment --show-dir
    else:
        sys.argv.append("--show-dir=" + imgs_result_dir)
    if (score_thresh != None):
        sys.argv.append("--show-score-thr=" + str(
            score_thresh))  # detection results will be plotted on the images and shown in a new window. used for debugging and visualization please comment --show-dir
    if (result_file != None):
        sys.argv.append("--out=" + result_file)
    if (eval_metrics != None):
        sys.argv.append("--eval=" + eval_metrics)

    train.main()


def main():
    # genuine_coco()
    slim_coco()


def genuine_coco():
    config_file = 'configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
    checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
    imgs_result_dir = 'my_dir/results/faster_rcnn_r50_fpn_1x_results/imgs'
    run_train(config_file, checkpoint_file, imgs_result_dir, flag_deubg_show=False)


def slim_coco():
    config_file = 'my_dir/my_configs/faster_rcnn_r50_fpn_1x_coco_slim.py'
    checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
    imgs_result_dir = 'my_dir/results/faster_rcnn_r50_fpn_1x_results/imgs'
    result_file = 'my_dir/results/faster_rcnn_r50_fpn_1x_results/result_file/results.pkl'
    flag_deubg_show = False
    score_thresh = 0.5
    eval_metrics = 'bbox'
    run_train(config_file, checkpoint_file, imgs_result_dir, score_thresh=score_thresh, flag_deubg_show=flag_deubg_show,
             result_file=result_file, eval_metrics=eval_metrics)


if __name__ == '__main__':
    main()
