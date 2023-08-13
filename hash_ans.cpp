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
    bool operator< (const project &other) const {
        return  score < other.score;}
    vector<pair<string,int>> req_skill;
};

void solve()
{
   vector<contributor> contri;
   vector<project> proj;
   
   double n_contributer; double no_projects;string temp_name; int no_skills;string fak_skil_na;int sk_lev;
   cin>>n_contributer;cin>>no_projects;
   for(int i = 0;i<n_contributer;i++)
   {
       cin>>temp_name;
       contributor c(temp_name);
       cin>>no_skills;
       for(int j = 0;j<no_skills;j++)
       {
           cin>>fak_skil_na;cin>>sk_lev;
           c.skill.push_back({fak_skil_na,sk_lev});
       }
       contri.push_back(c);
   }
   double projectss;string na_pro;int no_days;int score_pro;int before_before; int roless;string r_name;int lev; 
   for(int k = 0;k<no_projects;k++)
   {
       cin>>na_pro;
       project p;
       p.name = na_pro;
       cin>>no_days;cin>>score_pro;cin>>before_before;cin>>roless;
       p.score = score_pro;
       p.best_before = before_before;
       p.roles = roless;
       p.duration = no_days;
       for (int g = 0;g<roless;g++)
       {
           cin>>r_name;
           cin>>lev;
           p.req_skill.push_back({r_name,lev});
       }
       proj.push_back(p);
   }
    sort(proj.begin(),proj.end());
    vector<pair<int,int>> sorting;
    for(int n2 = 0;n2<proj.size();n2++)
    {
        sorting.push_back({n2,proj[n2].duration});
    }
    std::sort(sorting.begin(), sorting.end(), [](auto &left, auto &right) {
    return left.second < right.second;
    });
    cout<<proj[0].name;
    vector<pair<string,vector<string>>> result;
    for (int n3 =0; n3<sorting.size();n3++)
    {
        vector<string> temp_res;
        cout<<sorting.size();
        for(int n4 = 0; n4<proj[sorting[n3].first].roles;n4++)
        {
            for(int n5 = 0;n5<contri.size();n5++)
            {
                for(int n6 = 0;n6<contri[n5].skill.size();n6++)
                {
                    if ((proj[sorting[n3].first].req_skill[n4].first == contri[n5].skill[n6].first) && (proj[sorting[n3].first].req_skill[n4].second == contri[n5].skill[n6].second-1))
                    {
                        cout<<proj[sorting[n3].first].req_skill[n4].first;cout<<contri[n5].skill[n6].first;
                        if(std::find(temp_res.begin(), temp_res.end(), contri[n5].name) == temp_res.end()) 
                        {
                            temp_res.push_back(contri[n5].name);
                            contri[n5].skill[n6].second+=1;
                        }
                    }
                    else if ((proj[sorting[n3].first].req_skill[n4].first == contri[n5].skill[n6].first) && (proj[sorting[n3].first].req_skill[n4].second < contri[n5].skill[n6].second-1)) 
                    {
                            temp_res.push_back(contri[n5].name);
                    }
                }
            }
         }
         result.push_back({proj[sorting[n3].first].name,temp_res}); 
    }

    int res = result.size(); 
    string resr = to_string(res);
    string p;
    for (auto c:result)
    {
        for (auto k:c.second)
        {
            p += k + " "; 
        }
        
        resr += "/n" + c.first +"/n" + p;  
    }
    ofstream file("first.txt");
    file<<resr;
    file.close();

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
}