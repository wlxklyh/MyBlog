---
title: CppReview
date: 2017-08-10T00:00:00.000Z
tags: null
published: true
---

# 复习C++ 

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

### 2、





