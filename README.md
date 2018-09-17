## LeetCode Summary

636. Exclusive Time of Functions: 栈

547. Friend Circles：DFS

655. Print Binary Tree：二叉树

221. Maximal Square：DP

85. Maximal Rectangle：单调栈(Histogram变形)

84. Largest Rectangle in Histogram：单调栈

463. Island Perimeter：简单对比(map+zip的使用) or 遍历查找

695. Max Area of Island：DFS(本来想用DP，发现出不来)

200. Number of Islands：DFS

731. My Calendar II：小空间匹配

729. My Calendar I：同上

*732. My Calendar III：难，小数据量可以用线段匹配，大数据量要用LCT(但是这东西看不懂)

606. Construct String from Binary Tree：中序遍历

127. Word Ladder：BFS，需要考虑wordlist的类型，如果是list会超时，所以需要选用set

*126. Word Ladder II：待完成

718. Maximum Length of Repeated Subarray：基本匹配

209. Minimum Size Subarray Sum：注意避免TLE

76. Minimum Window Substring：因为元素个数问题，不能用set

324. Wiggle Sort II：基于中间值的三段排序，或者直接排序

75. Sort Colors：/

71. Simplify Path：split和join的使用

5. Longest Palindromic Substring：和718不同，首先需要判断回文点

647. Palindromic Substrings：题目要求低，所以O(n2)的不会TLE，还是马拉车算法学习一个

214. Shortest Palindrome：easy game

516. Longest Palindromic Subsequence：DP

*730. Count Different Palindromic Subsequences：比较难的DP，需要重新做

135. Candy：很简单的一道算法题，一开始没想明白

122. Best Time to Buy and Sell Stock II：基础贪婪

121. Best Time to Buy and Sell Stock：Kadane算法（最大子序列和）

123. Best Time to Buy and Sell Stock III：DP

188. Best Time to Buy and Sell Stock IV：DP，需要判断交易次数和价格数量的大小关系，不然会爆内存

105. Construct Binary Tree from Preorder and Inorder Traversal：递归建树

106. Construct Binary Tree from Inorder and Postorder Traversal：同上

173. Binary Search Tree Iterator：题目描述不好，就是做一个inorder遍历

94. Binary Tree Inorder Traversal：递归

144. Binary Tree Preorder Traversal：同上

145. Binary Tree Postorder Traversal：同上

468. Validate IP Address：看起来很简单，但有很多坑

132. Palindrome Partitioning II：DP

131. Palindrome Partitioning：循环+递归

661. Image Smoother：算法很简单，但是各种极端情况都需要考虑

42. Trapping Rain Water：双指针

*407. Trapping Rain Water II：BFS

373. Find K Pairs with Smallest Sums：堆

378. Kth Smallest Element in a Sorted Matrix：bisect的灵活使用

*719. Find K-th Smallest Pair Distance：和378类似，但容易TLE，难

273. Integer to English Words：注意打表的拼写

12. Integer to Roman：暴力打表

13. Roman to Integer：判断低位字母的位置，标flag

101. Symmetric Tree：递归

*207. Course Schedule：DFS

383. Ransom Note：统计

*691. Stickers to Spell Word：DP，比较难

1. Two Sum：/

167. Two Sum II - Input array is sorted：双指针，按1的做法会TLE

653. Two Sum IV - Input is a BST：/

381. Insert Delete GetRandom O(1) - Duplicates allowed：构造完整的数据结构

380. Insert Delete GetRandom O(1)：同上

2. Add Two Numbers：/

445. Add Two Numbers II：/

492. Construct the Rectangle：/

459. Repeated Substring Pattern：/

686. Repeated String Match：/

28. Implement strStr()：/

234. Palindrome Linked List.py：/

206. Reverse Linked List：/

92. Reverse Linked List II：比上一个调起来稍难

160. Intersection of Two Linked Lists：/

*143. Reorder List：in-place，难

398. Random Pick Index：/

382. Linked List Random Node：Reservoir Sampling，水池抽样

69. Sqrt(x)：/

*316. Remove Duplicate Letters：难，启发式思路

367. Valid Perfect Square：/

633. Sum of Square Numbers：/

50. Pow(x, n)：/

372. Super Pow：注意TLE

65. Valid Number：trick method，还可以用re和DFA敏感字过滤

8. String to Integer (atoi)：注意细节

55. Jump Game：/

763. Partition Labels：/

767. Reorganize String：/

303. Range Sum Query - Immutable：求和数组

307. Range Sum Query - Mutable：线段树(还可以用BIT)

304. Range Sum Query 2D - Immutable：求和数组强化版

3. Longest Substring Without Repeating Characters：双指针

4. Median of Two Sorted Arrays.py：/

766. Toeplitz Matrix：/

6. ZigZag Conversion：模拟

678. Valid Parenthesis String：/

556. Next Greater Element III：注意32bit数，判断上限

496. Next Greater Element I：/

503. Next Greater Element II：/

20. Valid Parentheses：/

*591. Tag Validator：RE

22. Generate Parentheses：/

*32. Longest Valid Parentheses：DP

*301. Remove Invalid Parentheses：BFS

283. Move Zeroes：/

27. Remove Element：/

26. Remove Duplicates from Sorted Array：/

203. Remove Linked List Elements：/

413. Arithmetic Slices：/

522. Longest Uncommon Subsequence II：/

295. Find Median from Data Stream：heap

480. Sliding Window Median：/

100. Same Tree：/

669. Trim a Binary Search Tree：/

623. Add One Row to Tree：/

213. House Robber II：/

198. House Robber：/

337. House Robber III：/

637. Average of Levels in Binary Tree：/

102. Binary Tree Level Order Traversal：/

107. Binary Tree Level Order Traversal II：/

124. Binary Tree Maximum Path Sum：/

112. Path Sum：negative value is possible

113. Path Sum II：/

437. Path Sum III：/

798. Smallest Rotation with Highest Score：/

43. Multiply Strings：/

66. Plus One：/

67. Add Binary：/

415. Add Strings：/

172. Factorial Trailing Zeroes：/

233. Number of Digit One：/

9. Palindrome Number：/

326. Power of Three：/

231. Power of Two：/

342. Power of Four：/

754. Reach a Number：考虑如何达到最小

258. Add Digits：/

645. Set Mismatch：/

357. Count Numbers with Unique Digits：/