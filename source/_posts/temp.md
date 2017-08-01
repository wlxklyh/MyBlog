---
title: temp
date: {}
tags: null
published: false
---
# unity 问题

看网络上的问题 记录一下

<!-- more -->

## 1、协同程序 
一般用于控制运动 序列以及对象的行为

## 2、Unity3d中的碰撞器和触发器的区别？
碰撞器是触发器的载体，而触发器只是碰撞器身上的一个属性。
当Is Trigger=false时，碰撞器根据物理引擎引发碰撞，产生碰撞的效果，可以调用OnCollisionEnter/Stay/Exit函数；
当Is Trigger=true时，碰撞器被物理引擎所忽略，没有碰撞效果，可以调用OnTriggerEnter/Stay/Exit函数。


## 3、物体发生碰撞的必要条件
两个物体都必须带有碰撞器Collider，其中一个物体还必须带有Rigidbody刚体。


## 4、了解  动态欧拉角 造成万向锁的现象

## 5、生命周期
Awake->OnEnable->Start
http://www.jianshu.com/p/8c353abb42e4

## 6、点光源 聚光灯 平行光 区域光源

## 7、应用阶段 -> 几何阶段 -> 光栅化阶段
顶点着色器 几何着色器 

## 8、内存优化
1、压缩自带
2、暂时不用的以后还需要使用的物体 隐藏起来 
3、释放 AssetBundle 占用的资源
4、降低模型的片面数 降低模型的骨骼数量
5、是哟个 lod 使用 shader

## 9、动态加载资源的方法
1、 Resource.load
2、

## 10、物理更新适合放在 FixedUpdate

## 11、游戏场景中放置多个 Camera会可能到混合

## 12、有些有哪些动画类型
关节动画 骨骼动画  关键帧动画

## 13、diffuse 光照计算公式
diffuse = kd * colorlight * max(0,N*L)


## 14、两种阴影判断的方法和工作原理














