#include <vector>
#include <string>
#include <iostream>

int stray(std::vector<int> numbers) {
    for (int i = 0; i < numbers.size()-1; i++){
        if (numbers[i] != numbers[i+1]){
            return (i == 0 ? (numbers[i] == numbers[i+2] ? numbers[i+1] : numbers[i]) : (numbers[i] == numbers[i-1] ? numbers[i+1] : numbers[i]));
        }
    }
};

int main(){
	std::cout << stray({1, 1, 2});
}

// Describe(solution_test)
// {
//     It(simple_array_1)
//     {
//         Assert::That(stray({1, 1, 2}), Equals(2));
//     }
//     It(simple_array_2)
//     {
//         Assert::That(stray({3, 17, 17, 17, 17, 17, 17}), Equals(3));
//     }
// };