from mmdet.apis import init_detector, inference_detector
#mim download mmdet --config yolov3_mobilenetv2_320_300e_coco --dest .
config_file = '../../configs/yolo/yolov3_mobilenetv2_320_300e_coco.py'
checkpoint_file = '../../checkpoints/yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth'
model = init_detector(config_file, checkpoint_file, device='cpu')  # or device='cuda:0'
# inference_detector(model, '../../demo/demo.jpg')

img = '../../demo/demo.jpg'  # or img = mmcv.imread(img), which will only load it once

# inference_detector(model, img)
result = inference_detector(model, img)
# visualize the results in a new window
# model.show_result(img, result)
# or save the visualization results to image files
model.show_result(img, result, out_file='../results/result.jpg')
