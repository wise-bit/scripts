#include <string>
#import <algorithm>
#include <vector>

class Kata
{

public:
    std::vector<std::string> sortByLength(std::vector<std::string> array)
    {
        int changes = 1;
        while (changes != 0){
            changes = 0;
            int length = 0;
            try {length = sizeof(array);}
            catch (...) {length = 0;}
            for (int i = 0; i < length-1; i++) {
            
                int l1 = 0; int l2 = 0;
                try {l1 = array[i].length();}
                catch (...) {l1 = 0;}
                try {l2 = array[i+1].length();}
                catch (...) {l2 = 0;}
                
                if (l1 > l2){
                    std::string temp = array[i+1];
                    array[i+1] = array[i];
                    array[i] = temp;
                    changes += 1;
                    // return array;
                }
            }
        }
        return array;
    }
};