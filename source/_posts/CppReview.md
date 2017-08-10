---
title: CppReview
date: 2017-08-10T00:00:00.000Z
tags: null
published: true
---

# 复习C++ 

回顾复习下C++的一些知识~
<!-- more -->

大学写的博客做了些实验 验证C++的知识点：http://blog.csdn.net/linyanhou/article/details/40153521

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



