import os

proj_path = os.path.realpath(__file__).split('lib')[0]
config_path = proj_path  + "config/"

def get_sub_dirs(dir):
    sub_dir_list = []
    if os.path.exists(dir):
        subdirs = os.listdir(dir)
        for item in subdirs:
            if os.path.isdir(dir + "/" + item):
                sub_dir_list.append(item)

    return sub_dir_list



# if __name__ == "__main__":
#     print get_sub_dirs(proj_path+"/script/api_test")


