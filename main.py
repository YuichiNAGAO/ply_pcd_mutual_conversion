import os
import argparse

import open3d as o3d


    
    
def plydir2pcddir(src_dir,dst_dir):
    for plyfile in os.listdir(src_dir):
        if  os.path.splitext(plyfile)[1]==".ply":
            pcd_data = o3d.io.read_point_cloud(os.path.join(src_dir,plyfile))
            pcdfile=os.path.join(dst_dir,plyfile.replace(".ply",".pcd"))
            o3d.io.write_point_cloud(pcdfile,pcd_data)

        
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--ply', type = str, help = 'existing path to the ply directory/file')
    parser.add_argument('--pcd', type = str, help = 'path to the pcd directory (optional)')
    args = parser.parse_args()
    
    if args.ply:
        if args.pcd:
                print('All the ply files in %s will be saved in %s as pcd'%(args.ply,args.pcd))
                os.makedirs(args.pcd,exist_ok=True)
                plydir2pcddir(args.ply,args.pcd)
                
                
        else:
            print('All the ply files in %s will be saved in the same directory as pcd'%(args.ply))
            plydir2pcddir(args.ply,args.ply)
            
        
    else:
        print('No source directory defined')   
