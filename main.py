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
    parser.add_argument('--pcl', type = str, help = 'existing path to the pcl directory/file')
    parser.add_argument('--pcd', type = str, help = 'path to the pcd directory (optional)')
    args = parser.parse_args()
    
    if args.pcl:
        if args.pcd:
                print('All the pcl files in %s will be saved in %s as pcd'%(args.pcl,args.pcd))
                os.makedirs(args.pcd,exist_ok=True)
                pcldir2pcddir(args.pcl,args.pcd)
                
                
        else:
            print('All the pcl files in %s will be saved in the same directory as pcd'%(args.pcl))
            pcldir2pcddir(args.pcl,args.pcl)
            
        
    else:
        print('No source directory defined')   