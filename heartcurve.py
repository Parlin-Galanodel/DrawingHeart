#heartcurve function, from wolfram
#using heart surface function
#       (http://mathworld.wolfram.com/HeartSurface.html)

# ugly C-styled code
import sys
from math import sqrt
printf=sys.stdout.write
def f(x,y,z):
    a=1.*x*x+9./4.*y*y+1.*z*z-1
    return a*a*a-x*x*z*z*z-9./80.*y*y*z*z*z
    
def h(x,z):
    y=1.0
    while y>=0:
        if f(x,y,z)<=0:
            return y
        y-=0.001
    return 0
    
def main():
    z=1.5
    while z>-1.5:
        x=-1.5
        while x<1.5:
            v=f(x,0,z)
            if v<=0:
                y0=h(x,z)
                ny=0.01
                nx=h(x+ny,z)-y0
                nz=h(x,z+ny)-y0
                nd=1./sqrt(nx*nx+ny*ny+nz*nz)
                d=(nx+ny-nz)*nd*0.5+0.5
                temp=int(d*5.0)
                printf (".:-=+*#%@"[temp])#use a string to denote 
                                          #different depth
                #heart.write(".:-=+*#%@"[temp])
            else:
                printf (' ')
                #heart.write(' ')
            x+=0.05#stepwidth, control the width of the heart
        printf ('\n')
        #heart.write('\n')
        z-=0.1#height
if __name__=='__main__':
	#heart=file('D:/heart.txt','wb')
	main()
	#heart.close()
	