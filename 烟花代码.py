import tkinter as tk            #导入tkinter包

from PIL import Image,ImageTk    #导入PIL包中的Image包和ImageTk包，用于打开图片，用作烟花的背景

import time as ti               #导入时间包

import math as m                #导入数学包

import random as r              #导入随机包

colors=['red','blue','lime','yellow','white','cyan','orange','deepskyblue','orangered']   #烟花的颜色

class particle:     #烟花的粒子类

    def __init__(self,canvas,num,sums,x,y,x_speed,y_speed,explosion_speed,color,size,max_life):

        self.canvas=canvas    #画布

        self.num=num          #粒子的序号

        self.sums=sums        #粒子的个数

        self.x=x              #粒子的横向坐标

        self.y=y              #粒子的纵向坐标

        self.x_speed=x_speed    #粒子在横向的移动速度

        self.y_speed=y_speed    #粒子在纵向的移动速度

        self.initial_speed=explosion_speed    #粒子的初始速度

        self.color=color       #粒子的颜色

        self.life=0            #粒子当前存活的时间

        self.max_life=max_life   #粒子最大的存活时间

        self.oval=self.canvas.create_oval(x-size,y-size,x+size,y+size,fill=self.color)   #粒子的范围（烟花的大小）

    def expand(self):    #判断粒子是否还在爆炸

        if self.life<=1.5:    #粒子是否到达最大爆炸时间

            return 1

        else:

            return 0

    def alive(self):     #判断粒子是否存活

        if self.life<=self.max_life:     #粒子是否到达最大存活时间

            return 1

        else:

            return 0

    def new(self,dt):    #更新当前烟花的粒子位置

        self.life=self.life+dt   #更新当前存活时间

        if self.alive() and self.expand():   #如果当前存活时间在爆炸时间内

            move_x=m.cos(m.radians(self.num*360/self.sums))*self.initial_speed   #则执行爆炸，更新横向坐标

            move_y=m.sin(m.radians(self.num*360/self.sums))*self.initial_speed   #更新纵向坐标

            self.canvas.move(self.oval,move_x,move_y)    #在画布上更新烟花

            self.x_speed=move_x/(float(dt)*1000)    #烟花绽放的速度

        elif self.alive():    #如果爆炸结束了，但粒子还存在，则开始坠落

            move_x=m.cos(m.radians(self.num*360/self.sums))    #更新横向坐标

            self.canvas.move(self.oval,self.x_speed+move_x,self.y_speed+0.05*dt)  #在画布上更新烟花

            self.y_speed=self.y_speed+0.5*dt     #烟花坠落的速度

        elif self.oval is not None:    #如果在坠落的时间外了，就将烟花从画布上擦除

            canvas.delete(self.oval)

            self.oval=None

def fireworks(canvas):#烟花函数（循环更新当前界面）

    times=ti.time()       #获取当前时间戳

    explode_points=[]     #烟花列表

    wait_time=r.randint(1,10)      #等待时间

    num_explode=r.randint(20,30)     #烟花的个数

    for point in range(num_explode):     #依次更新各个烟花

        firework=[]      #当前烟花的粒子列表

        x=r.randint(50,550)   #当前烟花的粒子在横向的活动范围

        y=r.randint(50,150)   #当前烟花的粒子在纵向的活动范围

        speed=r.uniform(0.5,2)   #粒子的绽放速度

        size=r.uniform(0.5,1.5)    #粒子的大小

        color=r.choice(colors)     #粒子的颜色

        explosion_speed=r.uniform(0.2,5)    #粒子爆炸的速度

        sum_particles=r.randint(30,50)      #粒子的总数

        max_life=r.uniform(0.6,1.75)        #粒子的最大存活时间

        for i in range(1,sum_particles):   #当前烟花的每个粒子的参数

            fire=particle(canvas,num=i,sums=sum_particles,explosion_speed=explosion_speed,x=x,y=y,x_speed=speed,y_speed=speed,color=color,size=size,max_life=max_life)

            firework.append(fire)    #将当前粒子加入到当前的烟花粒子列表中

        explode_points.append(firework)   #将当前烟花加入到烟花列表中

    expand_time=0     #初始爆炸的时间

    while expand_time<2:    #如果爆炸的时间小于2

        ti.sleep(0.001)     #爆炸帧

        newtime=ti.time()   #获取爆炸一次的时间戳

        times,dt=newtime,newtime-times    #更新当前的时间戳

        for point in explode_points:     #更新所有的粒子位置

            for item in point:

                item.new(dt)

        canvas.update()    #更新当前画布

        expand_time=expand_time+dt   #更新当前的爆炸时间

    global root   #root界面是全局变量

    root.after(wait_time,fireworks,canvas)

def close():     #关闭画布

    global root   #root界面是全局变量

    root.quit()

if __name__ == '__main__':

    width=600     #画布的宽

    height=375    #画布的高

    root=tk.Tk()   #定义界面root

    root.title('烟花')

    screenheight=root.winfo_screenheight()   #获取当前屏幕高度

    screenwidth=root.winfo_screenwidth()     #获取当前屏幕宽度

    x=(screenwidth-width)//2

    y=(screenheight-height)//2-100

    root.geometry('%dx%d+%d+%d'%(width,height,x,y))   #将界面放在屏幕中央

    canvas=tk.Canvas(root,width=width,height=height)  #将画布放在界面中铺满界面

    image=Image.open(r"D:\下载\图片\壁纸\wallhaven-397jrd_2560x1600.png")     #打开烟花背景图片

    image.thumbnail((width,height))                #将烟花背景缩放为画布大小

    photo=ImageTk.PhotoImage(image)                #将烟花背景放在画布中

    canvas.create_image(0,0,image=photo,anchor='nw')

    canvas.pack()      #放置画布

    root.protocol("WM_DELETE_WINDOW",close)     #关闭循环的界面

    root.after(100,fireworks,canvas)            #开始放烟花

    root.mainloop()   #将界面停住