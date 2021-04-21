### A batch conversion tool from ply to pcd using Python and Open3d

Version of open3d : 0.11.2

```
$ python main.py --pcl [existing path to the pcl directory] --pcd [(optional)save path to the pcd directory]
```

In the case where pcd directory is given:
```
|----- [path to the pcl directory]
|         |----- 0000.ply
|         |----- 0001.ply
|         |----- 0002.ply
|         ...
|----- [path to the pcd directory]
|         |----- 0000.pcd
|         |----- 0001.pcd
|         |----- 0002.pcd
|         ...
```

In the case where pcd directory is not given:
```
|----- [path to the pcl directory]
|         |----- 0000.ply
|         |----- 0000.pcd
|         |----- 0001.ply
|         |----- 0001.pcd
|         |----- 0002.ply
|         |----- 0002.pcd
|         ...
```
