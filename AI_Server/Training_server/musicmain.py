import Cluster as cl
import numpy as np
import LowLevelFeature as llf
import os
import collections

def extractLLF():
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/data"
    music_path1 = dir_path + "/Em-Gai-Mua-Huong-Tram.mp3"
    music_path2 = dir_path + "/Ngay-Mai-Em-Di-Touliver-Mix-Touliver-Le-Hieu-Soobin-Hoang-Son.mp3"
    music_path3 = dir_path + "/Hon-Anh-MIN.mp3"

    ms = llf.LowLevelMusic(music_path1)
    f = ms.extract_features()

    # ms1 = llf.LowLevelMusic(music_path2)
    # f1 = ms1.extract_features()
    #
    # ms2 = llf.LowLevelMusic(music_path3)
    # f2 = ms2.extract_features()

    # shape n_sample*n_feature
    X = []
    X.append(f)
    # X.append(f1)
    # X.append(f2)
    return np.array(X)

def cluster():
    X = extractLLF()
    print X
    # X = [[1.1, 1.2],
    #      [2.2, 2.5],
    #      [3.3, 3.6],
    #      [2.4, 2.7],
    #      [14.1, 3.2],
    #      [4.12, 15.2],
    #      [3.14, 3.6],
    #      [2.4, 13.7],
    #      [3.1, 3.2],
    #      [4.1, 4.2],
    #      [13.1, 13.2],
    #      [4.11, 14.2],
    #      [5.1, 15.2]]
    # km = cl.Cluster(2)
    # km.fit(X)
    # x = km.centroid()

def get_music():
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/data"
    music_path = dir_path + "/Em-Gai-Mua-Huong-Tram.mp3"
    music_json = collections.OrderedDict()
    music_json['id'] = 0
    music_json['music_path'] = music_path
    return music_json
if __name__ == "__main__":
    # cluster()
    print ""