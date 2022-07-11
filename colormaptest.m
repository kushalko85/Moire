clear;
Asite=[0 0;0 1;1 0;1 1];
Bsite=[1/3 1/3;4/3 1/3;1/3 4/3;4/3 4/3];
Csite=[2/3 2/3;2/3 -1/3;-1/3 2/3;-1/3 -1/3];
confactor=0.71
%confactor=confactor*0.82;
for i=1:100;
    for j =1:100;
        xcord=0.01*i;
        ycord=0.01*j;
        % calculating distance
        for k=1:4;
            Adis(k)=sqrt((xcord-Asite(k, 1))^2+(ycord-Asite(k,2))^2);
            Bdis(k)=sqrt((xcord-Bsite(k, 1))^2+(ycord-Bsite(k,2))^2);
            Cdis(k)=sqrt((xcord-Csite(k, 1))^2+(ycord-Csite(k,2))^2);
        end;            
         C(i,j,1)=1-min(Adis)/(confactor);
         C(i,j,2)=1-min(Bdis)/(confactor);
         C(i,j,3)=1-min(Cdis)/(confactor);
    end;
end;
image (C)

       