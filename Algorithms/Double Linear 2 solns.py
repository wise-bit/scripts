def dbl_linear(n):
    set_ = list()
    x = 1
    index = 0
    set_.append(x)
    while len(set_) <= n:
        tmp_set_ = set_
        for x in set_:
            tmp_set_.append(2*x+1)
            tmp_set_.append(3*x+1)
        set_ = tmp_set_
    set_.sort()
    return set_


def dbl_linear(n):
    arr = [1]
    y_incr, z_incr = 0, 0
    for i in range(n):
        y = arr[y_incr]*2+1
        z = arr[z_incr]*3+1
        if y <= z:
            arr.append(y)
            y_incr += 1
            if y == z:
                z_incr += 1
        else:
            arr.append(z)
            z_incr += 1
    return arr[n]

'''

in cpp

#include <iostream>
#include <vector>
#include <string>

static int dblLinear(int n){
    std::vector<int> arr = {n};
    int y_incr = 0;
    int z_incr = 0;
    for (int i = 0; i < n; i++){
        int y = arr[y_incr]*2+1;
        int z = arr[z_incr]*3+1;
        if (y <= z){
            arr.push_back(y);
            y_incr += 1;
            if (y == z){
                z_incr += 1;
            }
        } else {
            arr.push_back(z);
            z_incr += 1;
        }
    }
    return arr[n];
}

int main(){
    std::cout << dblLinear(10);
    return 0;
}

'''