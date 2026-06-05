// problem: 3753. Total Waviness of Numbers in Range II

#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;
using ll = long long;

using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vvi = vector<vi>;
using vpi = vector<pii>;
using vvpi = vector<vpi>;
using vb = vector<bool>;
using vd = vector<double>;
using vs = vector<string>;
using vll = vector<ll>;
using vvll = vector<vll>;
using vpll = vector<pll>;
using vvpll = vector<vpll>;
using qi = queue<int>;
using si = stack<int>;

class Solution {
  const int MX = 16;

public:
  long long totalWaviness(long long a, long long b) {
    auto solve = [&](long long num) -> long long {
      if (num < 100) {
        return 0;
      }
      string s = to_string(num);
      int n = s.size();

      long long memo_cnt[MX][10][10];
      long long memo_sum[MX][10][10];

      memset(memo_cnt, -1, sizeof(memo_cnt));
      memset(memo_sum, -1, sizeof(memo_sum));

      auto dfs = [&](this auto &&dfs, int pos, int prev, int curr, bool isLimit,
                     bool isLeading) -> pair<long, long> {
        if (pos == n) {
          return {1, 0};
        }
        if (!isLimit && !isLeading && prev >= 0 && curr >= 0) {
          if (memo_cnt[pos][prev][curr] != -1) {
            return {memo_cnt[pos][prev][curr], memo_sum[pos][prev][curr]};
          }
        }

        long long cnt = 0, sum = 0;
        int up = isLimit ? s[pos] - '0' : 9;
        for (int digit = 0; digit <= up; digit++) {
          bool newLeading = isLeading && (digit == 0);
          int newPrev = curr;
          int newCurr = newLeading ? -1 : digit;
          auto [subCnt, subSub] = dfs(pos + 1, newPrev, newCurr,
                                      isLimit && (digit == up), newLeading);

          if (!newLeading && prev >= 0 && curr >= 0) {
            if ((prev < curr && curr > digit) ||
                (prev > curr && curr < digit)) {
              sum += subCnt;
            }
          }

          cnt += subCnt;
          sum += subSub;
        }

        if (!isLimit && !isLeading && prev >= 0 && curr >= 0) {
          memo_cnt[pos][prev][curr] = cnt;
          memo_sum[pos][prev][curr] = sum;
        }

        return {cnt, sum};
      };

      auto [_, totalSum] = dfs(0, -1, -1, true, true);
      return totalSum;
    };

    return solve(b) - solve(a - 1);
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
