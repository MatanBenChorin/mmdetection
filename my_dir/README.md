
## Introduction

MMDetection is an open source object detection toolbox based on PyTorch. It is
a part of the OpenMMLab project.

The master branch works with **PyTorch 1.5+**.

<details open>
<summary>Major features</summary>

- **Modular Design**

  We decompose the detection framework into different components and one can easily construct a customized object detection framework by combining different modules.

- **Support of multiple frameworks out of box**

  The toolbox directly supports popular and contemporary detection frameworks, *e.g.* Faster RCNN, Mask RCNN, RetinaNet, etc.

- **High efficiency**

  All basic bbox and mask operations run on GPUs. The training speed is faster than or comparable to other codebases, including [Detectron2  maskrcnn-benchmarkand SimpleDet.

- **State of the art**

  The toolbox stems from the codebase developed by the *MMDet* team, who won COCO Detection Challenge detection-leaderboard) in 2018, and we keep pushing it forward.

</details>

Apart from MMDetection, we also released a library mmcv for computer vision research, which is heavily depended on by this toolbox.


## Recommended tutorials 

We recommend the following tutorials for getting started: 
- [colab tutorial](demo/MMDet_Tutorial.ipynb) 
- [instance segmentation colab tutorial](demo/MMDet_InstanceSeg_Tutorial.ipynb)
- [with existing dataset](docs/en/1_exist_data_model.md)
- [with new dataset](docs/en/2_new_data_model.md)
- [with existing dataset_new_model](docs/en/3_exist_data_new_model.md)
- [learn about configs](docs/en/tutorials/config.md)
- [customize_datasets](docs/en/tutorials/customize_dataset.md)
- [customize data pipelines](docs/en/tutorials/data_pipeline.md)
- [customize_models](docs/en/tutorials/customize_models.md)
- [customize runtime settings](docs/en/tutorials/customize_runtime.md)
- [customize_losses](docs/en/tutorials/customize_losses.md)
- [finetuning models](docs/en/tutorials/finetune.md)
- [weight initialization](docs/en/tutorials/init_cfg.md)
- [how to xxx](docs/en/tutorials/how_to.md)
- [test Results Submission](docs/en/tutorials/test_results_submission.md)
- [useful_hooks](docs/en/tutorials/useful_hooks.md)

More advanced:
- [Benchmark and Model Zoo](docs/en/model_zoo.md)
- [export a model to ONNX](docs/en/tutorials/pytorch2onnx.md)
- [export ONNX to TRT](docs/en/tutorials/onnx2tensorrt.md)

Useful Tools and Scripts in the following topics:
- Log Analysis
-  Result Analysis
-  Visualization
-  Error Analysis
-  Model Serving
-  Model Complexity
-  Model conversion
-  Dataset Conversion
-  Dataset Download
-  Benchmark
-  Miscellaneous
-  Hyper-parameter Optimization
-  Confusion Matrix

  can be found at: [useful tools](docs/en/useful_tools.md)
