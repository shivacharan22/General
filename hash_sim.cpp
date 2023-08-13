
#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

struct contributor
{
    string name;
    vector<pair<string,int>> skill;
    contributor(string a):name(a){}
};

struct project
{
    string name;
    int duration;
    int score;
    int best_before;
    int roles;
    vector<pair<string,int>> req_skill;
};

void solve()
{
   vector<contributor> contri;
   vector<project> proj;
   
   double n_contributer; double no_projects;string temp_name; int no_skills;string fak_skil_na;string fak_skil_na;int sk_lev;
   cin>>n_contributer;cin>>no_projects;
   for(int i = 0;i<n_contributer;i++){
       cin>>temp_name;
       contributor c(temp_name);
       cin>>no_skills;
       for(int j = 0;j<no_skills;j++){
           cin>>fak_skil_na;cin>>sk_lev;
           c.skill.push_back({fak_skil_na,sk_lev});
       }
       contri.push_back(c);
   }
   double projectss;string na_pro;int no_days;int score_pro;int before_before; int roless;string r_name;int lev; 
   cin>>projectss;
   for(int k = 0;k<projectss;k++){
       cin>>na_pro;
       project p;
       p.name = na_pro;
       cin>>no_days;cin>>score_pro;cin>>before_before;cin>>roless;
       p.score = score_pro;
       p.best_before = before_before;
       p.roles = roless;
       p.duration = no_days;
       for (int g = 0;g<roless;g++){
           cin>>r_name;
           cin>>lev;
           p.req_skill.push_back({r_name,lev});
       }
       proj.push_back(p);
   }
    double no_pro1;string proj_name1;string name1;string name2;
    cin>>no_pro1;
    double score;
    int time = 0;
    for(int n1 = 0; n1<no_pro1;n1++){
        cin>>proj_name1;cin>>name1;name2;
        while(!projected_done){
            if (time <req_time){
                contin
            }
        }
        if (days>best_before){

            }
        else
    }

   
   // int res = result.size(); 
    // string resr = to_string(res);
    // for (auto c:result)
    // {
    //     resr += " " + c;
    // }
    // ofstream file;
    // file.open("C:\\Users\\91965\\Elaborate_output.txt");
    // file<<resr;
    // file.close();
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
}