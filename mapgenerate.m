Asite=[0 0;0 1;1 0;1 1];
Bsite=[1/3 1/3;4/3 1/3;1/3 4/3;4/3 4/3];
Csite=[2/3 2/3;2/3 -1/3;-1/3 2/3;-1/3 -1/3];
RawData=table2array(CuPcRegular);
for i=1:2601;
    xcord=RawData(i, 3);
    ycord=RawData(i, 4);
    for k=1:4;
        Adis(k)=sqrt((xcord-Asite(k, 1))^2+(ycord-Asite(k,2))^2);
        Bdis(k)=sqrt((xcord-Bsite(k, 1))^2+(ycord-Bsite(k,2))^2);
        Cdis(k)=sqrt((xcord-Csite(k, 1))^2+(ycord-Csite(k,2))^2);
    end; 
    Cmap_Data(i,1)=1-min(Adis)/0.71;
    Cmap_Data(i,2)=1-min(Bdis)/0.71;
    Cmap_Data(i,3)=1-min(Cdis)/0.71;
end;
scatter (RawData(:,1),RawData(:,2), 15, Cmap_Data,'filled');