from PIL import Image, ImageDraw, ImageFont
import math

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# aiX palette (site theme #bbdefb family)
DEEP   = (13, 71, 118)     # deep blue
MID    = (25, 118, 210)    # primary blue
LIGHT  = (187, 221, 251)   # theme light blue
PALE   = (232, 242, 253)   # near-white blue
INK    = (15, 42, 66)

def lerp(a,b,t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))

def hgrad(w,h,c1,c2):
    img=Image.new("RGB",(w,h),c1); px=img.load()
    for x in range(w):
        t=x/max(1,w-1); col=lerp(c1,c2,t)
        for y in range(h): px[x,y]=col
    return img

def dots(draw,w,h,color,step=26,r=2,alpha=None):
    for y in range(0,h,step):
        for x in range(0,w,step):
            draw.ellipse([x-r,y-r,x+r,y+r],fill=color)

def banner(title, fname, w=1200, h=200):
    img=hgrad(w,h,DEEP,MID)
    d=ImageDraw.Draw(img,"RGBA")
    # subtle dot texture on right
    for y in range(0,h,22):
        for x in range(int(w*0.62),w,22):
            d.ellipse([x-2,y-2,x+2,y+2],fill=(255,255,255,22))
    # accent bar
    d.rectangle([0,0,10,h],fill=LIGHT)
    # left aiX tag
    tf=ImageFont.truetype(FB,26)
    d.text((44,28),"aiX WEEKLY",font=tf,fill=(187,221,251,255))
    # title
    size=64
    f=ImageFont.truetype(FB,size)
    while d.textlength(title,font=f) > w-90 and size>34:
        size-=2; f=ImageFont.truetype(FB,size)
    bbox=d.textbbox((0,0),title,font=f)
    th=bbox[3]-bbox[1]
    d.text((44, 96),title,font=f,fill=(255,255,255,255))
    # thin underline accent
    d.rectangle([46, 96+th+22, 46+min(360,int(d.textlength(title,font=f))), 96+th+26],fill=(187,221,251,230))
    img.save(fname)
    print("wrote",fname)

sections = [
    ("TL;DR","media/tldr.png"),
    ("Table of Contents","media/toc.png"),
    ("This Week at a Glance","media/glance.png"),
    ("Research Highlights","media/research.png"),
    ("What's in the News","media/news.png"),
    ("Institutional Movements","media/movements.png"),
    ("Most Discussed","media/discussed.png"),
    ("From My Desk","media/fromdesk.png"),
    ("Try This Week","media/try.png"),
]
for t,f in sections: banner(t,f)

# Featured image (1600x840, richer)
def featured():
    w,h=1600,840
    img=hgrad(w,h,DEEP,MID)
    d=ImageDraw.Draw(img,"RGBA")
    # network motif
    import random; random.seed(7)
    pts=[(random.randint(int(w*0.5),w-40),random.randint(40,h-40)) for _ in range(26)]
    for i,(x,y) in enumerate(pts):
        for (x2,y2) in pts[i+1:]:
            if (x-x2)**2+(y-y2)**2 < 240**2:
                d.line([x,y,x2,y2],fill=(187,221,251,45),width=1)
    for (x,y) in pts:
        d.ellipse([x-5,y-5,x+5,y+5],fill=(187,221,251,190))
    # left accent
    d.rectangle([0,0,16,h],fill=LIGHT)
    tf=ImageFont.truetype(FB,34)
    d.text((70,88),"aiX WEEKLY",font=tf,fill=(187,221,251,255))
    f1=ImageFont.truetype(FB,92)
    d.text((66,150),"AI in Higher",font=f1,fill=(255,255,255,255))
    d.text((66,250),"Education",font=f1,fill=(255,255,255,255))
    fs=ImageFont.truetype(FR,40)
    d.text((70,392),"August 26th, 2026",font=fs,fill=(210,230,250,255))
    # subtitle line
    d.rectangle([72,470,470,474],fill=(187,221,251,220))
    fq=ImageFont.truetype(FR,34)
    lines=["Adoption is near-universal.","Guidance is not.","Counting is not measuring."]
    yy=500
    for ln in lines:
        d.text((72,yy),ln,font=fq,fill=(224,238,252,255)); yy+=52
    fcap=ImageFont.truetype(FR,26)
    d.text((72,h-64),"Curated by Claude · Reviewed by Tian Zheng · aiX Programs, Columbia University",font=fcap,fill=(180,206,236,255))
    img.save("featured.png"); print("wrote featured.png")

featured()
