/*
submits:
- date: 2020-08-19
  cheating: false
*/

/*
 * @lc app=leetcode id=258 lang=golang
 *
 * [258] Add Digits
 *
 * https://leetcode.com/problems/add-digits/description/
 *
 * algorithms
 * Easy (55.63%)
 * Likes:    879
 * Dislikes: 1148
 * Total Accepted:    318.4K
 * Total Submissions: 552K
 * Testcase Example:  '38'
 *
 * Given a non-negative integer num, repeatedly add all its digits until the
 * result has only one digit.
 *
 * Example:
 *
 *
 * Input: 38
 * Output: 2
 * Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
 * Since 2 has only one digit, return it.
 *
 *
 * Follow up:
 * Could you do it without any loop/recursion in O(1) runtime?
 */

package main

// @lc code=start

import (
	"strconv"
)

func addDigits(num int) int {
	if num < 10 {
		return num
	}

	s := strconv.Itoa(num)

	var sum int64
	for _, char := range s {
		intt, err := strconv.ParseInt(string(char), 10, 32)
		if err != nil {
			panic(err)
		}
		sum += intt
	}

	return addDigits(int(sum))
}

// @lc code=end
