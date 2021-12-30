from mmcv import Config
from tools.train import main as mmdet_train
import os
import shutil
import sys
import pandas as pd



def main():
    config_path = '/home/matanb/PycharmProjects/mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
    cfg=Config.fromfile(config_path)
    cfg['work-dir'] = './results'

    mmdet_train()
    print('Finish Train')

    if 0:
        pass
        # analyzer_script_path = 'tools/analysis_tools/analyze_logs.py'
        # plot_curve = [--keys ${KEYS}]
        # title = [--title ${TITLE}] [--legend ${LEGEND}] [--backend ${BACKEND}] [--style ${STYLE}] [--out ${OUT_FILE}]
        # # Compare the bbox mAP of two runs in the same figure.
        # tools/analysis_tools/analyze_logs.py plot_curve log1.json log2.json --keys bbox_mAP --legend run1 run2
        #
        # # Test Faster R-CNN and visualize the results, save images to the directory results/
        # tools/analysis_tools/analyze_results.py \
        #    configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py \
        #    result.pkl \
        #    results \
        #    --show
    if 0:
        pass
        # # If you want to filter the low score prediction results, you can specify the show-score-thr parameter
        #  tools/analysis_tools/analyze_results.py \
        #    configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py \
        #    result.pkl \
        #    results \
        #    --show-score-thr 0.3
        #
        # # analyzes COCO results per category and by different criterion. It can also make a plot to provide useful information.
        # tools / analysis_tools / coco_error_analysis.py ${RESULT} ${OUT_DIR}[-h][--ann ${ANN}] [--types ${TYPES[TYPES...]}]




if __name__ == "__main__":
    main()
