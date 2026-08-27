from PIL import Image, ImageDraw, ImageFont
import random
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DEEP=(13,71,118); MID=(25,118,210); LIGHT=(187,221,251)
def lerp(a,b,t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
w,h=1600,840
img=Image.new("RGB",(w,h),DEEP); px=img.load()
for x in range(w):
    c=lerp(DEEP,MID,x/(w-1))
    for y in range(h): px[x,y]=c
d=ImageDraw.Draw(img,"RGBA")
random.seed(11)
pts=[(random.randint(int(w*0.5),w-40),random.randint(40,h-40)) for _ in range(26)]
for i,(x,y) in enumerate(pts):
    for (x2,y2) in pts[i+1:]:
        if (x-x2)**2+(y-y2)**2 < 240**2:
            d.line([x,y,x2,y2],fill=(187,221,251,45),width=1)
for (x,y) in pts: d.ellipse([x-5,y-5,x+5,y+5],fill=(187,221,251,190))
d.rectangle([0,0,16,h],fill=LIGHT)
d.text((70,84),"aiX WEEKLY",font=ImageFont.truetype(FB,34),fill=(187,221,251,255))
f1=ImageFont.truetype(FB,92)
d.text((66,146),"AI in Higher",font=f1,fill=(255,255,255,255))
d.text((66,246),"Education",font=f1,fill=(255,255,255,255))
d.text((70,388),"August 26th, 2026",font=ImageFont.truetype(FR,40),fill=(210,230,250,255))
d.rectangle([72,466,470,470],fill=(187,221,251,220))
fq=ImageFont.truetype(FR,34)
lines=["Teaching about AI, not just with it.","New requirements. Shared frameworks.","A field guide to what's available."]
yy=498
for ln in lines:
    d.text((72,yy),ln,font=fq,fill=(224,238,252,255)); yy+=52
d.text((72,h-64),"Curated by Claude · Reviewed by Tian Zheng · aiX Programs, Columbia University",font=ImageFont.truetype(FR,26),fill=(180,206,236,255))
img.save("featured.png"); print("featured.png refreshed")
