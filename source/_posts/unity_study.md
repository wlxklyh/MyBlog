---
title: Unity安装->入门->工程学习->shader
date: 2017-07-30 12:49:39
tags:
---



## 总体的思维导图
通过下面一张图，大概的知道一个学习的方向和流程。对于这篇文章讲的是第一个部分，入门，初次接触unity。
![Alt text](./1496577433020.png)
<!−− more −−>



## 一、安装
#### 1、安装教程（windows）
mac就比较简单 官网下载dmg就可以安装使用了
我用下面图中的两个文件完成安装，一个是安装文件（4.7），一个是破解，然后根据下面链接完成安装
![Alt text](./1496577678948.png)

http://jingyan.baidu.com/article/90895e0f959c7564ec6b0bfb.html

#### 2、需要的文件（百度网盘分享）

http://pan.baidu.com/s/1slFHeFz

- 分享的文件里的东西有：
	- 【安装使用】：Unity 4.7.1安装文件
	- 【安装使用】：Unity 4.x pro Patch.exe
	- 【入门使用】：《unity4.x从入门到精通》
	- 【入门使用】：简单的工程（微信飞机游戏）：
	- 【进一步了解使用】：RPG游戏的简单的工程
	- 【shader学习使用】：《Unity Shader入门精要》
	- 
#### 3、安装结果
使用a.Unity 4.7.1安装文件 b.Unity 4.x pro Patch.exe  然后用上上面的教程链接就可以完成windows unity的安装  打开如下：
![Alt text](./1496583208861.png)



## 二、入门学习：
#### 1、开始我找了本书看《unity4.x从入门到精通》：
《unity4.x从入门到精通》
http://pan.baidu.com/s/1slFHeFz

#### 2、《unity4.x从入门到精通》读书的记录：
##### 第一章 （可跳过）
第一章 没什么干货 可以直接跳过

##### 第二章  （重点看2.1  2.2+实操一下）
- 刚接触的unity的可以按照第二章说的去操作一下  感受一下unity的一些功能 想贪快的就看**2.1** 、**2.2**部分即可 后面的用到再查阅
- 快捷键部分 等到基本入门了 再来看一遍 会比较受用的感觉  

##### 第三章 （粗略看）
- 第三章看下 不用纠那么细致 
##### 第四章 （重点看+操作）
- 第四章书讲的是怎么写代码的 看完第四章就会输出hello world
##### 截取两张图
![Alt text](./1490002232972.png)
![Alt text](./1490002240157.png)



##### 后面5-17章的当作工具书看

12章 到16  是针对开发的介绍

17章 进阶 ： 网络


#### 3、大致的浏览了《unity4.x从入门到精通》 前四章之后带着几个疑问去分类学习：
##### 3.1、C#代码跟unity怎么关联起来？  书中13章![Alt text](./1491552037983.png)
###### 1、C#脚本的规则
（1）凡事需要添加到游戏对象的C#脚本类都是需要直接或者间接的继承 MonoBehaviour 如果在unity添加脚本 unity会自动填充继承MonoBehaviour的代码  如果是自己新建一个文件 然后在unity从拖拽添加component 这样是不会成功的（后面会说unity怎么添加C#文件）

（2）继承了MonoBehaviour的类 都会有Start 和 Awake函数的继承  一般使用Start和Awake来初始化  不使用构造函数的原因是unity中无法确定构造函数的顺序。这里我觉得有个原因是：unity会把所有绑定在对象身上的类实例化  然后才可以GetComponent()  例如：下面的操作如果在构造函数中做 可能PlayerAttack这个没有实例化 那么获取不到  所以把初始化工作放在Start中
![Alt text](./1491552515808.png)

（3）类名和脚本文件名相同 

（4）协同函数Coroutines 返回类型必须是Ienumerator

（5）C#不支持自定义命名空间

###### 2、C#脚本在unity编辑器中关联对象（十三章有详细介绍）
1、创建脚本的方法：
![Alt text](./1491553048549.png)

2、创建完之后的编辑：
这里可以修改用MonoDevelop的编辑器 或者用Vs2012作为代码编辑
![Alt text](./1491553152505.png)

3、关联到对象去
（3.1）添加一个gameobject 
![Alt text](./1491553612376.png)
（3.2） 然后给gameObject添加脚本
![Alt text](./1491553537327.png)![Alt text](./1491553548688.png)

在Unity中，继承MonoBehaviour的C#脚本都被看作一个Component 游戏对象可以理解为一个容纳各种类型component的容器 游戏对象的所有component一起决定了这个对象的行为表现 这个对象被添加到scene中之后 然后点击build and run 之后这个脚本的Start函数就会被调用一起  可以在这里输出 hello world  这就算是unity的hello world


###### 3、怎么获取别的对象以及他的component
使用函数 GameObject.Find  null则是找不到  根据类名
使用函数GameObject.FindWithTag
还有在unity编辑器中拖拽

查看数组的表13-6 表13-7  表13-8  表13-9 

![Alt text](./1491555497064.png)
![Alt text](./1491555396564.png)
![Alt text](./1491555581945.png)
![Alt text](./1491555622726.png)
![Alt text](./1491555636221.png)



## 三、工程学习：
看了《unity4.x从入门到精通》 简单操作unity之后 我上网找几个简单的游戏demo来看下，这样我觉得会比较快上手。
### 1、微信飞机大战
工程下载地址：
http://pan.baidu.com/s/1slFHeFz （网上找的工程）
这个比较容易看懂   

下面说明的过程：
（1）背景移动 -->（2）敌机出生-->（3）自己的飞行
![背景移动](./ply1.gif)==》 ![敌机出生](./ply2.gif)==》 ![自己的飞行](./ply3.gif)





#### 1、初看这个工程
只有一个场景scene
![Alt text](./1496655674282.png)
预制体有这些
![Alt text](./1496663793026.png)
脚本是这些
![Alt text](./1496663193818.png)
#### 2、分几个部分看
##### 2.1、scene
![Alt text](./1496664667730.png)
1.里面有个 Main Camera 点击它然后看导航栏Inspector
2.Main Camera里面有一些component组件 其中Camera 去修改size view port然后运行看下结果 
![Alt text](./1496664752184.png)
3.除了Main Camera 这个Scene里面还有一些飞机（hero） 背景（bg） 还一些不是UI的东西（bombManager）

上面大概的了解到，在这个Scene里面拖拽了一些物件 还有一个摄像机 把这些物件投影到屏幕中，到目前为止，我们大概知道是怎么得到游戏的静态界面的，但是游戏是怎么动起来的还不知道。接下来脚本就是讲怎么动起来的。


##### 2.2、脚本
1. 代码入口，没有一个明确的Main函数入口  
下面按照顺序说下（1）背景移动 （2）怎么生成敌机  （3）怎么控制自己的战机
![Alt text](./1496665501144.png)
（1）背景移动 
scene里面有个object叫bg 然后再点击其中一个background查看导航栏 
可以看到每个background都挂在了一个脚本组件 BackgroundTransform.cs  这个脚本就是控制不背景移动的
![Alt text](./1497515757683.png)
![Alt text](./1497515795595.png)

看到BackgroundTransform这个脚本 两个背景来控制屏幕的背景交替向下移动
```
public class BackgroundTransform : MonoBehaviour {
	public static float moveSpeed = 2f;
	
	// Update is called once per frame
	void Update () {
		this.transform.Translate( Vector3.down * moveSpeed * Time.deltaTime );
		Vector3 postion = this.transform.position;
		if(postion.y<=-8.52f){
			//有两个背景在交替滚动  如果有一个滚动到屏幕外面则改动显示
			this.transform.position = new Vector3(postion.x,postion.y+8.52f*2,postion.z );
		}
	}
}
```

（2）怎么生成敌机
scene里面有个叫spawn的东西  这个spawn十个空object 里面挂了一个spawn.cs脚本组件
![Alt text](./1497516506138.png)
【代码如下】：
![Alt text](./1497516724024.png)


地机的行为就看模型上面挂的脚本组件Enemy.cs


（3）怎么控制自己的战机
同样的在hero这个上面挂了Hero.cs的脚本组件  然后具体就看里面的代码
![Alt text](./1497516894694.png)




### 2、RPG游戏
然后再找个复杂点的游戏工程来看
#### 1、初看工程 
- 工程下载地址：
http://pan.baidu.com/s/1slFHeFz（网上找的工程）
- 工程的脚本目录
![Alt text](./1491550201008.png)

#### 2、工程代码查看
**看下怎么把这个人物控制方向运动起来的**
![Alt text](./rpg.gif)

1.打开03_play这个scene 然后拖拽一个Magician模型到scene中
先在Prefabs文件夹中找到Magician看模型有什么挂件
- Magician挂了Character Controller这个控制组件
这个是角色控制器 可以对角色做移动的操作 在playermove脚本里面用到

- Magician还挂了PlayerDir PlayerMove  PlayerAnimation PlayerState PlayerAttack等脚本来实现模型的行为
看下PlayerMove的update函数
![Alt text](./1491550243585.png)
这里判断如果距离大于0.3f则会移动


从Magician引发的问题：

##### 2.1、移动的时候有个targetPosition 这个是怎么来的？
targetPosition 是PlayerDir.cs这个里面的成员
PlayerDir.cs里面会计算鼠标点击屏幕的位置发出的射线的碰撞结果 如果是地面那么修改这个玩家的朝向 
![Alt text](./1497532344804.png)


##### 2.2、又引发一个问题鼠标怎么会变样？
我们看到03_play这个scene有个object叫GameSetting 这个是一个纯粹为了挂脚本用的object 
![Alt text](./1497531965474.png)
我们看到这个CursorManager就是我们在游戏中的鼠标的管理类

##### 2.3、模型怎么会动起来呢？
打开03_play这个scene 然后拖拽一个Magician模型到scene中 然后在菜单栏window animation打开animation窗口 然后可以选择已经做好的动作 attack1 然后点击播放 现在我们知道动作可以预先做好 然后再代码中调用 我们看下代码是怎么调用的 
![Alt text](./1497533865288.png)
PlayerAnimation.cs这个脚本 根据一个状态去 播放动画animation.CrossFade(animName);

```
// Update is called once per frame
	void LateUpdate () {
        if (attack.state == PlayerState.ControlWalk) {
            if (move.state == ControlWalkState.Moving) {
                PlayAnim("Run");
            } else if (move.state == ControlWalkState.Idle) {
                PlayAnim("Idle");
            }
        } else if (attack.state == PlayerState.NormalAttack) {
            if (attack.attack_state == AttackState.Moving) {
                PlayAnim("Run");
            }
        }
	}
	void PlayAnim(string animName) {
        animation.CrossFade(animName);
    }
```

这个项目的运行
![Alt text](./1491877171720.png)
![Alt text](./1491877201762.png)

之后看下怎么改改这个项目  不懂的再google 或者再去细看unity的一些用法 或则C#的用法



## 四、Unity Shader学习

### A、我学习的三个点
-----------------
#### 1.下载源码中源码下载：
https://github.com/candycat1992/Unity_Shaders_Book

#### 2.学习hello world!
**下面gif是unity shader的hello world!**
![Alt text](./shader2.gif)

#### 3.看书照着源码学习 然后实践





 
  
   
   


### B、学习随便记录的笔记 
-----------------
#### 1.第一章


#### 2.第二章 渲染流水线
应用阶段->几何阶段->光栅化阶段
应用阶段把渲染图元交给几何阶段

##### 2.2CPU 和 GPU 的通信
1. 把数据加载到显存中
2. 设置渲染状态
3. 调用 drallcall

**1.把数据加载到显存中**
硬盘--->内存--->显存
顶点数据 法线方向 纹理坐标

**2.设置渲染状态**
vs ps
顶点着色器 片元着色器

**3.drawcall**

##### 2.3GPU 流水线
###### 顶点着色器
把顶点坐标转换到齐次裁剪坐标系得到归一化的设备坐标 NDC
opengl unity的 NDC 是-1 1
屏幕映射 转换到屏幕坐标系
屏幕坐标系Opengl 是左下角

#### 3.第三章 Unity shader基础
##### 3.1 创建shader的常见流程
1. 创建一个材质
2. 创建一个unity shader 并把它赋给上一步中创建的材质
3. 把材质赋给要渲染的对象
4. 在材质面板上（选中材质然后查看导航栏）调整shader的属性


##### 3.2 shader lab
GLSL是opengl的shader语言 Directx的shader语言是HLSL   shader lab的就是 unity shader的shader语言
可以细看下这个章节  熟悉下语法

#### 4 学习 Shader 所需的数学知识
一些基础的知识都是大概知道 可以等到要用到的时候再去复习
一些空间 M 模型空间 W 世界空间 V 摄像机空间 NDC 归一化空间


#### 5 开始学习 Shader
##### 5.2 最简单的片元着色器 顶点着色器
###### 5.2.2 unity支持的语义：
POSITION，TANGENT，NORMAL，TEXCOORD0，TEXCOORD1，COLOR
###### 5.2.3 顶点着色器和片元着色器之间的通信：
声明一个新的结构体v2f v2f可用于定点着色器和片元着色器之间传递信息
###### 5.3.1内置包含的文件
在后面的学习中 总是会用到一些内置的文件
需要include一下 类似C++的include

##### 5.5 Debug技巧
1. 把想知道的值赋值到某个颜色 通过屏幕上显示的颜色来判断一个值
2. 还可以找到一个简单的取色脚本  ColorPicker.cs
3. 高级的：Visual Studio Graphics Debugger
4. Unity里面的帧调试器


#### 6 Unity 中的基础光照
##### 6.2 进入摄像机的光分成4个部分
- 自发光：本身辐射量  如果没有全局光照技术 自会影响自己的辐射量
- 高光反射：（我觉得是完全镜面反射）光源的完全镜面反射方向散射多少辐射量？？ 是镜面反射的散射？？
- 漫反射：这个就是光源的漫反射
- 环境光：其他所有的间接光照

计算高光反射：![Alt text](./1495002356532.png)
Phong 模型来计算高光反射部分：
![Alt text](./1495002389507.png)


##### 6.4 光照实现
（1）Properties定义一个颜色值 
（2）LightMode标签是 Pass 标签的一种 只有定义了正确的 LightMode 我们才能得到一些 Unity的内置光照变量 
Tags { "LightMode"="ForwardBase" }

（3）还是之前的 CGPROGRAM ENDCG

（4）为了用到 Unity的内置变量  
''' #include "Lighting.cginc"  "'

（5）逐顶点 着色器

- 逐顶点漫反射：有锯齿 应该是因为处理是每个片元的顶点 所以不精细
- 逐像素漫反射：无锯齿 但是黑面太黑 都是一个色 黑色
- 半伯兰特模型：无锯齿 黑面有渐变
 c = c * m (0.5 (n * I) + 0.5)
#### 7 基础纹理
- 记住这个 ： o.uv = v.texcoord.xy * _MainTex_ST.xy + _MainTex_ST.zw;
###### 7.1.2 纹理取样
fixed3 albedo = tex2D(_MainTex, i.uv).rgb * _Color.rgb;

###### 7.2 凹凸映射
不改变顶点 改变的是绘制 
法线纹理 normal map

###### 7.2.1高度纹理
存储的是强度值   这个通过高度来计算法线 
颜色越浅越突 反而凹

###### 7.2.2法线纹理

法线的向量分量是 -1 到1 
所以 pixel = (noamal+1)/2
normal = (pixel * 2) - 1

这种纹理称为是模型空间的法线纹理  我恩会采用另外一种坐标空间 切线空间  我们用模型顶点的切线空间来存储法线  对于每个顶点都有一个属于自己的切线空间 这个切线空间的原点就是该顶点本身 z 轴就是顶点的法线 x 轴是顶点的切线方向

我们的法线纹理 存储的是 法线在各自的切线空间的向量 大部分都是浅蓝色的原因是 0 0 1映射到0 1就是0.5 0.5 1（浅蓝色） 0 0 1就是 z 轴  大部分的法线都是跟切线空间的 z 轴同方向

一种是模型空间下的法线纹理 一种是切线空间下的法线纹理

模型空间存储的优点：
- 实现简单 直观。生成简单
- 提供平滑的边界 模型空间可以生成平滑

切线空间优点：
- 自由度高 模型空间的是绝对法线信息  应用到不同网格都有合理的效果
- 可进行 UV 动画 我们通过移动一个纹理的 UV 坐标来实现凹凸移动的效果
- 可压缩  只此处 xy  z 可以推倒得到 

######  7.2.3 实践
- 一种在切线空间下进行光照计算 把光照方向、视角方向变换到切线空间下 ：效率比较高  在顶点着色器可以完成 光照和视角的转换  第二种要堆法线纹理取样 需要在片元着色器中变换 我觉得应该是片元的数量大于顶点的数量所以转换需要很多 
有时我们要在世界空间下进行一些计算 例如在 Cubemap进行环境映射 需要使用世界空间下进行一些计算 （这个 cubemap 不知讲啥）
- 另外一种是在世界坐标空间下进行光照计算 我们要把切线空间下的法线防线转换到世界空间下：


1. 在切线空间下计算
思路：在片元着色器中得到纹理采样的切线空间下的法线 然后再与切线空间下的视角方向 光照方向进行计算
注：float4 texcoord : TEXCOORD0; 传入的是float4 xy 是原因的纹理 UV zw 是法线纹理 uv

######  7.2.4 unity 法线纹理类型
法线纹理会根据平台被压缩
使用 unpackNormal 函数取解压
普通纹理的话 是4个通道都是不能舍弃  如果是法线纹理 那么只有ag 是需呀的 br 是不需要的 用 DXT5nm 可以升内存空间。
Create from Grayscale 是凹凸映射的方法 高度图 

##### 7.3渐变纹理
##### 7.4遮罩纹理
使用其中某个（或者几个）通道做乘法 如果通道为0 可以保证表面不受该属性影响 

#### 8透明效果
unity 先渲染 Background 然后渲染 Geometry 大多数的不透明物体 前面都是开启深度测试和深度写入   之后渲染 AlphaTest 这个是透明物体  需要排序 从远到近 然后进行渲染


##### 8.3透明度测试
用一个阀值决定

##### 8.4透明度混合
Blend 内置的混合模式命令 
Blend off 关闭混合
Blend SrcFactor DstFactor
srccolor * SrcFactor + dstcolor * DstFactor = Target

###### 8.6.1 混合等式和参数
现在有 源颜色 S 和目标颜色 D 现在想要得到输出颜色 O 就必须使用一个等式来计算，这个就是混合等式 
我们会用两个混合等式  一个用于混合 RGB 一个混合 A 通道 每个等式要两个因子   一共四个因子。



中级篇
####9 更复杂的光照
Forward Rendering Path、Deferred Rendering Path Vertext Lit Rendering Path

顶点照明渲染路径：是对硬件配置要求最好  运算性能最高的

跳过。。。

#### 10 高级纹理

##### 10.1立方体纹理 
立方体纹理是环境映射的一种实现方法
包含6张图像  采样的时候是用三维的坐标 

使用立方体纹理的好处 实现简单快捷 得到的效果好  缺点是 如果当场景引入了新的物体 光源 或者物体在发生移动时 我们就需要重新生成 立方体纹理  可以反射环境  但不能反射自己  


###### 10.1.1 天空盒子
windows -lighting 里面设置 skybox

###### 10.1.2折射
折射 是用光照计算函数 然后用折射函数混合反射光



##### 10.2渲染纹理 



##### 10.2程序纹理 



#### 11 让画面动起来

##### 11.1 unity shader 中的内置变量
_Time float4 场景加载开始所经过的实际
_SinTime 正弦值
_CosTime 余弦值
unity_DeltaTime 

##### 11.2 纹理动画
- 序列帧动画：记住 UV 纹理坐标是左下角是原点
- 滚动的背景：修改 UV 纹理坐标 对两张纹理取样 然后混合


