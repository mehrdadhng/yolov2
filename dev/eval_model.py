import sys
sys.path.append('./cocoapi/PythonAPI')

import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import skimage.io as io
import pylab


def get_mAPs():
    annType = 'bbox'
    prefix = 'instances'
    dataDir = 'cocoapi'
    dataType = 'val2017'
    annFile = '%s/annotations/%s_%s.json' % (dataDir, prefix, dataType)
    resFile = '%s/results/results.json' % dataDir
    cocoGt = COCO(annFile)
    cocoDt = cocoGt.loadRes(resFile)

    imgIds=sorted(cocoGt.getImgIds())
    imgIds = imgIds[0:50]
    cocoEval = COCOeval(cocoGt,cocoDt,annType)
    cocoEval.params.imgIds  = imgIds
    cocoEval.evaluate()
    cocoEval.accumulate()
    cocoEval.summarize()


if __name__ == "__main__":
    get_mAPs()