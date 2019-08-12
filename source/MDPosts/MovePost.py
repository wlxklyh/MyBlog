# -*- coding: utf-8 -*-
import argparse
import os;
import shutil;
import os.path;

def main():

    print("======[1]MovePost start=====")

    # [0]参数处理===
    parser = argparse.ArgumentParser()
    args, unknown = parser.parse_known_args()

    parser.add_argument(
        "-p", "--path",
        default='G:\\WorkSpace\\GitSpace\\OtherGit\\GithubBlog', help="path")

    SourcePostPath = os.path.join(args.path,"source");

    MdPostPath = os.path.join(SourcePostPath, "MDPosts");
    _postsPath = os.path.join(SourcePostPath, "_posts");



    listDirs = os.walk(MdPostPath)
    for root, dirs, files in listDirs:
        for folderPath in dirs:
            folderAbsPath = os.path.join(root, folderPath)
            print(folderPath)
            if ".idea" == folderPath:
                continue
            if "Img" == folderPath:
                continue
            MdFilePath = os.path.join(folderAbsPath, folderPath+".md");
            ImgFilePath = os.path.join(folderAbsPath, "Img");

            strCmd = 'hexo publish '+folderPath
            print("run:"+strCmd)
            os.system(strCmd)

            targetMdFilePath = os.path.join(_postsPath, folderPath+".md");
            targetImgFilePath = os.path.join(_postsPath, folderPath);

            print("MdFilePath:"+MdFilePath)
            print("ImgFilePath:"+ImgFilePath)
            print("targetMdFilePath:"+targetMdFilePath)
            print("targetImgFilePath:"+targetImgFilePath)

            if  os.path.exists(targetImgFilePath):
                shutil.rmtree(targetImgFilePath)
            pass

            shutil.copyfile(MdFilePath, targetMdFilePath)
            shutil.copytree(ImgFilePath,targetImgFilePath)

main()