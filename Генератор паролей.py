from operator import length_hint
import random
lost = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
case = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
NUMBER = "0123456789"
Symbol = "[]{}#()*;._-"

all = lost + case + NUMBER + Symbol
length = 9
password = "".join(random.sample(all,length))
print("The password:", password)