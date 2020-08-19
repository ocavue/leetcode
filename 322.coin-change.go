/*
submits:
 - date: 2020-07-07
   cheating: false
labels: [dp]
*/

/*
 * @lc app=leetcode id=322 lang=golang
 *
 * [322] Coin Change
 *
 * https://leetcode.com/problems/coin-change/description/
 *
 * algorithms
 * Medium (33.70%)
 * Likes:    4097
 * Dislikes: 135
 * Total Accepted:    405K
 * Total Submissions: 1.2M
 * Testcase Example:  '[1,2,5]\n11'
 *
 * You are given coins of different denominations and a total amount of money
 * amount. Write a function to compute the fewest number of coins that you need
 * to make up that amount. If that amount of money cannot be made up by any
 * combination of the coins, return -1.
 *
 * Example 1:
 *
 *
 * Input: coins = [1, 2, 5], amount = 11
 * Output: 3
 * Explanation: 11 = 5 + 5 + 1
 *
 * Example 2:
 *
 *
 * Input: coins = [2], amount = 3
 * Output: -1
 *
 *
 * Note:
 * You may assume that you have an infinite number of each kind of coin.
 *
 */

package main

// @lc code=start

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func coinChange(coins []int, targetAmount int) int {
	if targetAmount == 0 {
		return 0
	}

	// index 是硬币的金额之和
	// value 是凑出这个金额所需要的最少的硬币数量
	amountMap := make([]int, targetAmount+1)

	for amount := 1; amount <= targetAmount; amount++ {
		for _, coin := range coins {
			if coin == amount {
				amountMap[amount] = 1
				break
			}
			if amount-coin > 0 {
				rest := amountMap[amount-coin]
				if rest != 0 {
					if amountMap[amount] == 0 {
						amountMap[amount] = rest + 1
					} else {
						amountMap[amount] = min(rest+1, amountMap[amount])
					}
				}
			}
		}
	}
	// fmt.Println(amountMap)

	if amountMap[targetAmount] == 0 {
		return -1
	}
	return amountMap[targetAmount]
}

// @lc code=end
