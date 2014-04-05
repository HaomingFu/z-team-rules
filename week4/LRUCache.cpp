/*
 *  From http://oj.leetcode.com/problems/lru-cache/
 *  An implementation for Least-Recently-Used Cache
 *  Date: April 5, 2014
 *  By Yao
 *  Accpted
 */
#include <iostream>

using namespace std;


class LRUCache{
    public: 
        LRUCache(int capacity){
            limit = capacity;
            len = 0;
            ts = 1;

            for(int i=0;i<limit;++i)
                a[i][0]=a[i][1]=a[i][2]=0;
            
        }

        int get(int key){
            int i;

            for(i=0;i<len && a[i][0]!=key;++i){}

            if(i<len){
                if(a[i][2]!=ts-1) //we just accessed to a[i] 
                    a[i][2]=ts++;

                return a[i][1];
            }
            return -1;
        }

        void set(int key, int value){
            int i=0;
            for(i=0;i<len && a[i][0]!=key;++i){}
            if(i<len){
                a[i][1]=value;
                a[i][2]=ts++;
            }
            else{

                if(len<limit){
                    a[len][0]=key;
                    a[len][1]=value;
                    a[len][2]=ts++;
                    len++;
                }
                else{  //find the leaset recently used cells, the cell with least timestamp
                    int index = 0;
                    int least = a[0][2];
                    for(int i=1;i<limit;++i){
                        if(a[i][2]<least){
                            least = a[i][2];
                            index = i;
                        }
                    }
                    a[index][0]=key;
                    a[index][1]=value;
                    a[index][2]=ts++;
                }
            }
        }

    private:
        int limit;
        int len;
        int ts; //timestamp
        int a[10000][3];
};

int main(){
    LRUCache cache(2);
    cache.set(2,1);
    cache.set(2,2);
    cout<<cache.get(2)<<endl;
    cache.set(1,1);
    cache.set(4,1);
    cout<<cache.get(2)<<endl;
}
