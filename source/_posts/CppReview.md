---
title: CppReview
date: {}
tags: null
published: true
---

# 复习C++ 

回顾复习下C++的一些知识~
重新看下大学时候自己写的博客，做了些实验来验证C++的知识点：http://blog.csdn.net/linyanhou/article/details/40153521

<!-- more -->


### 1、虚函数实现机制
Class A(){
	virtual void Ax(){};
    virtual void Ay(){};
};
Class D:A{
	virtual void Ax(){};
	virtual void Ax1(){};
    virtual void Ay1(){};
};

A a;
D d;

a对象包含一个虚函数表的指针
vptrA:存了Ax、Ay函数的函数地址 
d对象包含一个虚函数表的指针
vptrD:存了Ax、Ay、Ax1、Ay1函数的函数地址 
Ax是指的是继承类里面的 Ax

多重集成 A、B（两个都包含虚函数的类） 那么则会有两个虚表 


用下面代码看下虚表存在哪里：
class A
{
public :
       virtual void test(){};
};
int main()
{
       A a1;
       A a2;
      cout<<&a1<<endl;
      cout<< sizeof (a1)<<endl;
      cout<<&a2<<endl;
      cout<< sizeof (a2)<<endl;
}


输出结果跟 &a1 a1._vfptr 比较发现是一样的，sizeof(a1)是4字节

见大学写的博客：http://blog.csdn.net/linyanhou/article/details/40153521

### 2、构造函数调用顺序
基类构造函数  之后成员对象的构造函数 之后派生类的构造函数
下面实验是说明成员对象在初始化列表初始化的话是先于本身的构造函数的：
class C
{
public :
      C()
      {
            printf( "C constructor\n" );
      }
      C( int i)
      {
            printf( "have num %d constructor\n" ,i );
      }
};
class A
{
public :
       C c;
      A():c(123){printf( "A constructor\n" );c = C ();};
       virtual void foo(){
            printf( "Base Class Constructor." );
      }
};
int main()
{
       A a;
}
输出是：
第一先是这句：A():c(123) 调用了 C 的参数构造函数 输出have num 123 constructor
第二是这句：printf( "A constructor\n" );  输出A constructor
第三句是这句：c = C (); 调用 C 的默认构造函数C constructor

### 3、union  还有大端小端的问题
利用 union 来看是否是大小端
union T
{
	char s[2];
    int a;
};

int main()
{
	T t;
    (1)
	打印 t.s[0]  t.s[1] t.a 的地址得知
    &t.s[0] = &（t.a）
    结论：char数组的0位地址是int的地址向左对齐
    (2)
      t.a=0;
      t.s[0]=10;
      t.s[1]=1;
      printf( "%d\n" ,t.a);
      
      **（1）定义分析：**
      大端 高位存在低地址 例如：
      int 4字节  byte[0] byte[1] byte[2] byte[3] 
      假设这个 int的16进制是 0x12 34 56 78
      地址递增 int 0x12 34 56 78 
      那么 低地址byte[0]存整数的最高位0x12 byte[1]=0x34 byte[2]=0x56 byte[3]=0x78
      
      **（2）输出分析：**
      输出是266，所以这个 int a 的16进制：0x00 00 01 0A 
      0A是整数低位，t.s[0]是低地址 高位存在高地址
      
      【注】：修正原来的文章  我当时实验的电脑是小端  高位存在高地址
      
      
      
}


### 4、verctor 的内存分配：
回顾下自己大学的博客 久不用就容易忘记 还是需要不断的学习
http://blog.csdn.net/linyanhou/article/details/40067727
1. 不断 push vectro 内存分配 capacity
for( int i=0;i<200;i++){
    v.push_back(a1);
}
不断 push 然后查看 capacity:
1 
2
3
4
6
9
13
源码：
if (_Capacity < size() + _Count)//当前空间不足，需要扩容  
            {   // not enough room, reallocate  
            _Capacity = max_size() - _Capacity / 2 < _Capacity  
                ? 0 : _Capacity + _Capacity / 2;    // try to grow by 50%，扩容50%  
            if (_Capacity < size() + _Count)//扩容50%后依然不够容下，则使容量等于当前数据个数加上新增数据个数
   
2. 构造函数的调用过程：
详细看我之前写的博客：
http://blog.csdn.net/linyanhou/article/details/40067727
   
3. 如何使用提高性能：
为了比较，我们用了三种方式来把100个数据存入vector中，分别是：1、直接每次push_back();2、使用resize()提前分配100个空间，然后push_back;3、使用reserve提前分配100个存储空间。

速度（快到慢）：3>2>1

【注】：reserve分配空间  resize()会调用构造函数