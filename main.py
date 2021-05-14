import os
import argparse

import open3d as o3d
import pdb


def pcddir2plydir(src_dir,dst_dir):
    for pcdfile in os.listdir(src_dir):
        if  os.path.splitext(pcdfile)[1]==".pcd":
            ply_data = o3d.io.read_point_cloud(os.path.join(src_dir,pcdfile))
            plyfile=os.path.join(dst_dir,pcdfile.replace(".pcd",".ply"))
            o3d.io.write_point_cloud(plyfile,pcd_data)


    
def plydir2pcddir(src_dir,dst_dir):
    for plyfile in os.listdir(src_dir):
        if  os.path.splitext(plyfile)[1]==".ply":
            pcd_data = o3d.io.read_point_cloud(os.path.join(src_dir,plyfile))
            pcdfile=os.path.join(dst_dir,plyfile.replace(".ply",".pcd"))
            o3d.io.write_point_cloud(pcdfile,pcd_data)

        
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--ply', type = str, help = 'path to the ply directory')
    parser.add_argument('--pcd', type = str, help = 'path to the pcd directory')
    
    args = parser.parse_args()
    
    
    
    if args.ply!=None and  args.pcd!=None:
        print("Please set one of --ply and --pcd")
        
    
    elif args.ply:
        
        dst_dir=args.ply+"_pcd"
        print('Input dir: %s'%(args.ply))
        print('Output dir: %s'%(dst_dir))
        os.makedirs(dst_dir,exist_ok=True)
        plydir2pcddir(args.ply,dst_dir)
                
                
    elif args.pcd:
        
        dst_dir=args.ply+"_ply"
        print('Input dir: %s'%(args.pcd))
        print('Output dir: %s'%(args.pcd))
        os.makedirs(dst_dir,exist_ok=True)
        pcddir2plydir(args.pcd,dst_dir)
        

    else:
        print('No source directory set')   
        
        
        
        