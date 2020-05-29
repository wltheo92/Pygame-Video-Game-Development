import pygame as p,random
p.init()
screen=p.display.set_mode((1000,700))
p.display.set_caption("Megaman X4")
clock=p.time.Clock()
fps=15
f=3 #factor for scaling up objects

font=p.font.Font("OpenSans-Bold.ttf",100)

p.mixer.music.load("battle_music.mp3")

G=p.Rect(0,570,6084,130)
Rs=[G]

#Settings for sub-boss Magma Lagoon
mI=0
mx,my=900,570
mdx,mdy=0,0
mxbool=1
mstate="i"
minit=1
msurf=p.image.load("magma_lagoon.jpg")
mHP=10000
mBlast=[]
mbody_rect=None

midle=[(290,27,88,79)]
mattack1=[(525,126,70,105)] 
mattack2=[(141,437,82,76)]
mattack3=[(109,580,91,63),(109,580,91,63)] 
mattack4=[(218,254,98,73),(218,254,98,73)]                  
mblast0=[(518,1010,69,52),(454,1008,61,56),(386,1008,59,54),\
         (300,1010,82,53),(236,1011,55,52),(187,1019,45,34),\
         (149,1022,32,38),(127,1028,18,14)]
mblast1=[(581,924,54,64),(520,924,56,59),(460,923,56,60),\
         (397,921,54,80),(336,919,49,51),(296,925,34,51),\
         (255,924,36,51),(213,924,36,45),(170,921,36,64),\
         (134,920,31,41),(113,928,17,53),(93,935,14,18)]
mblast2=[(230,869,22,49),(259,870,35,46),(298,870,32,48),\
         (334,871,32,48),(369,872,30,44),(408,874,25,39),\
         (444,885,27,32),(479,885,22,28),(513,891,20,20)]
mw,mh=88*f,79*f

#Settings for playable character
surf=p.image.load("zerox4sheet.jpg")
I=0
x,y=100,570
dx,dy=0,0
xbool=0
state="i"
init=1
HP=10000
saber_rect=None
body_rect=None

idle=[(292,103,44,49),(341,103,44,49),(389,103,44,49),\
      (436,103,44,49),(485,103,44,49)]
idle2=[(328,1376,40,49),(376,1377,41,48),(424,1378,42,46),\
       (470,1378,44,46)]
walk=[(208,323,51,45),(265,324,51,45),(320,323,49,46),\
      (375,322,47,46),(429,320,45,49),(481,320,41,48),\
      (111,385,47,48),(167,386,50,45),(223,387,47,46),\
      (275,386,51,47),(332,385,48,48),(386,384,46,49),\
      (437,384,44,50),(486,385,47,48)]
jumpup=[(166,164,46,58),(219,166,45,56),(268,166,44,58),\
        (319,166,44,58),(370,169,45,57)]
jumpdown=[(424,169,41,53),(474,175,41,56),(132,234,39,65),\
          (177,230,37,78),(221,230,36,80),(265,230,37,80),\
          (310,249,42,60),(360,264,43,43)]
dash=[(111,990,47,46),(162,993,56,42),(227,1001,58,35),\
      (227,1001,58,35),(227,1001,58,35),(227,1001,58,35),\
      (227,1001,58,35),(422,991,46,46),(522,990,42,46)]
saber1=[(156,440,49,63),(214,440,78,63),(300,442,88,60),\
        (390,455,92,48),(491,453,84,50),(25,514,71,45),\
        (104,514,67,45),(176,514,60,45),(240,514,48,45),\
        (296,514,47,45),(457,514,46,46),(508,513,42,46),\
        (557,514,44,46)]
oo1=[(-22,45),(-22,46),(-24,48),(-29,49),(-21,49),(-21,45),\
     (-20,45),(-20,45),(-19,45),(-19,45),(-23,45),(-19,45),\
     (-22,45)]
wo1=[(-3,-63,27,23),(13,-63,43,47),(26,-59,37,58),\
     (26,-39,37,38),(26,-15,36,14),(25,-15,26,13),\
     (26,-18,20,15),(26,-15,14,11),None,None,None,\
     None,None]
saber2=[(151,567,53,45),(206,564,70,48),(278,566,85,46),\
        (434,620,47,48)]
oo2=[None,(-30,48),(-26,46),None]
wo2=[None,(23,-29,16,10),(-10,-30,68,12),None]
jumpsaber=[(59,837,54,62),(118,838,72,62),(193,839,91,66),\
           (291,831,100,74),(524,829,42,79),(572,828,38,80)]
oo3=[None,(-27,58),(-29,66),(-28,74),None,None]
wo3=[None,(6,-62,40,32),(-10,-66,71,48),(28,-64,48,56),\
     None,None]

def collideG(x,y,dy,state,I,init,Rs,Z):
    K=["i" if HP>=20 else "i2","l","r"]
    for r in Rs:
        if r.collidepoint(x,int(y+dy)):
            return (r.top,0,K[Z],0,1)
    return (y,dy,state,I,init)

bg=p.image.load("bg01.jpg")
L=int(bg.get_rect().width*700/bg.get_rect().height)
bg=p.transform.scale(bg,(L,700))

p.mixer.music.play()

while 1:
    for e in p.event.get():
        if e.type==p.QUIT:p.quit()
        if e.type==p.KEYDOWN:
            if e.key==p.K_RIGHT:
                if state in ["i","i2"]:state="r"
                if state=="l":state="r"
                if state=="ju":state="jur"
                if state=="jul":state="jur"
                if state=="jd":state="jdr"
                if state=="jdl":state="jdr"
                
            if e.key==p.K_LEFT:
                if state in ["i","i2"]:state="l"
                if state=="r":state="l"
                if state=="ju":state="jul"
                if state=="jur":state="jul"
                if state=="jd":state="jdl"
                if state=="jdr":state="jdl"

            if e.key==p.K_x:
                if state in ["i","i2"]:state="ju"
                if state=="l":state="jul"
                if state=="r":state="jur"
                
            if e.key==p.K_z:
                if state in ["i","i2"]:state="d"
                if state=="l":state="dl"
                if state=="r":state="dr"
                
            if e.key==p.K_c:
                if state in ["i","i2"]:state,I="s1",0
                if state in ["l","r"]:state,I="s2",0
                if state=="ju":state,I="jus",0
                if state=="jul":state,I="jusl",0
                if state=="jur":state,I  ="jusr",0
                if state=="jd":state,I="jds",0
                if state=="jdl":state,I="jdsl",0
                if state=="jdr":state,I="jdsr",0
                
        if e.type==p.KEYUP:
            if e.key==p.K_RIGHT:
                if state=="r":state="i" if HP>=20 else "i2"
            if e.key==p.K_LEFT:
                if state=="l":state="i" if HP>=20 else "i2"
    
    if state=="i":
        M=idle
        dx,dy=0,0
        saber_s=None
        
    if state=="i2":
        M=idle2
        dx,dy=0,0
        saber_s=None
        
    if state=="r":
        M=walk
        dx,dy=10,0
        xbool=0
        
    if state=="l":
        M=walk
        dx,dy=-10,0
        xbool=1
        
    if state=="ju":
        M=jumpup
        if init:
            dy=-60
            init=0
        else:
            dy=int(dy/2)
            if dy==0:
                state="jd"
                I=0
                init=1
                
    if state=="jd":
        M=jumpdown
        if init:
            dy=10
            init=0
        else:
            dy=dy*1.5;
            y,dy,state,I,init=collideG(x,y,dy,state,I,init,Rs,0)
            
    if state=="jul":
        M=jumpup
        dx=-20
        xbool=1
        if init:
            dy=-60
            init=0
        else:
            dy=int(dy/2)
            if dy==0:
                state="jdl"
                I=0
                init=1
                
    if state=="jur":
        M=jumpup
        dx=20
        xbool=0
        if init:
            dy=-60
            init=0
        else:
            dy=int(dy/2)
            if dy==0:
                state="jdr"
                I=0
                init=1
    
    if state=="jdl":
        M=jumpdown
        dx=-20
        xbool=1
        if init:
            dy=10
            init=0
        else:
            dy=dy*1.5;
            y,dy,state,I,init=collideG(x,y,dy,state,I,init,Rs,1)
            
    if state=="jdr":
        M=jumpdown
        dx=20
        xbool=0
        if init:
            dy=10
            init=0
        else:
            dy=dy*1.5;
            y,dy,state,I,init=collideG(x,y,dy,state,I,init,Rs,2)
            
    if state=="d":
        M=dash
        dx=-40 if xbool else 40
        dy=0
        if I==len(M)-1:
            state="i" if HP>=20 else "i2"
            I=0
    
    if state=="dl":
        M=dash
        dx=-40
        xbool=1
        dy=0
        if I==len(M)-1:
            state="l"
            I=0
            
    if state=="dr":
        M=dash
        dx=40
        xbool=0
        dy=0
        if I==len(M)-1:
            state="r"
            I=0
            
    if state=="s1":
        M=saber1
        dx,dy=0,0
        if I==len(M)-1:
            state="i" if HP>=20 else "i2"
            M=idle if HP>=20 else idle2
            I=0
            
    if state=="s2":
        M=saber2
        dx,dy=0,0
        if I==len(M)-1:
            state="i" if HP>=20 else "i2"
            M=idle if HP>=20 else idle2
            I=0
            
    if state=="jus":
        M=jumpsaber
        dy=int(dy/2)
        if dy==0:
            state="jd"
            I=0
            init=1
            
    if state=="jusl":
        M=jumpsaber
        xbool=1
        dy=int(dy/2)
        if dy==0:
            state="jdl"
            I=0
            init=1
            
    if state=="jusr":
        M=jumpsaber
        xbool=0
        dy=int(dy/2)
        if dy==0:
            state="jdr"
            I=0
            init=1
            
    if state=="jds":
        M=jumpsaber
        if init:
            dy=10
            init=0
        else:
            dy=1.5*dy
            y,dy,state,I,init=collideG(x,y,dy,state,I,init,Rs,0)
            
    if state=="jdsl":
        M=jumpsaber
        dx=-20
        xbool=1
        if init:
            dy=10
            init=0
        else:
            dy=1.5*dy
            y,dy,state,I,init=collideG(x,y,dy,state,I,init,Rs,1)
            
    if state=="jdsr":
        M=jumpsaber
        dx=20
        xbool=0
        if init:
            dy=10
            init=0
        else:
            dy=1.5*dy
            y,dy,state,I,init=collideG(x,y,dy,state,I,init,Rs,2)
    
    screen.blit(bg.subsurface(p.Rect(0,0,1000,700)),(0,0))
    
    x+=dx
    y+=dy
    I=(I+1)%len(M)
    a,b,c,d=M[I]
    w,h=f*c,f*d
    if x<0:x=int(w/2)
    if x>=1000:x=1000-int(w/2)

    #Drawing playable character
    if HP>0:
    
        s=surf.subsurface(p.Rect(a,b,c,d))
        s=p.transform.scale(s,(w,h))
        s=p.transform.flip(s,xbool,False)

        
        if state not in ["s1","s2","jus","jusl","jusr"]:
            screen.blit(s,(round(x-w/2),round(y-h)))
            body_rect=p.Rect(x-f*10,int(y-h/2-h/4),20*f,int(h/2))
            
        else:
            if state=="s1":OO,WO=oo1,wo1
            elif state=="s2":OO,WO=oo2,wo2
            else:OO,WO=oo3,wo3
            if WO[I]:
                sox,soy,sw,sh=WO[I]
                sox,soy,sw,sh=f*sox,f*soy,f*sw,f*sh
                
                if xbool:saber_rect=p.Rect(x-abs(sox)-sw,y+soy,sw,sh)
                else:saber_rect=p.Rect(x+sox,y+soy,sw,sh)
            if OO[I]:
                ox,oy=OO[I]
                ox=f*ox
                oy=f*oy
                if xbool:screen.blit(s,(x-(w-abs(ox)),y-h))
                else:screen.blit(s,(x+ox,y-h))
                body_rect=p.Rect(x-f*10,int(y-oy/2-oy/4),20*f,int(oy/2))
            else:
                body_rect=p.Rect(x-f*10,int(y-h/2-h/4),20*f,int(h/2))
                screen.blit(s,(round(x-w/2),round(y-h)))

        p.draw.rect(screen,p.Color("white"),p.Rect(20,20,10,500))
        p.draw.rect(screen,p.Color("yellow"),\
        p.Rect(20,20+int((1-HP/10000)*500),10,int(500*HP/10000)))
        
    else:
        body_rect=None
        text=font.render("GAME OVER",1,p.Color("white"),p.Color("blue"))
        screen.blit(text,(30,30))
    
    if mstate=="i":
        mM=midle
        mdx,mdy=0,0
        mxbool=0 if x<=mx else 1
        minit=1
        if body_rect:
            if abs(mx-x)<=900:mstate=random.choice(["a1","a3","a4"])
            
    if mstate=="a1":
        mM=mattack1
        mdx=0
        mxbool=0 if x<=mx else 1
        mBlast.append([1,int(mx-0.7*mw) if x<mx else int(mx+0.7*mw),my-mh,-10,0])
        if minit:
            mdy=-100
            minit=0
        else:
            mdy=int(mdy/1.5)
            if mdy==0:
                mstate="a2"
                mI=0
                minit=1
                
    if mstate=="a2":
        mM=mattack2
        if body_rect.collidepoint(mx,my): HP-=5
        for r in Rs:
            if r.collidepoint(mx,my):
                mstate="i"
                mI=0
                my=r.top
                mdy=0
                break
        else:
            if minit:
                mdy=20
                mdx=-1*int(0.2*abs(mx-x)) if x<mx else int(abs(mx-x)/5)
                mxbool=0 if x<mx else 1
                minit=0
            else:
                mdy=1.5*abs(mdy)
                for r in Rs:
                    if r.collidepoint(mx,my+mdy):
                        mstate="i"
                        my=r.top
                        mdx,mdy=0,0
                        mM=midle
                        mI=0
                        minit=1
                        break
                        
    if mstate=="a3":
        mM=mattack3
        mdx,mdy=0,0
        mxbool=0 if x<mx else 1
        mBlast.append([0,int(mx-0.6*mw) if x<mx else int(mx+0.6*mw),\
        my-39*f,-80 if x<=mx else 80,0])
        if mI==len(mM)-1:
            mstate="i"
            mI=0
            
    if mstate=="a4":
        mM=mattack4
        mdx,mdy=0,0
        mxbool=0 if x<mx else 1
        mBlast.append([2,int(mx-0.4*mw) if x<mx else int(mx+0.4*mw),\
        my-48*f,-80 if x<=mx else 80,0])
        if mI==len(mM)-1:
            mstate="i"
            mI=0
    
    if mHP>0:
    
        mx+=mdx
        my+=mdy
        mI=(mI+1)%len(mM)
        if mx<0:
            mx=int(mw/2)
            mxbool=1
        if mx>1000:
            mx=1000-int(mw/2)
            mxbool=0
        a,b,c,d=mM[mI]
        ms=msurf.subsurface(p.Rect(a,b,c,d))
        mw,mh=f*c,f*d
        mbody_rect=p.Rect(int(mx-20*f),int(my-mh/2-mh/4),40*f,int(mh/2))
        if saber_rect:
            k=saber_rect.colliderect(mbody_rect)
            if k==True:mHP-=10
        ms=p.transform.scale(ms,(mw,mh))
        ms=p.transform.flip(ms,mxbool,False)
        screen.blit(ms,(int(mx-mw/2),my-mh))
        
        if len(mBlast)>0:
            NEW=[]
            for e in mBlast:
                A,B,C,D,E=e
                if A==0:
                    a,b,c,d=mblast0[E]
                    bs=msurf.subsurface(p.Rect(a,b,c,d))
                    bw,bh=f*c,f*d
                    bs=p.transform.scale(bs,(bw,bh))
                    bs=p.transform.flip(bs,True if D>0 else False,False)
                    screen.blit(bs,(int(B-bw/2),int(C-bh/2)))
                    if body_rect:
                        if p.Rect(int(B-bw/2),int(C-bh/2),bw,bh).\
                        colliderect(body_rect):HP-=5
                    if (B+D<1000 or B+D>0) and E<len(mblast0)-1:
                        NEW.append([A,B+D,C,D,E+1])
                elif A==1:
                    a,b,c,d=mblast1[E]
                    bs=msurf.subsurface(p.Rect(a,b,c,d))
                    bw,bh=f*c,f*d
                    bs=p.transform.scale(bs,(bw,bh))
                    screen.blit(bs,(int(B-bw/2),int(C-bh/2)))
                    if body_rect:
                        if p.Rect(int(B-bw/2),int(C-bh/2),bw,bh).\
                        colliderect(body_rect):HP-=5
                    if C+D>0 and E<len(mblast1)-1:
                        NEW.append([A,B,C+D,D,E+1])
                else:
                    a,b,c,d=mblast2[E]
                    bs=msurf.subsurface(p.Rect(a,b,c,d))
                    bw,bh=f*c,f*d
                    bs=p.transform.scale(bs,(bw,bh))
                    bs=p.transform.flip(bs,True if D>0 else False,False)
                    screen.blit(bs,(int(B-bw/2),int(C-bh/2)))
                    if body_rect:
                        if p.Rect(int(B-bw/2),int(C-bh/2),bw,bh).\
                        colliderect(body_rect):HP-=5
                    if (B+D<1000 or B+D>0) and E<len(mblast0)-1:
                        NEW.append([A,B+D,C,D,E+1])
            mBlast=NEW

        p.draw.rect(screen,p.Color("white"),p.Rect(970,20,10,500))
        p.draw.rect(screen,p.Color("yellow"),\
        p.Rect(970,20+int((1-mHP/10000)*500),10,int(500*mHP/10000)))
    else:
        text=font.render("Victory",1,p.Color("white"),p.Color("blue"))
        screen.blit(text,(30,30))
    p.display.update()
    clock.tick(fps)

