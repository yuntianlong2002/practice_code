//Kind of like build a graph

//Suppose the getMonthlyAmazonDollars get how much dollors a member spend each month,
//Then he/she will get 0.1*getMonthlyAmazonDollars() for his own

double calculatePayout(Member member){
    //get own payout
    double rv=member.getMonthlyAmazonDollars()*0.1;
    for(auto recruit: member.getRecruitedMembers()){
        rv+=getRecruitValue(recruit);
    }
    return rv;
}

//Recursive call
double getRecruitValue(Member member){
    double rv=member.getMonthlyAmazonDollars();
    for(auto recruit: member.getRecruitedMembers()){
        rv+=getRecruitValue(recruit);
    }
    return rv*0.04;//In each layer, I compute the value for my sponser
}