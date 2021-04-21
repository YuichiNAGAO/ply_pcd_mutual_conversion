import os
import argparse

import open3d as o3d


    
    
def pcldir2pcddir(src_dir,dst_dir):
    for plyfile in os.listdir(src_dir):
        if  os.path.splitext(plyfile)[1]==".ply":
            pcd_data = o3d.io.read_point_cloud(os.path.join(src_dir,plyfile))
            pcdfile=os.path.join(dst_dir,plyfile.replace(".ply",".pcd"))
            o3d.io.write_point_cloud(pcdfile,pcd_data)
          
        
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type = str, help = 'existing path to the pcl directory/file')
    parser.add_argument('--dst', type = str, help = 'path to the pcd directory (optional)')
    args = parser.parse_args()
    
    if args.src:
        if args.dst:
                print('All the pcl files in %s will be saved in %s as pcd'%(args.src,args.dst))
                pcldir2pcddir(args.src,args.dst)
                os.makedirs(args.dst,exist_ok=True)
                
        else:
            print('All the pcl files in %s will be saved in the same directory as pcd'%(args.src))
            pcldir2pcddir(args.src,args.src)
            
        
    else:
        print('No source directory defined')   