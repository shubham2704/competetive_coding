#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__);fflush(stderr);
#else
	#define eprintf(...) 42
#endif

using ll = long long;
using ld = long double;
using uint = unsigned int;
using ull = unsigned long long;
template<typename T>
using pair2 = pair<T, T>;
using pii = pair<int, int>;
using pli = pair<ll, int>;
using pll = pair<ll, ll>;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
ll myRand(ll B) {
	return (ull)rng() % B;
}

#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second

clock_t startTime;
double getCurrentTime() {
	return (double)(clock() - startTime) / CLOCKS_PER_SEC;
}

int solve() {
	int n;
	string a, b;
	cin >> n >> a;
	int ans = 0;
	for (int i = 1; i < n; i++) {
		cin >> b;
		if ((int)a.size() < (int)b.size()) {
			a = b;
			continue;
		}
		int f = 0;
		for (int i = 0; f == 0 && i < (int)b.size(); i++) {
			if (a[i] == b[i]) continue;
			if (a[i] < b[i])
				f = 1;
			else
				f = -1;
		}
		if (f == 1) {
			while((int)b.size() < (int)a.size()) {
				b.push_back('0');
				ans++;
			}
			a = b;
			continue;
		}
		if (f == -1) {
			while((int)b.size() <= (int)a.size()) {
				b.push_back('0');
				ans++;
			}
			a = b;
			continue;
		}
		int p = (int)a.size() - 1;
		while(p >= (int)b.size() && a[p] == '9') p--;
		if (p < (int)b.size()) {
			while((int)b.size() <= (int)a.size()) {
				b.push_back('0');
				ans++;
			}
			a = b;
			continue;
		}
		while((int)b.size() < p) {
			b.push_back(a[(int)b.size()]);
			ans++;
		}
		b.push_back(a[(int)b.size()] + 1);
		ans++;
		while((int)b.size() < (int)a.size()) {
			b.push_back('0');
			ans++;
		}
		a = b;
	}
	return ans;
}

int main()
{
	startTime = clock();
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: %d\n", i, solve());
	}

	return 0;
}
