#define MAX_LEVEL 10
using namespace std;

void printSocialGraph (Member m){
    //Your code here
    int level=0;
    //Prepare to print the first layer
    unordered_map<Member, int> record;
    stack<Member> s;
    s.push(m);
    
    while(level<=MAX_LEVEL){
        //Extract all the members we get in last layer
        List<Member> curentLayer;
        while(!s.empty()){
            curentLayer.push_back(s.top());
            s.pop();
        }
        
        //Print them 
        for(auto directFriend : curentLayer){
            //Add the friend to map to avoid duplicate
            record[Member]=1;
            
            //level 0 is self..
            if(level>0)
                cout<<directFriend.name<<" "<<directFriend.email<<endl;
            
            for(auto nexttocheck: directFriend.friends){
                //And remove duplicate
                if(record.find(nexttocheck)!=record.end())
                    s.push(nexttocheck);
            }
        }
        //we can also recursively call the printSocialGraph function
        level++;
    }
}