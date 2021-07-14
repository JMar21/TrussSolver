import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Solves a truss')
    parser.add_argument('--scale', help='scale applied to geom',default=2, type=float)
    parser.add_argument('--disp-scale',help='scale applied to disp', default=500, type=float)
    parser.add_argument('--load-scale',help='scale applied to loads',default =0.02, type=float)
    parser.add_argument('--no-draw-original', help='Should draw OG geom', action='store_true')
    return parser.parse_args()