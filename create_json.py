# 合并json文件，并得到标准的json格式：
import json
import cv2
import os
file_path = r'E:\python\mmdetection\val_zjy'

# 生成json的字典
result_json = {
    "info": "spytensor created",
    "license": "license",
    "images": [],
    "annotations": [],
    "categories": []
}
# 添加images的键值：
img_id = 0
anno_id = 0
for file in os.listdir(file_path):
    if file[-4:] == '.jpg':
        img = cv2.imread(file_path + "\\" + file)
        img_h, img_w, _ = img.shape
        result_json["images"].append({"height": img_h, "weight": img_w, "id": img_id, "file_name": file})
        img_id += 1

    # 添加annotations的键值：
    if file[-4:] == 'json':
        with open(file_path + "\\" + file, 'r', encoding='UTF-8') as f:
            annotations = json.load(f)
        if not annotations['outputs'] == {}:
            for anno in annotations['outputs']['object']:
                x_min = anno['bndbox']['xmin']
                x_max = anno['bndbox']['xmax']
                y_min = anno['bndbox']['ymin']
                y_max = anno['bndbox']['ymax']
                w = int(x_max - x_min)
                h = int(y_max - y_min)
                result_json["annotations"].append({"id": anno_id, "image_id": img_id, "category_id": file[:file.index("_")],
                                                   "bbox": [x_min, y_min, w, h], "iscrowd": 0, "area": w*h})
                anno_id += 1

# categories:
CLASSES = ('bingdundun', 'Sanyo', 'Eifini', 'PSALTER', 'Beaster', 'ON',
           'BYREDO', 'Ubras', 'Eternelle', 'PERFECT DIARY', 'huaxizi',
           'Clarins', 'L occitane', 'Versace', 'Mizuno', 'Lining', 'DOUBLE STAR',
           'YONEX', 'Tory Burch', 'Gucci', 'Louis Vuitton', 'CARTELO',
           'JORDAN', 'KENZO', 'UNDEFEATED', 'BOY LONDON', 'TREYO', 'carhartt',
           'jierou', 'Blancpain', 'GXG', 'leding', 'Diadora',
           'TUCANO', 'Loewe', 'Granite Gear', 'DESCENTE',
           'OSPREY', 'Swatch', 'erke', 'Massimo Dutti', 'PINKO', 'PALLADIUM',
           'origins', 'Trendiano', 'yiner', 'Monster Guardians', 'fuerjia', 'IPSA',
           'Schwarzkopf')
cls_id = 1
for cls in CLASSES:
    result_json["categories"].append({"id": cls_id, "name": CLASSES[cls_id-1]})
    cls_id += 1

# 保存json
with open(file_path + '\\' + 'instances_val_zjy_2017.json', 'w') as f:
    f.write(json.dumps(result_json, indent=1))











