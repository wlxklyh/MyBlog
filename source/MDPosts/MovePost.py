# -*- coding: utf-8 -*-
import argparse
import os;
import shutil;
import os.path;
import logging


logging.basicConfig(filename='log_examp.log',level=logging.DEBUG)



def main():
    print ("print ======[1]MovePost start=====")
    logging.info("======[1]MovePost start=====\n")
    os.system("echo '===MovePost start'")
    # [0]参数处理===
    parser = argparse.ArgumentParser()
    args, unknown = parser.parse_known_args()

    parser.add_argument(
        "-p", "--path",
        default='G:\\WorkSpace\\GitSpace\\OtherGit\\GithubBlog', help="path")

    #args.path='G:\\WorkSpace\\GitSpace\\OtherGit\\GithubBlog'

    SourcePostPath = os.path.join(args.path,"source");

    MdPostPath = os.path.join(SourcePostPath, "MDPosts");
    _postsPath = os.path.join(SourcePostPath, "_posts");



    listDirs = os.walk(MdPostPath)
    for root, dirs, files in listDirs:
        for folderPath in dirs:
            folderAbsPath = os.path.join(root, folderPath)

            if ".idea" == folderPath:
                continue
            if "Img" == folderPath:
                continue
            MdFilePath = os.path.join(folderAbsPath, folderPath+".md");
            ImgFilePath = os.path.join(folderAbsPath, "Img");

            strCmd = 'hexo publish '+folderPath
            logging.info("run:"+strCmd+"\n")
            os.system(strCmd)

            targetMdFilePath = os.path.join(_postsPath, folderPath+".md");
            targetImgFilePath = os.path.join(_postsPath, folderPath);

            # logging.info("MdFilePath:"+MdFilePath)
            # logging.info("ImgFilePath:"+ImgFilePath)
            # logging.info("targetMdFilePath:"+targetMdFilePath)
            # logging.info("targetImgFilePath:"+targetImgFilePath)

            if  os.path.exists(targetImgFilePath):
                shutil.rmtree(targetImgFilePath)
            pass

            shutil.copyfile(MdFilePath, targetMdFilePath)
            shutil.copytree(ImgFilePath,targetImgFilePath)
# main()