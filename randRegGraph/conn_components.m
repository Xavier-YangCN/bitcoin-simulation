function num = conn_components(A)
%given an adjacant matrix of a graph, print the number of vertecies of its max connected components
global a;
a = zeros(1,1000);

len = size(A,1);
nums = 0;

for i = 1:len
    if a(i)==0
        nums = nums+1;
        dfs(A,i,nums);
    end
end

b = zeros(1,nums);
for i = 1:len
    b(a(i))= b(a(i))+1;        
end

num=0;
for i = 1:nums
    if b(i)>num
        num=b(i);
    end
end

end

function dfs(A,m,x)
%dfs from node m
global a;
a(m)=x;
len = size(A,1);

for i = 1:len
    if (A(m,i)==1) && (a(i)==0)
        a(i)=x;
        dfs(A,i,x);
    end
end

end





