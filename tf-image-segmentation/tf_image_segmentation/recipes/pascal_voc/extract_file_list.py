import os
root = "/media/keti-ai/AI_HARD3/DataSets/BDD/segmentation/test/test/"
path ="/media/keti-ai/AI_HARD3/DataSets/BDD/segmentation/test/test/raw_images/"

(dir_path, dir_names, filenames) = next(os.walk(os.path.abspath(path)))

with open(os.path.join(root, "val.txt"), "w") as f:
    for filename in filenames:
        filename = filename.split(".")[0]
        f.write("".join([filename, "\n"]))