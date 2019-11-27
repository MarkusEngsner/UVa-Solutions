#include <iostream>
#include <vector>

bool is_jolly(std::vector<int> input) {
    std::vector<bool> is_used(input.size() - 1, false);
    for (int i = 1; i < input.size(); i++) {
        auto difference = abs(input[i - 1] - input[i]);
        if (difference >= input.size() || difference == 0)
            return false;
        if (is_used[difference - 1])
            return false;
        is_used[difference - 1] = true;
    }
    return true;
}

int main() {
    int n = 0;
    int temp = 0;
    std::vector<int> input;
    while (std::cin >> n) {
        input.clear();
        for (int i = 0; i < n; i++) {
            std::cin >> temp;
            input.push_back(temp);
        }
        if (is_jolly(input)) {
            std::cout << "Jolly\n";
        } else {
            std::cout << "Not jolly\n";
        }
    }
    return 0;
}
