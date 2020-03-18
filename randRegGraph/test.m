fprintf('-------- test createRandRegGraph() ------------\n');

n = 1000;
d = 25;

G = full(createRandRegGraph(n, d));

nums=0;


bar=waitbar(0,'Prefare to calculate...');

len1=1000;len2=20;
x = zeros(1,len1*len2);
y = zeros(1,len1*len2);
x1 = zeros(1,len1);
y1 = zeros(1,len1);


for k = 1:len1-1
    for i = 1:len2
       p = randperm(n,k);
       temp=G;
       for j = 1:size(p,2)
           temp(p(j),:)=zeros(1,n);
           temp(:,p(j))=zeros(n,1);
       end
       nums=nums+1;
       x(nums)=k;
       y(nums)=conn_components(temp);
       if y(nums)==(n-k)
           x1(k)=x1(k)+1;
       end
       
       str=['in computing',num2str(roundn(100*((k-1)*len2+i)/(len1*len2),-2)),'%'];
       waitbar(((k-1)*len2+i)/(len1*len2),bar,str);
    end
    y1(k)=k;
    x1(k)=x1(k)/len2;
end
close(bar)
fig1=subplot(2,1,1);
scatter(fig1,y1,x1,'filled')
fig2=subplot(2,1,2);
scatter(fig2,x,y,'filled')

fprintf('-------- end ------------\n');