# -*- coding: utf-8 -*-
import argparse
import os;
import shutil;
import os.path;
import logging


logging.basicConfig(filename='log_examp.log',level=logging.DEBUG)



def main():
    print ("print ======[1]MovePost start=====")
    print os.path.abspath(os.curdir)

    SourcePostPath = os.path.join(os.curdir,"source");

    MdPostPath = os.path.join(SourcePostPath,"MDPosts");
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



main()