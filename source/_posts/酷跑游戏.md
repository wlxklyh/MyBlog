---
title: 酷跑游戏
date: 2017-08-16 08:49:39
tags: unity
reward: true
---


## 一、对这个项目的初步认识：
### 1、游戏跑起来是怎么样的：
![Alt text](./demo.gif)

<!-- more -->



### 2、怎么打开这个工程
#### 2.1工程下载：
【附】：项目下载资料为网络搜集所得，仅供学习研究，严谨用于商业行为，请下载后于24小时之内删除。

链接: http://pan.baidu.com/s/1bp5yiSn 密码: 6t4e

#### 2.2怎么打开这个工程
##### 1、安装unity （mac上面打开会有问题 我在windows unity 4.7版本打开）:
安装教程见我的博客：
https://wlxklyh.github.io/2017/07/30/unity_study/

##### 2、新建一个工程  然后双击下载到的unitypackage就会导入 之后打开MainScene 然后点击运行即可 


### 3、工程代码的结构
![Alt text](./1502367185977.png)


### 4、工程代码的入口
![Alt text](./1502419665363.png)
看到Game这个object挂载了很多的脚本组件
![Alt text](./1502421000610.png)
我们接下来会看这些代码，从名字来看 重点看GameManager DataManager Mission Manager GUIManager

### 5、第三方库
UI用了NGUI
![Alt text](./1502589425321.png)

## 二、阅读代码

### 1、先看GameManager
这个是游戏管理的类，从这里开始阅读，


### 2、AudioManager音效管理
音效的配置都在Unity编辑器里面配置这些音乐  见图片
（看MainScene里面Game这个对象 里面挂载一个脚本组件AudioManager）
![Alt text](./1502587224424.png)
这个类比较脚本 提供两个接口给外部调用
playBackgroundMusic 播放背景音乐
playSoundEffect	播放音效 这里用枚举列出了几种音效

### 3、CoinGUICollection硬币收集管理的类


### 4、DataManager数据管理
Unity提供PlayerPrefs存储玩家的数据  

### 5、GUIClickEventReceiver 点击事件的接收
首先我们先看下项目是怎么实现事件点击的 然后看下其他的方法 然后稍微知道NGUI怎么实现点击的
#### 5.1. 项目中响应点击
1.这里用到了一个脚本叫做 GUIClickEventReceiver  然后项目中的所有button都挂载了这个脚本.
![Alt text](./1502589610210.png)![Alt text](./1502589637210.png)
2.NGUI的Button被点击了会响应这个Button挂载的脚本的OnClick函数
3.所以，所有的button都会响应GUIClickEventReceiver  的OnClick函数  看到这个函数里面做了分发这些响应事件
 ![Alt text](./1502592120847.png)

#### 5.2 NGUI响应事件的方法：http://www.xuanyusong.com/archives/2390
这个链接里面用的事件和委托的方法就可以像观察着模式那样处理
如果是本项目这样的就会在一个地方处理 不够解耦 但是又统一直观

#### 5.3 NGUI响应事件:https://my.oschina.net/u/185335/blog/380414
原理都在NGUI 的dll里面 


### 6、GUIManager 界面管理
这个界面管理也有点类似GUIClickEventReceiver 统一处理比较直观统一
左边的图是MainScene里面的截图 包括所有的Panel 下一幅图是GUIManager里面的panel成员
![Alt text](./1502592598574.png) ![Alt text](./1502592616992.png)

showGUI这个函数用来显示具体哪个面板的 在按钮响应分发用的挺多 点击一个按钮就打开相应的面板

设置游戏UI 像分数这些：setInGameScore 金币数量：setInGameCoinCount  
显示教程：showTutorial
刷新分数：refreshStoreGUI

### 7、InputController 输入管理
需要了解下Unity 里面的Input
http://blog.csdn.net/lingyun_blog/article/details/41451565

Unity为我们预设了一些输入：
![Alt text](./1502593455464.png) 



回到项目中的InputController，看到Update函数里面，用GetButtonUp判断是否点击了Jump函数 
 if (Input.GetButtonUp("Jump")) {
            playerController.jump(false);
        }

到此为止，这个类我们可以看到是怎么得到键盘鼠标的输入的 然后再这个类去把事件传给playerObeject 让它响应相应的动作


### 8、MissionManager 关卡管理

### 9、PowerUpManager 玩家buff管理类
能力加强的管理类： DoubleCoin双倍金币, CoinMagnet金币磁铁, Invincibility无敌, SpeedIncrease加速, None
activatePowerUp激活哪个加强buff dataManager.getPowerUpLength(powerUpType);时间在DataManager里面配置
用协程来实现加强buff的维持的时间
activatePowerUp函数激活 然后开始协程StartCoroutine("runPowerUp");
yield return new WaitForSeconds(activePowerUpData.duration);等待相应的时间 然后结束强化deactivatePowerUp();


### 10、SocialManager社交管理
Facebook Twitter的功能

### 11、StaticData 静态数据
在unityEditor里面设置

### 12、玩家的转向跳跃
这个要看这几个脚本PlayerController.cs InputController.cs 我们先确定一个重要的点：我们看到人物前进实际是把物体向后移动实现的，人物会相对当前位置跳跃 沿着Y轴移动
##### 1、先看下InputController这个脚本 
![Alt text](./1502593542093.png)
看到 up按钮和space按钮都预设为跳
![Alt text](./1502593562614.png)
上面两张图是这个工程设置了按键对应的名称：Jump Slide LeftTurn

下面我们分别说人物三类动作的响应函数
这个是控制输入的
（1）人物可以跳跃 下滑 攻击：
InputController的Update()函数

 if (Input.GetButtonUp("Jump")) {
            playerController.jump(false);
        } else if (Input.GetButtonUp("Slide")) {
            playerController.slide();
        } else if (Input.GetButtonUp("Attack")) {
            playerController.attack();
        }
        
（2）人物可以左转向 右转向
（3）游戏中有三个轨道左中右轨道，左方向键可以向左移动到最左的轨道，右方向键可以向右移动到最右的轨道
**（2）（3）的代码一起看**
LeftTurn LeftSlot用的按键是同一个 都是a和左方向键 如果playerController.turn返回true就不会执行playerController.changeSlots代码了
这里可以看出玩家左移用playerController.changeSlots代码 左转用playerController.turn

			if (Input.GetButtonUp("LeftTurn")) {
                hasTurned = playerController.turn(false, true);
            } else if (Input.GetButtonUp("RightTurn")) {
                hasTurned = playerController.turn(true, true);
            }

            // can change slots if the player hasn't turned
            if (!hasTurned) {
                if (Input.GetButtonUp("LeftSlot")) {
                    playerController.changeSlots(false);
                } else if (Input.GetButtonUp("RightSlot")) {
                    playerController.changeSlots(true);
                }
            }

**playerController.changeSlots**
infiniteObjectGenerator.slotDistance这个是unity编辑器里面配置是2  两个跑道之间的距离是2
targetSlotValue = (int)currentSlotPosition * infiniteObjectGenerator.slotDistance;这个值就是目标的跑道的偏移
这里更新目标位置
updateTargetPosition(targetRotation.eulerAngles.y);
看下这个函数updateTargetPosition的这两句
targetPosition.x += targetSlotValue * Mathf.Cos(yAngle * Mathf.Deg2Rad);
        targetPosition.z += targetSlotValue * -Mathf.Sin(yAngle * Mathf.Deg2Rad);
把targetSlotValue 换算成左边偏倚 y轴的转向也就是人物中心轴转向 如果一开始游戏 Y转向是0度  那么Mathf.Cos(yAngle * Mathf.Deg2Rad)是1 -Mathf.Sin(yAngle * Mathf.Deg2Rad);是0 然后targetSlotValue 的偏移都是X的便宜 Z不用偏移 同理可以想像下 如果向左转了90 之后 偏移就

**playerController.turn**
1. 获取目标转向：Vector3 direction = platformObject.getTransform().right * (rightTurn ? 1 : -1);
2. 得到目标的转向：targetRotation = Quaternion.LookRotation(direction);
3. 然后在LateUpdate里面真正的插值转职到targetRotation

        if (thisTransform.rotation != targetRotation) {
            thisTransform.rotation = Quaternion.RotateTowards(thisTransform.rotation, targetRotation,Mathf.Lerp(slowRotationSpeed, fastRotationSpeed, Mathf.Clamp01(Quaternion.Angle(thisTransform.rotation, targetRotation) / 45)));
        }
        
这里查下RotateTowards函数是旋转到目标角度 Mathf.Lerp函数是获得插值  插值就可以实现平滑的旋转
### 13、InfiniteGenerator和InfiniteObjects文件夹下面的脚本
MainScene里面有个Obeject叫InfiniteObject  这些无限的场景和物体都是在这个object下面

![Alt text](./1502597632750.png)

分成五类物体：
（1）obstacles：障碍物 
（2）scene：场景
（3）powerups：强化道具
（4）platforms：底板
（5）coins：硬币

#### 1、InfiniteObjectGenerator 生成器
**函数入口，调用堆栈**：
1. PlayerController::LateUpdate()
2. InfiniteObjectGenerator::moveObjects()
3. InfiniteObjectGenerator::spawnObjectRun()

我们看下spawnObjectRun函数：

有个函数在移动整个场景moveObjects  这个是被PlayerController的LateUpdate函数调用
moveObjects里面来调用spawnObjectRun  从而不断生成

**我们看下moveObjects这个函数**
1. for (int j = 0; j < (int)ObjectLocation.Last; ++j) {这个循环是移动所有的物体
2. infiniteObject = infiniteObjectHistory.getTopTurnInfiniteObject(i == 0);这句获取第一个物体判断是否要销毁
3. spawnObjectRun(true);这句调用了生成的函数

spawnObjectRun这个函数的前半部分是生成路径 后半部分是生成一个转向

## 附
vs2015断调试unity项目
http://www.itcast.cn/news/20151229/1437047587.shtml
