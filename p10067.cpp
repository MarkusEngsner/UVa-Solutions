#include <queue>
#include <iostream>
#include <string>
#include <cstring>
#include <fstream>

void connected(int v, const int *below, const int *above, int *target) {
  int one = v % 10;
  int ten = v % 100 - one;
  int hundred = v % 1000 - ten - one;
  int thousand = v % 10000 - hundred - ten - one;
  target[0] = thousand + hundred + ten + below[one];
  target[1] = thousand + hundred + ten + above[one];
  target[2] = thousand + hundred + above[ten / 10] * 10 + one;
  target[3] = thousand + hundred + below[ten / 10] * 10 + one;
  target[4] = thousand + above[hundred / 100] * 100 + ten + one;
  target[5] = thousand + below[hundred / 100] * 100 + ten + one;
  target[6] = above[thousand / 1000] * 1000 + hundred + ten + one;
  target[7] = below[thousand / 1000] * 1000 + hundred + ten + one;
}

int fewestTurns(const int &start, const int &end, const int edges[10000][8], bool *discovered, int *cost) {
  if (start == end)
    return 0;
  if (discovered[start] || discovered[end])
    return -1;
  std::queue<int> q;
  q.push(start);
  discovered[start] = true;
  memset(cost, -1, sizeof(int) * 10000);
  cost[start] = 0;
  while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (int i = 0; i < 8; i++) {
      if (!discovered[edges[v][i]]) {
        q.push(edges[v][i]);
        cost[edges[v][i]] = cost[v] + 1;
        discovered[edges[v][i]] = true;
        if (edges[v][i] == end)
          return cost[edges[v][i]];
      }
    }
  }
  return -1;
}

inline int toNumber() {
  std::string x;
  std::getline(std::cin, x);
  //std::cin >> x;
  //int a, b, c, d;
  //std::cin >> a >> b >> c >> d;
  return (x[0] - 48) * 1000 + (x[2] - 48) * 100 + (x[4] - 48) * 10 + (x[6] - 48);
}

std::string handleCase(const int edges[10000][8], int *cost) {
  int start = toNumber();
  int end = toNumber();
  int forbidden_count;
  std::cin >> forbidden_count;
  bool discovered[10000];
  std::memset(discovered, false, sizeof(discovered));
  int temp;
  for (int i = 0; i < forbidden_count; i++) {
    temp = toNumber();
    discovered[temp] = true;
  }
  return std::to_string(fewestTurns(start, end, edges, discovered, cost)) + '\n';
}

int main() {
/*
  std::ifstream in("in.txt");
  std::cin.rdbuf(in.rdbuf());
*/
  std::ios_base::sync_with_stdio(false);
  std::string result = "";
  int above[10], below[10];
  for (int i = 0; i < 10; i++) {
    above[i] = (i + 1) % 10;
    below[i] = (i - 1) % 10;
  }
  below[0] = 9; // exception from loop
  int edge_lookup[10000][8];
  for (int i = 0; i < 10000; i++) {
    connected(i, below, above, edge_lookup[i]);
  }
  int cost[10000];
  int case_count;
  std::cin >> case_count;
  for (int i = 0; i < case_count; i++)
    result.append(handleCase(edge_lookup, cost));
  std::cout << result;
}
