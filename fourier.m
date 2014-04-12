datapoints=-pi:0.001:pi;
y=zeros(1,length(datapoints));
i=1;

for x=datapoints;
    for n=1:1:5%3 or 5
        y(i)=y(i)+2*(-1)^(n+1)*sin(n*x)/n;
    end
    i=i+1;
end

plot(datapoints,y)