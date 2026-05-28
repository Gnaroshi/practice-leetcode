// problem: 3093. Longest Common Suffix Queries

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

// first time to using class for problem solving
const int MX = 0x3f3f3f3f;
class Trie {
public:
  Trie() : tot_(0) {
    for (int i = 0; i < N; i++) {
      memset(tr_[i], 0, sizeof(tr_[i]));
      min_len_[i] = MX;
      idx_[i] = MX;
    }
  }

  void clear() {
    for (int i = 0; i <= tot_; i++) {
      memset(tr_[i], 0, sizeof(tr_[i]));
      min_len_[i] = MX;
      idx_[i] = MX;
    }
    tot_ = 0;
  }

  void insert(const string &s, int idx) {
    int p = 0;
    if (min_len_[p] > s.length()) {
      min_len_[p] = s.length();
      idx_[p] = idx;
    }
    for (auto &i : s) {
      int cur = i - 'a';
      if (tr_[p][cur] == 0) {
        tr_[p][cur] = ++tot_;
      }
      p = tr_[p][cur];
      if (min_len_[p] > s.length()) {
        min_len_[p] = s.length();
        idx_[p] = idx;
      }
    }
  }

  int query(const string &s) {
    int p = 0;
    for (auto &i : s) {
      int cur = i - 'a';
      if (tr_[p][cur] != 0) {
        p = tr_[p][cur];
      } else {
        break;
      }
    }
    return idx_[p];
  }

private:
  static constexpr int N = 500005, M = 26;
  int tot_;
  int tr_[N][M];
  int min_len_[N];
  int idx_[N];
};

Trie tr;

class Solution {
public:
  vector<int> stringIndices(vector<string> &wordsContainer,
                            vector<string> &wordsQuery) {
    tr.clear();
    int n = wordsContainer.size(), m = wordsQuery.size();
    vector<int> ret(m);
    for (int i = 0; i < n; i++) {
      string s = wordsContainer[i];
      reverse(s.begin(), s.end());
      tr.insert(s, i);
    }

    for (int i = 0; i < m; i++) {
      string s = wordsQuery[i];
      reverse(s.begin(), s.end());
      ret[i] = tr.query(s);
    }

    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
